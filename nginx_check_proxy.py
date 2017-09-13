#!/usr/bin/python
import subprocess
import os
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler 

class HTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		errorcode = {'error':2,'success':0}
		buf=errorcode['error']
		## check nginx configuration
		config_output=subprocess.call(["/etc/init.d/nginx configtest"], shell=True)
		## check nginx status
		status_process=subprocess.Popen("ps -ef|grep 'nginx: master process'|grep -v grep|wc -l",shell=True, stdout=subprocess.PIPE)
		status_output=status_process.stdout.read()
		if (config_output==0) and (int(status_output)==1):
			buf= errorcode['success']
		else:
			buf= errorcode['error']
		self.protocal_version = "HTTP/1.1"
        	self.send_response(200)  
        	self.send_header("Welcome","Contect") 
        	self.end_headers()  
		self.wfile.write(buf)
http_server = HTTPServer(('0.0.0.0',50000),HTTPHandler) 
http_server.serve_forever()

