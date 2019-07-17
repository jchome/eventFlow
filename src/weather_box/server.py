'''
Created on Jul 17, 2019

box = WeatherBoxServer(8080)
box.serve_forever()

@author: julien
'''
from get_wrapper_box.server import GetWrapperBoxServer

class WeatherBoxServer(GetWrapperBoxServer):
    '''
    Just a standalone box, without reference to other services
    '''

    def __init__(self, port):
        '''
        Constructor
        '''
        super(WeatherBoxServer, self).__init__(port)
        self.AKI_KEY = "7611e996fadc01dd0dc8f6519816ddcf"
        self.keyForCity = "city"
    
    def check_inputs(self, query_components):
        city = query_components.get(self.keyForCity)
        if city is None:
            return False
        if len(city.split(",")) != 2:
            return False
        return True
    
    def define_url(self, query_components):
        city = query_components.get(self.keyForCity)
        url = "http://api.openweathermap.org/data/2.5/weather?q=%(city)s&APPID=%(api_key)s" % {
            'api_key': self.AKI_KEY,
            'city': city}
        return url
        
    
    