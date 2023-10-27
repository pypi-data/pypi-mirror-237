from sys import path
from .storage import Storage
import os
from .utils import path_generator

class Hive(Storage):
    storage_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data, type=None, generated=None, regen=None) -> None:
        super().__init__(raw_data, type)
        self.storage_type = Hive.storage_type
        self.generated = generated
        if generated and regen:
            self.path = self.raw_data['datasource']['database'] + "." + path_generator()
        else:
            self.path = self.raw_data['datasource']['database'] + "." + self.raw_data['datasetFileType']['tableName']

    def generate_properties(self):

        props = super().generate_properties()
        props += [(None, self.path)]
        props += [('hiveUserName', self.raw_data['datasource']['user'])]
        props += [('hivePassword', self.raw_data['datasource']['password'])]
        props += [('hiveMetastoreUris', self.raw_data['datasource']['protocol'] + self.raw_data['datasource']['host'] + ":" + str(self.raw_data['datasource']['port']))]
    
        for element in self.raw_data['datasource']['other']:
            if element['key'] == "hiveHadoopUserName":
                props += [('hiveHadoopUserName', element['value'])]
    
        return props

    def get_path(self):
        return self.path
