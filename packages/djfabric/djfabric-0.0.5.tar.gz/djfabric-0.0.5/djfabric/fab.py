import os
import sys
import environ

from datetime import datetime
from os.path import join, dirname
from fabric.api import env, run, local, sudo, cd, prefix, get, put
from contextlib import contextmanager


__all__ = [
    'pull',
    'deploy',
    'restart',
    'dump_db',
    'fetch_db',
    'fetch_media',
    'setup',
    'upload_env',
    'cert',
    'nginx_conf',
    'restart_nginx',
    'supervisor_conf',
    'unfold_to_server',
    'upload_db',
    'push_db',
    'clean_thumbnail',
]

config = environ.Env()
_STORAGE = {}


@contextmanager
def source():
    with prefix('source ~/sites/{}/env/bin/activate'.format(config('DOMAIN'))):
        yield


def pull():
    run('git pull origin master')


def deploy():
    with cd('~/sites/{}/{}/'.format(config('DOMAIN'), config('PROJECT_NAME'))):
        pull()

        with source():
            run('pip install -r ./requirements.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')
            run('python manage.py sync_translation_fields --noinput')

    restart()


def restart():
    project_name = config('PROJECT_NAME')

    with cd('~/sites/{}/{}/'.format(config('DOMAIN'), project_name)):
        pull()

    sudo('sudo supervisorctl restart {}'.format(config('PROJECT_NAME')))

    if config('CELERY') == 'on':
        sudo('sudo supervisorctl restart {}_celery'.format(project_name))
        sudo('sudo supervisorctl restart {}_celery_beat'.format(project_name))


def dump_db():
    file_path = '/home/dev/{}_{}.sql'.format(
        config('DB_NAME'),
        datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    )

    run('pg_dump {} > {}'.format(config('DB_NAME'), file_path))

    get(file_path, file_path)

    return file_path


def fetch_db():
    file_path = dump_db()

    local('sudo -u postgres psql -c "DROP DATABASE IF EXISTS {};"'.format(
        config('DB_NAME')
    ))

    local('sudo -u postgres psql -c "CREATE DATABASE {};"'.format(
        config('DB_NAME')
    ))

    local('sudo -u postgres psql -d {} -f {}'.format(
        config('DB_NAME'),
        file_path
    ))

    run('rm {}'.format(file_path))
    local('rm {}'.format(file_path))


def upload_db():
    file_path = '/home/dev/{}_{}.sql'.format(
        config('DB_NAME'),
        datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    )

    local('pg_dump {} > {}'.format(config('DB_NAME'), file_path))

    put(file_path, file_path)

    return file_path


def push_db():
    file_path = upload_db()

    run('sudo -u postgres psql -c "CREATE DATABASE {};"'.format(
        config('DB_NAME')
    ))

    run('sudo -u postgres psql -d {} -f {}'.format(
        config('DB_NAME'),
        file_path
    ))

    run('rm {}'.format(file_path))
    local('rm {}'.format(file_path))


def setup():
    frame = sys._getframe()
    project_dir = dirname(frame.f_back.f_code.co_filename)
    config.read_env(join(project_dir, '.env'))
    env.project_dir = project_dir
    env.user = 'dev'
    env.hosts = [config('HOST')]
    env.password = config('HOST_PASSWORD')


def upload_env():
    put(
        join(env.project_dir, '.env'),
        '/home/dev/sites/{}/{}/.env'.format(
            config('DOMAIN'), config('PROJECT_NAME'))
    )


def cert():
    sudo(f"sudo certbot certonly --webroot -d {config('DOMAIN')} -w /var/www/html")
    sudo("sudo nginx -t")
    restart_nginx()


def _get_tmp_dir():
    tmp_dir = join(env.project_dir, 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)
    return tmp_dir


def _write_file(tmp_file_path, lines, params):
    with open(tmp_file_path, 'w') as file:
        file.write("\n".join([line % params for line in lines]))


def nginx_conf():
    tmp_dir = _get_tmp_dir()
    project_name = config('PROJECT_NAME')
    tmp_file_path = join(tmp_dir, project_name)

    _write_file(
        tmp_file_path=tmp_file_path,
        lines=[
            "server {",
            "    listen 80;",
            "    server_name %(domain)s www.%(domain)s;",
            "    return 301 https://%(domain)s$request_uri;",
            "}",
            "server {",
            "    server_name %(domain)s;",
            "    listen 443 ssl http2;",
            "",
            "    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:AES256+EECDH:AES256+EDH';",
            "",
            "    ssl_certificate /etc/letsencrypt/live/%(domain)s/fullchain.pem;",
            "    ssl_certificate_key /etc/letsencrypt/live/%(domain)s/privkey.pem;",
            "    ssl_trusted_certificate /etc/letsencrypt/live/%(domain)s/chain.pem;",
            "",
            "    client_max_body_size 4G;",
            "    ssl_stapling on;",
            "    ssl_stapling_verify on;",
            "",
            '    add_header Strict-Transport-Security "max-age=31536000";',
            '    add_header X-Frame-Options "SAMEORIGIN";',
            "",
            "    location / {",
            "        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;",
            "        proxy_set_header X-Forwarded-Proto https;",
            "        proxy_set_header Host $host;",
            "        proxy_redirect off;",
            "        proxy_pass http://unix:/home/dev/sites/%(domain)s/%(project_name)s/%(project_name)s.sock;",
            "    }",
            "",
            "    location /static/ {",
            "        root /home/dev/sites/%(domain)s/public;",
            "        expires 30d;",
            "    }",
            "    location /media/ {",
            "        root /home/dev/sites/%(domain)s/public;",
            "        expires 30d;",
            "    }",
            "    location /.well-known {",
            "        root /var/www/html;",
            "    }",
            "    location /robots.txt {",
            "        alias /home/dev/sites/%(domain)s/public/robots.txt;",
            "    }",
            "}"
        ],
        params={
            "domain": config("DOMAIN"),
            "project_name": project_name,
        }
    )

    put(
        tmp_file_path,
        f"/etc/nginx/sites-available/{project_name}",
        use_sudo=True
    )

    sudo(f"sudo ln -s /etc/nginx/sites-available/{project_name} /etc/nginx/sites-enabled")
    restart_nginx()


