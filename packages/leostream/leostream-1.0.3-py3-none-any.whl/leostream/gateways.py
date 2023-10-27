from .restapi import LeostreamClient
from .webresource import WebResource

class LeostreamGateways(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamClient()
        self.resource = "gateways"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/gateways?as+tree=0"
        self.data = self.list()
