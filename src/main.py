#!/usr/bin/env python3
'''
Created on Jul 9, 2019

@author: julien
'''

import threading
from cluster_box.server import CluserBoxServer

if __name__ == '__main__':
    '''
    cluster = CluserBoxServer(8080)
    cluster.read_services("services.ini")
    cluster.serve_forever()
    cluster_thread = Thread(target=cluster.serve_forever, name="cluster_thread", args=(), daemon=True)
    cluster_thread.start()
    print("ready")
    '''
    class ThreadBox(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.daemon = True
            
        def run(self):
            httpd = CluserBoxServer(8080)
            httpd.read_services("services.ini")
            httpd.serve_forever()
    
    thread1 = ThreadBox()
    thread1.start()
    print("ready")
    thread1.join()
    print("End.")
            