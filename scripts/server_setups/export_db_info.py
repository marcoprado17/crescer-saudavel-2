# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================

import sys
sys.path.insert(0, "/vagrant")
from configs.instance.db_info import DB_USERNAME, DB_PASSWORD, TEST_DB_NAME, PRODUCTION_DB_NAME

text_file = open("scripts/server_setups/export_db_info_result.txt", "w")
text_file.writelines([
    "DB_USERNAME='%s'\n" % DB_USERNAME,
    "DB_PASSWORD='%s'\n" % DB_PASSWORD,
    "TEST_DB_NAME='%s'\n" % TEST_DB_NAME,
    "PRODUCTION_DB_NAME='%s'\n" % PRODUCTION_DB_NAME])
text_file.close()
