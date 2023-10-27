import os
from .storage import Storage
from .asset import Asset

class Dataset(Asset):
    asset_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data=None, name=None):

        self.id = str(raw_data['id'])

        self.properties = []
        
        if name is None:
            self.name = self.id
        
        self.storage = Storage(raw_data=raw_data)

    def generate_properties(self):
        self.properties = self.storage.generate_properties()
        return self.properties
    
    