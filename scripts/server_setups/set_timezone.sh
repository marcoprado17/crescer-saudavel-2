#!/usr/bin/env bash

TIMEZONE=America/Sao_Paulo

sudo timedatectl set-timezone ${TIMEZONE}
export TZ=${TIMEZONE}