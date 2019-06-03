# -*- encoding:utf-8 -*-
from junyi.config import DEBUG_TOGGLE


def info(msg):
    print("[INFO] " + str(msg))


def debug(msg):
    if DEBUG_TOGGLE == True:
        print("[DEBUG] " + str(msg))


def error(msg):
    print("[ERROR] " + str(msg))
