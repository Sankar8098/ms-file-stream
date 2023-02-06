# This file is a part of ms-file-stream
# Coding : Mr Malik [@mrmalik_offl]

import sys
import re, os
from os import environ
from dotenv import load_dotenv

id_pattern = re.compile(r'^.\d+$')

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("23990433"))
    API_HASH = str(environ.get("e6c4b6ee1933711bc4da9d7d17e1eb20"))
    BOT_TOKEN = str(environ.get("6119758281:AAFNCl4gzd-1w957bRKEhjb6kW1JnaDZm3U"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL",'-1001682397310' )
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", '8080'))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "100.27.12.117"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    FQDN = str(environ.get("FQDN", '100.27.12.117:8080')
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "100.27.12.117:8080" if NO_PORT else ":" + str(PORT)
        )
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")
    FORCE_SUB = os.environ.get("FORCE_SUB", "SK_MoviesOffl")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5821871362').split()]
    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")
