# crescer-saudavel-2

## Instruções de deploy

1. Dar um gulp build, reiniciar e redimensionar as imagens
2. 
```
cp -R ~/PycharmProjects/crescer-saudavel-2 ~/PycharmProjects/crescer-saudavel-2-build{N}
cd ~/PycharmProjects/crescer-saudavel-2-build{N}
git status
git checkout -b build{N}
subl .
```
3. Em configs/instance/instace_app_config.py:
```
DEBUG = False
TEMPLATE_FOLDER = "/vagrant/build/templates"
ADMIN_MAIL = "crescer.saudavel.suporte@gmail.com"
```
4. Em .gitignore, remover as seguintes linhas:
```
build
scripts/server_setups/export_db_info_result.txt
/configs/instance/instance_app_config.py
/configs/instance/db_info.py
```
5. 

```
git status
git add .
git commit -m "build{N}"
git push origin build{N}
```
. 
6
```
ssh root@vps0048.publiccloud.com.br
pkill gunicorn
sudo rm -rf /vagrant
mkdir /vagrant
cd /vagrant
git clone -b build{N} https://github.com/marcoprado17/crescer-saudavel-2.git .
ls
```
7. 

```
scripts/server_setups/production_server_setup.sh
python scripts/server_setups/restart_db.py
python scripts/server_setups/fill_db_with_random_data.py
scripts/start_server/start_production_server.sh
```