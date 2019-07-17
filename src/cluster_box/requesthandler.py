'''
Created on Jul 9, 2019

@author: julien
'''
from standalone_box.requesthandler import StandaloneRequestHandler

class CluserRequestHandler(StandaloneRequestHandler):
    
    def do_GET(self):
        '''
        Answer to GET methods
        '''
        if self.path == "/":
            # Call the super "/"
            return super(CluserRequestHandler, self).do_GET()
        elif self.path == "/services":
            return self.get_services()
        elif self.path.startswith("/service/"):
            service_name = self.path[len("/service/"):]
            return self.get_service(service_name)
        else:
            self.send_json_error("Failed", 500)
    
    def do_POST(self):
            message = {"message": "not yet implemented", "success": False}
            self.send_json_error(message, 500)
    
    def get_services(self):
        self.send_json_message(self.server.services)

    def get_service(self, service_name):
        data = self.server.get_service(service_name)
        if data is None:
            message = {"message": "Service not found", "success": False}
            self.send_json_error(message, 500)
        else:
            self.send_json_message(data)
            

        