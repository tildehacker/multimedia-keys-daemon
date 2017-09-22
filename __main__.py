#!/usr/bin/env python3
# *-* encoding: utf-8 *-*

import os
import daemon

from daemons import run

# Should run this program as root
if os.getuid() != 0:
    raise PermissionError("Run as root.")

log = open("mkd.log", "w+")

with daemon.DaemonContext(stdout=log, stderr=log):
    run()
