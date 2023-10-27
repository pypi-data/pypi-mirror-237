from .restapi import LeostreamClient
from .webresource import WebResource

class LeostreamPoolAssignments(WebResource):
    
    def __init__(self, pool_id) -> None:
        self._api = LeostreamClient()
        self.resource = "pool-assignments"
        self._pool_id = pool_id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(self._pool_id)+ "/pool-assignments"
        self.data = self.get()
