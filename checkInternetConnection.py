# This snippet is for checking internet connection for your python program
# urllib based methods are requelting in no connection error and seems to be outdated
# Below are two methods to test active internet connection.
# Last updated: 25th Feb 2021

import requests
import time

#Best working code for me is sokcet program 
def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

# Requests method opens up a new http connection for each request resulting in error after some time
def is_connected():
    try:
        #requests.get('https://www.google.com/')
        requests.head('https://www.google.com/')
        print('connected')
        return True
    except OSError:
        print('can not reach the URL')
        pass
    return False

while True:
    is_connected()
    time.sleep(5)
