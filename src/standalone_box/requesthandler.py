'''
Created on Jul 11, 2019

@author: julien
'''

from http.server import BaseHTTPRequestHandler

class StandaloneRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        message = {"result": "ok"}
        return self.send_json_message(message)
    
    def send_json_message(self, message):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        self.wfile.write(bytes(str(message), "utf8"))
        return
        
    def send_json_error(self, message, error_code):
        self.send_response(error_code)
        self.send_header('Content-type','text/json')
        self.end_headers()
        self.wfile.write(bytes(str(message), "utf8"))
        return
    