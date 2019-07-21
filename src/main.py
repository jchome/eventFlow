#!/usr/bin/env python3
'''
Created on Jul 9, 2019

@author: julien
'''

import threading
from cluster_box.server import CluserBoxServer
from weather_box.server import WeatherBoxServer

class ThreadBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        
    def run(self):
        httpd = CluserBoxServer(8080)
        httpd.read_services("services.ini")
        httpd.serve_forever()

def start_weather_box():
    '''
    Start the WeatherBoxServer and wait for queries
    '''
    box = WeatherBoxServer(8081)
    box.serve_forever()

def start_cluster_box():
    '''
    Start the CluserBoxServer in a thread
    '''
    thread1 = ThreadBox()
    thread1.start()
    print("ready")
    thread1.join()
    print("End.")
    
if __name__ == '__main__':
    #start_weather_box()
    
    httpd = CluserBoxServer(8080)
    httpd.read_services("services.ini")
    print(httpd.call_service("weatherdata", {"city": "Cannes,FR"}))
    
            