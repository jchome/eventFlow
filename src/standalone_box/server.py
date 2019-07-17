'''
Created on Jul 11, 2019

@author: julien
'''

from http.server import HTTPServer
import json

class StandaloneBoxServer(HTTPServer):
    '''
    Just a standalone box, without reference to other services
    '''

    def __init__(self, port, request_handler_class):
        '''
        Constructor
        '''
        super(StandaloneBoxServer, self).__init__(('', port), request_handler_class)
        
    def send_json_message(self, request_hanlder, message, http_status):
        request_hanlder.send_response(http_status)
        request_hanlder.send_header('Content-type','text/json')
        request_hanlder.end_headers()
        request_hanlder.wfile.write(bytes(str(message), "utf8"))
        return
    
    def send_json_object(self, request_hanlder, data):
        string_data = json.dumps(data)
        self.send_json_message(request_hanlder, string_data, 200)
        return
    