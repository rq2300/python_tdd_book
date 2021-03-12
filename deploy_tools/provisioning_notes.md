Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.8
* pip3 and pipenv
* Git

e.g., on Ubuntu:

    sudo apt update
    sudo apt install nginx python38 python3-pip
    pip3 install pipenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    |   ├── .env
    |   ├── Pipfile
    |   ├── Pipfile.lock
    |   ├── db.sqlite3
    |   ├── manage.py etc
    |   └── static
    └── DOMAIN2
        ├── .env
        ├── Pipfile
        ├── Pipfile.lock
        ├── db.sqlite3
        ├── manage.py etc
        └── static
