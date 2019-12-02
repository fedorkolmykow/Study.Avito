#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class HttpProcessor(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.wfile.write(b"Hello! Try put next URL http://localhost:8010/discounts")

def run(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('localhost', 8010)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()    		

