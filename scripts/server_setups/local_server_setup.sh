#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh;
SET_TIMEZONE_FULL_PATH=/vagrant/scripts/server_setups/set_timezone.sh;

chmod +x ${SHARED_SERVER_SETUP_FULL_PATH};
${SHARED_SERVER_SETUP_FULL_PATH};
chmod -x ${SHARED_SERVER_SETUP_FULL_PATH};

DB_USERNAME=${DB_USERNAME};
TEST_DB_NAME=${TEST_DB_NAME};

source /vagrant/scripts/server_setups/export_db_info_result.txt;

sudo runuser -l postgres -c "psql -c \"create database "${TEST_DB_NAME}" owner "${DB_USERNAME}";\"";

chmod +x ${SET_TIMEZONE_FULL_PATH};
${SET_TIMEZONE_FULL_PATH};
chmod -x ${SET_TIMEZONE_FULL_PATH};