'''
Created on Jul 17, 2019

@author: julien
'''

from standalone_box.requesthandler import StandaloneRequestHandler

class GetWrapperRequestHandler(StandaloneRequestHandler):
    '''
    Handler that provides data
    '''
    
    def do_GET(self):
        '''
        Provide the GET interface
        '''
        query_components = self.parse_GET()
        try:
            result = self.server.get_data(query_components)
            return self.send_json_object(result)
        except Exception as e:
            return self.send_json_error("{'error': 'Error during query execution : %s'}" % str(e), 500)
       

    
    def do_POST(self):
        '''
        Provide the POST interface
        '''
        query_components = self.parse_POST()
        try:
            result = self.server.get_data(query_components)
            return self.send_json_object(result)
        except Exception as e:
            return self.send_json_error("{'error': 'Error during query execution : %s'}" % str(e), 500)
       