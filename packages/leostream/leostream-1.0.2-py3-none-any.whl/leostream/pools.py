from .restapi import LeostreamClient
from .webresource import WebResource

class LeostreamPools(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamClient()
        self.resource = "pools"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/pools?as+tree=0"
        self.data = self.list()
