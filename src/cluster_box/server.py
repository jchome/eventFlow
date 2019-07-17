'''
Created on Jul 9, 2019

Usage:

    cluster = CluserBoxServer(8080)
    cluster.read_services("services.ini")
    cluster.serve_forever()


@author: julien
'''
from standalone_box.server import StandaloneBoxServer
from cluster_box.requesthandler import CluserRequestHandler
from urllib import request, parse
import configparser

class CluserBoxServer(StandaloneBoxServer):
    '''
    classdocs
    '''

    def __init__(self, port):
        '''
        Constructor
        '''
        super(CluserBoxServer, self).__init__(port, CluserRequestHandler)
        self.services = {}
        
    def read_services(self, config_file):
        '''
        Read services from a config file (.ini)
        '''
        config = configparser.ConfigParser()
        config.read(config_file)
        for service_name in config['DEFAULT']:
            self.add_service(service_name, config['DEFAULT'][service_name])
        return self.services
    
    def add_service(self, name, url):
        '''
        Add a service into the service list
        '''
        if self.services.get(name) is None:
            self.services[name] = []
        self.services[name].append(url)
        return self.services
    
    def call_service(self, service_name, data):
        # If failed, try another url of the service
        url = self.get_service(service_name)
        data_encoded = parse.urlencode(data).encode()
        # Call as POST method
        req = request.Request(url, data=data_encoded)
        response = request.urlopen(req)
        return response
    
    def get_service(self, service_name, index=0):
        service_data = self.services.get(service_name)
        if service_data is not None:
            return service_data[index]
        else:
            return None
        

if __name__ == '__main__':
    cluster = CluserBoxServer(8080)
    cluster.read_services("services.ini")
    cluster.serve_forever()

        