#!/usr/bin/env bash

IDENTIFIER=""
VPS_PASSWORD=""
GITHUB_PASSWORD=""

while getopts 'i:v:g:' flag; do
  case "${flag}" in
    i) IDENTIFIER="${OPTARG}" ;;
    v) VPS_PASSWORD="${OPTARG}" ;;
    g) GITHUB_PASSWORD="${OPTARG}" ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

if [ -z $IDENTIFIER ]
    then
        echo "You need to provide the build identifier as argument using -i flag"
        exit 1
fi

if [ -z $VPS_PASSWORD ]
    then
        echo "You need to provide the vps password as argument using -v flag"
        exit 1
fi

if [ -z $GITHUB_PASSWORD ]
    then
        echo "You need to provide the github password as argument using -g flag"
        exit 1
fi

url_encode() {
  python -c 'import urllib, sys; print urllib.quote(sys.argv[1], sys.argv[2])' \
    "$1" "$urlencode_safe"
}

GITHUB_PASSWORD_ENCODED=$(url_encode "$GITHUB_PASSWORD")

cd ~/PycharmProjects/crescer-saudavel-2
gulp build
rm -rf ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER;
cp -R ~/PycharmProjects/crescer-saudavel-2 ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER;
cd ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER
git checkout -b build$IDENTIFIER
echo "

DEBUG = False
TEMPLATE_FOLDER = '/vagrant/build/templates'
ADMIN_MAIL = 'crescer.saudavel.suporte@gmail.com'
" >> ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER/configs/instance/instance_app_config.py
echo "
!build
!configs/instance/instance_app_config.py
!configs/instance/db_info.py
" >> ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER/.gitignore
rm -rf ~/PycharmProjects/crescer-saudavel-2-build$IDENTIFIER/src
git add .
git commit -m build$IDENTIFIER
git push origin build$IDENTIFIER

sshpass -p "$VPS_PASSWORD" ssh -o StrictHostKeyChecking=no root@vps0048.publiccloud.com.br "
pkill gunicorn;
sudo rm -rf /vagrant;
mkdir /vagrant;
cd /vagrant;
git clone -b build$IDENTIFIER https://marcoprado17:$GITHUB_PASSWORD_ENCODED@github.com/marcoprado17/crescer-saudavel-2.git .;
scripts/server_setups/production_server_setup.sh; python scripts/server_setups/restart_db.py;
python scripts/server_setups/fill_db.py;
scripts/start_server/start_production_server.sh"
