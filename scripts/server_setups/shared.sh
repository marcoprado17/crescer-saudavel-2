#!/usr/bin/env bash

sudo apt-get update;
sudo apt-get install -y python-pip;
sudo apt-get install -y python-dev;
sudo apt-get install -y postgresql;
sudo apt-get install -y python-psycopg2;

sudo pip install --upgrade pip
sudo pip install -r /vagrant/requirements.txt;

python /vagrant/scripts/server_setups/export_db_info.py;

source /vagrant/scripts/server_setups/export_db_info_result.txt;

DB_USERNAME=${DB_USERNAME};
DB_PASSWORD=${DB_PASSWORD};
PRODUCTION_DB_NAME=${PRODUCTION_DB_NAME};

sudo runuser -l postgres -c "psql -c \"create user "${DB_USERNAME}" with password '"${DB_PASSWORD}"';\"";
sudo runuser -l postgres -c "psql -c \"create database "${PRODUCTION_DB_NAME}" owner "${DB_USERNAME}";\"";