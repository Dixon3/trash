#!/usr/bin/env python
import os
import sys


sys.path.append('./lib') # Add modules in lib

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyzakupki.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
