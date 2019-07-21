'''
Created on Jul 11, 2019

@author: julien
'''

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cgi import parse_header, parse_multipart

class StandaloneRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        message = {"result": "ok"}
        return self.send_json_message(message)
    
    def do_POST(self):
        message = {"result": "ok"}
        return self.send_json_message(message)
    
    def send_json_message(self, message):
        self.server.send_json_message(self, message, 200)
        
    def send_json_error(self, message, error_code):
        self.server.send_json_message(self, message, error_code)
        
    def send_json_object(self, data):
        self.server.send_json_object(self, data)
    
    def parse_GET(self):
        query = urlparse(self.path).query
        return parse_qs(query)
    
    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            data = self.rfile.read(length).decode('latin1')
            postvars = parse_qs(
                    data, 
                    keep_blank_values=1)
        else:
            postvars = {}
        return postvars
    