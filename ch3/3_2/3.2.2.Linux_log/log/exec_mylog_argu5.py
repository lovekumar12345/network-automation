#!/bin/env python
#-*- coding: utf-8 -*-

import mylog_1
import os

logfile = "/var/log/messages"
file_length = os.path.getsize(logfile)

mylog_1.printlog("/var/log/messages", "fail", int(file_length/2), 3, 5)
