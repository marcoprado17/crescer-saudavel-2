#!/usr/bin/env bash

cd /vagrant;
gunicorn build.app:app -b localhost:8000;