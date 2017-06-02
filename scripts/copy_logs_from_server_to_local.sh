#!/usr/bin/env bash

if [ -z $1 ]
    then
        echo "You need to provide the vps password as argument"
        exit 1
fi

rm -rf ~/Downloads/logs
sshpass -p "$1" scp -o StrictHostKeyChecking=no -r root@vps0048.publiccloud.com.br:/vagrant/logs ~/Downloads
subl ~/Downloads/logs
