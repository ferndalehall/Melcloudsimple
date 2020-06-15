'''
Created on 25 Apr 2020

@author: jpickford
'''
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
import json


URL_LOGIN        = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Login/ClientLogin"
URL_LIST_DEVICES = "https://app.melcloud.com/Mitsubishi.Wifi.Client/User/ListDevices"

class Melcloudsimple(object):
    '''
    A simple class to access a Mitsubishi Air Source Heat Pump through the MELCloud
    WiFi interface.

    __init__(key, email, password, verbose)
    
    Args:
        key        pre-existing key
        email      email address for logging in
        password   password
        verbose    True or False
        
    getAllValues()
    
    Args:
        None
    
    Return:
        dict{}      A dictionary containing the data returned by the listdevices URL
        '''
    def __init__(self, key,email, password, verbose):

        self.key = key
        self.email = email
        self.password = password
        self.verbose = verbose
        self.data = None
           
        # To set max_retries       
        self.mel_adapter = HTTPAdapter(max_retries=3)
        self.session = Session()
        self.session.mount('https://app.melcloud.com', self.mel_adapter)
        
        if self.key == None and ( self.email is not None and self.password is not None):
            response = self.session.post(
                URL_LOGIN, data={
                "AppVersion": "1.9.3.0",
                "CaptchaChallenge": "",
                "CaptchaResponse": "",
                "Email": self.email,
                "Password": self.password,
                "Language": 0,
                "Persist": "true"
            }
            )
            
            self.key = response.json()['LoginData']['ContextKey']
            
        if self.verbose:
            print("self.verbose = ", self.verbose)
            print("self.key = ", self.key)
            print("self.email = ", self.email)
            print("self.password = ", self.password)
    
    def getAllValues(self):
        header={
            'Host': 'app.melcloud.com',
            #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': 'application/json; q=0.01',
            'Accept-Language': 'en-GB,en;q=0.5',
            #'Accept-Encoding': 'gzip, deflate, br',
            'X-MitsContextKey': self.key,
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://app.melcloud.com/',
            #'Cookie': 'policyaccepted=true'
        }
        try:
            response = self.session.get(URL_LIST_DEVICES, headers=header,timeout=10)
        except ConnectionError as ce:
            print(ce)
        except Exception as e:
            print("Exception:", e)

        # Convert the returned string to JSON and save
        my_json = response.content.decode('utf8')
        self.data = json.loads(my_json[1:-1])
        
        if self.verbose:
            for k in self.data:
                print(k, self.data[k])
        
            info = self.data['Structure']['Devices'][0]['Device']
            print("Device info:")
            for i in info:
                print(i, info[i])
        return self.data
