'''
Created on Jul 11, 2019

@author: julien
'''

from http.server import HTTPServer

class StandaloneBoxServer(HTTPServer):
    '''
    Just a standalone box, without reference to other services
    '''

    def __init__(self, port, request_handler_class):
        '''
        Constructor
        '''
        super(StandaloneBoxServer, self).__init__(('', port), request_handler_class)
    