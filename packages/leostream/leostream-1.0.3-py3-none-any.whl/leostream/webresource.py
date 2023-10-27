# pylint: disable=E1101
import requests
import json
import os

class WebResource(object):
    ''' This class is the base class for all Leostream resources found in the API. It contains the common functions
        for all resources. 
        General design ideas:
        1. The resource class will have a data attribute that contains the data from the API
        2. The resource class will have a resource attribute that contains the name of the resource
        3. The resource class will have a _URL attribute that contains the URL for the resource
        4. The resource class will have a _HEADERS attribute that contains the headers for the resource
        5. The resource class will have a _api attribute that contains the LeostreamSession object
        6. The resource class will have a get() function that will return the data from the API
        7. The resource class will have a update() function that will update the resource via the API

        Rationale for design:
        - Create classes for Leostream entities like Pools, Centers, Gateways etc.
        - Group common classes in a Package
        - Each class is responsible for it's own data
        - Create inheritance relation or interface like construction to avoid duplication (login to Leostream/ API get,update)
        '''
    

    def update(self , data):
        ''' 
        This method will update the resource via the API. It will return the response from the API'''

        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api._session}

        response = requests.put(url=self._URL, headers=self._HEADERS, verify=False, data=json.dumps(data))
        data = response.json()

        # check https status code
        if response.status_code != 200:
            raise Exception("Error: the login request returned HTTP status code " + str(response.status_code) + " with the following message: " + str(data))

        return data

    def list(self):
        '''
        This method will return a list of all resources of the type specified in the url attribute'''

        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api._session}

        response = requests.get(url=self._URL, headers=self._HEADERS, verify=False)
        data = response.json()

        # check https status code
        if response.status_code != 200:
            raise Exception("Error: the login request returned HTTP status code " + str(response.status_code) + " with the following message: " + str(data))

        return data
    
    def get(self):
        '''
        This method will return the data for the resource specified in the url attribute'''

        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api._session}

        response = requests.get(url=self._URL, headers=self._HEADERS, verify=False)
        data = response.json()

        # check https status code
        if response.status_code != 200:
            raise Exception("Error: the login request returned HTTP status code " + str(response.status_code) + " with the following message: " + str(data))

        return data

    def writefile(self, data):
        '''
        This method will write the data from the API to a file in JSON format. It will create a directory for the resource if it does not exist.
        The file name will be the resource id. It can be used to create a backup of the resource configuration.'''
        
        # Save the response to a file
        jsondir= os.getenv("LEOSTREAM_API_JSONDIR", ".")
              
        # If the resource has an id and a pool_id, this is a pool assignment
        if hasattr(self, '_id') and hasattr(self, '_pool_id') :
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource)  

            if not os.path.exists(jsondir + '/'+ self.resource  + '/' + str(self._pool_id)):
                os.makedirs(jsondir + '/'+ self.resource + '/' + str(self._pool_id))  
            
            filename = jsondir + '/' + self.resource + '/' + str(self._pool_id) + '/' + str(self._id) + '.json'

        # If the resource has an id and no pool_id, this is not a pool assignment
        elif hasattr(self, '_id') and not hasattr(self, '_pool_id'):
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource) 
            filename = jsondir + '/' + self.resource + '/' + str(self._id) + '.json'

        # If the resource has a pool_id and no id, this is a pool
        elif hasattr(self, '_pool_id') and not hasattr(self, '_id'):
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource) 
            filename = jsondir + '/' + self.resource + '/' + str(self._pool_id) + '.json'

        # If the resource has no id and no pool_id, this is a resource list (centers, gateways, pools, etc)
        else:    
            filename = jsondir + '/' + self.resource + '.json'

        with open(filename, 'w') as f:
            json.dump(data, f, indent=1)
