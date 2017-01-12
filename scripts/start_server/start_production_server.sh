#!/usr/bin/env bash

cd /vagrant;
gunicorn build.app_contexts.app:app -b localhost:8000;