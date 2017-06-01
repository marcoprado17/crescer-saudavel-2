#!/usr/bin/env bash
if [ -z $1 ]
    then
        echo "Pass the build identifier as argument"
        exit 1
fi
rm -rf ~/PycharmProjects/crescer-saudavel-2-build$1;
cp -R ~/PycharmProjects/crescer-saudavel-2 ~/PycharmProjects/crescer-saudavel-2-build$1;
cd ~/PycharmProjects/crescer-saudavel-2-build$1
git checkout -b build$1
echo "

DEBUG = False
TEMPLATE_FOLDER = '/vagrant/build/templates'
ADMIN_MAIL = 'crescer.saudavel.suporte@gmail.com'
" >> ~/PycharmProjects/crescer-saudavel-2-build$1/configs/instance/instance_app_config.py
echo "
!build
!configs/instance/instance_app_config.py
!configs/instance/db_info.py
" >> ~/PycharmProjects/crescer-saudavel-2-build$1/.gitignore
git add .
git commit -m build$1
git push origin build$1

ssh root@vps0048.publiccloud.com.br pkill gunicorn
ssh root@vps0048.publiccloud.com.br sudo rm -rf /vagrant
ssh root@vps0048.publiccloud.com.br mkdir /vagrant
ssh root@vps0048.publiccloud.com.br cd /vagrant
ssh root@vps0048.publiccloud.com.br git clone -b build$1 https://github.com/marcoprado17/crescer-saudavel-2.git .
ssh root@vps0048.publiccloud.com.br scripts/server_setups/production_server_setup.sh
ssh root@vps0048.publiccloud.com.br python scripts/server_setups/restart_db.py
ssh root@vps0048.publiccloud.com.br python scripts/server_setups/fill_db.py
ssh root@vps0048.publiccloud.com.br scripts/start_server/start_production_server.sh
