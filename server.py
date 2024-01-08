#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@File    :   server.py
@Time    :   2023/12/29 20:24:41
@Author  :   Fisher Yu
@Version :   1.0
@Contact :   plmkop@gmail.com
@License :   © Copyright 2023-2033, idoobi.top
@Desc    :   None
'''

import os
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer

from crontab import CronTab


def init_crontab():
    cron = CronTab("root")
    cron.remove_all()
    job = cron.new(command="certbot renew")
    job.minute.on(0)
    job.hour.on(0)
    job.month.every(2)
    cron.write()


class CertbotServer(BaseHTTPRequestHandler):

    def do_GET(self):
        sys.stdout.write(f"Client from {self.client_address[0]}:{self.client_address[1]} requesting:\t {self.path}")
        path = self.path.lstrip('/')
        file = os.path.join(webroot, path)
        
        if not path or not os.path.exists(file):
            sys.stdout.write("\t404\n")
            self.send_response(404)
            return
        
        if not os.access(file, os.R_OK):
            sys.stdout.write("\t403\n")
            self.send_response(403)
            return
        
        self.send_response(200)
        self.end_headers()

        with open(file, 'rb') as resp: 
            self.wfile.write(resp.read()) 


init_crontab()
webroot = "/srv/www"
os.makedirs(webroot, exist_ok=True)


try:
    sys.stdout.write("Starting server on port 80\n")
    httpd = HTTPServer(('0.0.0.0', 80), CertbotServer)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Ctrl+C Received, Stopping......")


