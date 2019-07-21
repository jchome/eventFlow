'''
Created on Jul 17, 2019

@author: julien
'''
from standalone_box.server import StandaloneBoxServer
from get_wrapper_box.requesthandler import GetWrapperRequestHandler
import requests

class GetWrapperBoxServer(StandaloneBoxServer):
    '''
    Simply wrap the do_get and call the HTTP GET request
    '''


    def __init__(self, port, request_handler_class=GetWrapperRequestHandler):
        '''
        Constructor
        The default request handler is GetWrapperRequestHandler
        '''
        super(GetWrapperBoxServer, self).__init__(port, request_handler_class)
        
        
    def check_inputs(self, query_components):
        '''
        To override.
        Check that input data are correct.
        '''
        return True
    
    def define_url(self, query_components):
        '''
        To override.
        Return the URL to call.
        '''
        return "http://localhost/"
    
    def get_data(self, query_components):
        '''
        Override this method and return a DICT object.
        Call the HTTP GET request
        '''
        if not self.check_inputs(query_components):
            return "GetWrapperBoxServer: invalid inputs"
        url = self.define_url(query_components)
        
        r = requests.get(url)
        return r.json()
    