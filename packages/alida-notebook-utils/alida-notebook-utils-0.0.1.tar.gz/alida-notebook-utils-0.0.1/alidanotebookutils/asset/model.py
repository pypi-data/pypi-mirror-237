import os
from .model_storage.generic_storage import GenericStorage
from .asset import Asset

class Model(Asset):
    asset_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data, name=None):
        
        self.id = str(raw_data['id'])
        
        self.properties = []

        if name is None:
            self.name = self.id
        
        self.storage = GenericStorage(raw_data)

    def generate_properties(self):
        self.properties = self.storage.generate_properties()
        return self.properties

