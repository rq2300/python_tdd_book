import random

from fabric.contrib.files import append
from fabric.contrib.files import exists
from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import run


REPO_URL = "https://github.com/rq2300/python_tdd_book.git"

def deploy():
    site_folder = f"/home/{env.user}/sites/{env.host}"
    run(f"mkdir -p {site_folder}")
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()


def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")


def _update_virtualenv():
    run("pipenv install")


def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", f"SITENAME={env.host}")
    current_content = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_content:
        new_secret = "".join(random.SystemRandom().choices("abcdefghijklmnopqrstuvwxyz0123456789", k=50))
        append(".env", f"DJANGO_SECRET_KEY={new_secret}")


def _update_static_files():
    run(f"/home/{env.user}/.local/share/virtualenvs/{env.host}-*/bin/python manage.py collectstatic --noinput")


def _update_database():
    run(f"/home/{env.user}/.local/share/virtualenvs/{env.host}-*/bin/python manage.py migrate --noinput")