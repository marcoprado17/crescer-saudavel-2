#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh;

chmod +x ${SHARED_SERVER_SETUP_FULL_PATH};
${SHARED_SERVER_SETUP_FULL_PATH};
chmod -x ${SHARED_SERVER_SETUP_FULL_PATH};

sudo mkdir /vagrant/configs/instance;
sudo touch /vagrant/configs/instance/instance_app_config.py;
sudo touch /vagrant/configs/instance/__init__.py;
echo "DEBUG=False" >> /vagrant/configs/instance/instance_app_config.py;
echo "STATIC_FOLDER='vagrant/build/static'" >> /vagrant/configs/instance/instance_app_config.py;

sudo apt-get install -y python nginx gunicorn;
sudo /etc/init.d/nginx start;
sudo rm /etc/nginx/sites-enabled/default;
sudo rm /etc/nginx/sites-available/build;
sudo rm /etc/nginx/sites-enabled/build;
sudo cp /vagrant/configs/ngix_config /etc/nginx/sites-available/build;
sudo ln -s /etc/nginx/sites-available/build /etc/nginx/sites-enabled/build;
sudo /etc/init.d/nginx restart;