from .restapi import LeostreamClient
from .webresource import WebResource

class LeostreamPoolAssignment(WebResource):
    
    def __init__(self, pool_id, id) -> None:
        self._api = LeostreamClient()
        self.resource = "pool-assignments"
        self._id = id
        self._pool_id = pool_id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(self._id)+ "/pool-assignments/" + str(self._pool_id)
        self.data = self.get()