def restart_nginx():
    sudo("sudo nginx -t")
    sudo("sudo systemctl restart nginx")


def supervisor_conf():
    tmp_dir = _get_tmp_dir()
    runsite_tmp_file_path = join(tmp_dir, config('PROJECT_NAME') + ".conf")
    _write_file(
        tmp_file_path=runsite_tmp_file_path,
        lines=[
            "[program:%(project_name)s]",
            "command=bash /home/dev/runsite.bash -d %(domain)s -n %(project_name)s -w 3 -s core.settings",
            "user=dev",
            "stdout_logfile=/home/dev/sites/%(domain)s/logs/supervisor.log",
            "autostart=True",
            "autorestart=true",
            "redirect_stderr=true"
        ],
        params={
            "domain": config("DOMAIN"),
            "project_name": config('PROJECT_NAME'),
        }
    )
    put(
        runsite_tmp_file_path,
        "/etc/supervisor/conf.d",
        use_sudo=True
    )

    if config('CELERY') == 'on':
        celery_tmp_file_path = join(tmp_dir, config('PROJECT_NAME') + "-celery.conf")
        _write_file(
            tmp_file_path=celery_tmp_file_path,
            lines=[
                "[program:%(project_name)s_celery]",
                "command=/home/dev/sites/%(domain)s/env/bin/celery -A core worker --loglevel=INFO --concurrency=10 %(worker)s --uid=1000",
                "directory=/home/dev/sites/%(domain)s/%(project_name)s",
                "autostart=true",
                "autorestart=true",
                "numprocs=1",
                "stderr_logfile=/home/dev/sites/%(domain)s/logs/celery.err.log",
                "stdout_logfile=/home/dev/sites/%(domain)s/logs/celery.out.log",
                "startsecs=10",
                "priority=1000"
            ],
            params={
                "domain": config("DOMAIN"),
                "project_name": config('PROJECT_NAME'),
                "worker": "-n worker1.%%h"
            }
        )
        put(
            celery_tmp_file_path,
            "/etc/supervisor/conf.d",
            use_sudo=True
        )

        celery_beat_tmp_file_path = join(tmp_dir, config('PROJECT_NAME') + "-celery-beat.conf")
        _write_file(
            tmp_file_path=celery_beat_tmp_file_path,
            lines=[
                "[program:%(project_name)s_celery_beat]",
                "command=/home/dev/sites/%(domain)s/env/bin/celery -A core beat --max-interval=7200 --loglevel=INFO",
                "directory=/home/dev/sites/%(domain)s/%(project_name)s",
                "autostart=true",
                "autorestart=true",
                "numprocs=1",
                "startsecs=10",
                "priority=1000"
            ],
            params={
                "domain": config("DOMAIN"),
                "project_name": config('PROJECT_NAME'),
            }
        )
        put(
            celery_beat_tmp_file_path,
            "/etc/supervisor/conf.d",
            use_sudo=True
        )

    sudo("sudo supervisorctl reread")
    sudo("sudo supervisorctl update")


def unfold_to_server():
    site_dir = f"/home/dev/sites/{config('DOMAIN')}"
    run(f"mkdir -p {join(site_dir, 'public', 'static')}")
    run(f"mkdir -p {join(site_dir, 'public', 'media')}")
    run(f"mkdir -p {join(site_dir, 'logs')}")
    sudo(f"sudo chmod -R 775 {join(site_dir, 'public')}")

    run(f"git clone git@github.com:pmaigutyak/{config('PROJECT_NAME')}.git {join(site_dir, config('PROJECT_NAME'))}")

    run(f"virtualenv {join(site_dir, 'env')} --python=/usr/bin/python3.8")
    run(f"ln -s {join(site_dir, 'env', 'bin', 'activate')} /home/dev/{config('PROJECT_NAME')}env")
    run(f"ln -s {join(site_dir, config('PROJECT_NAME'))} {config('PROJECT_NAME')}")

    upload_env()
    supervisor_conf()
    cert()
    nginx_conf()


def fetch_media():

    local_media_dir = join(env.project_dir, 'media')
    local('rm -r -f ' + local_media_dir)
    local('mkdir ' + local_media_dir)

    remote_media_dir = "/home/dev/sites/%s/public/media" % config('DOMAIN')
    exclude = ['cache']

    for dir_name in run('ls ' + remote_media_dir).split('  '):

        if dir_name in exclude:
            continue

        local('scp -r dev@{}:{} {}'.format(
            config('HOST'),
            join(remote_media_dir, dir_name),
            local_media_dir
        ))


def clean_thumbnail():
    with cd('~/sites/{}/{}/'.format(config('DOMAIN'), config('PROJECT_NAME'))):
        pull()

        with source():
            run('python manage.py thumbnail clear_delete_all')

    restart()
