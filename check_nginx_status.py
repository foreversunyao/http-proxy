#!/usr/bin/python
# coding=utf-8
#
# Check Nginx status and configuration
# By Samuel
# 10/09/2017
#
import sys
import httplib, subprocess

if __name__ == '__main__':
    FATAL = 2
    SUCCESS = 0
    total = len(sys.argv)
    exit_code=FATAL
    if total != 2:
        print("Usage: python xxx ipaddress")
        sys.exit(exit_code)
    host=str(sys.argv[1])
    c = httplib.HTTPConnection(host,50000)
    c.request('GET', '/', '{}')
    exit_code = c.getresponse().read()
    if int(exit_code) == SUCCESS:
        print "Nginx is OK"
    else:
        print "Nginx has issue"
    sys.exit(int(exit_code))
