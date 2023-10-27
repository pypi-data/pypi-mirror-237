from .restapi import LeostreamClient
from .webresource import WebResource

class LeostreamCenters(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamClient()
        self.resource = "centers"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/centers?as+tree=0"
        self.data = self.list()
