from .storage import Storage
import os
from .utils import path_generator

class Minio(Storage):
    storage_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data, type=None, generated=None, regen=None) -> None:
        super().__init__(raw_data, type)
        self.storage_type = Minio.storage_type

        if generated and regen:
            self.path = self.raw_data['datasource']['prefixPath'] + path_generator()
        else:
            if self.raw_data['datasetFileType']['type'] == "table":
                self.path = self.raw_data['datasetFileType']['tableName'] 
            else:
                self.path = self.raw_data['datasetFileType']['path']


    def generate_properties(self):
        props = super().generate_properties()

        if not "secure" in self.raw_data['datasource'] or self.raw_data['datasource']['secure'] is None or self.raw_data['datasource']['secure'] == False:
            protocol = "http"
            use_ssl = "False"
        else:
            protocol = "https"
            use_ssl = "True"


        props += [(None, self.path)]
        props += [('path', self.path)]
        props += [('minIO_URL', protocol + '://' + self.raw_data['datasource']['host'] + ':' + str(self.raw_data['datasource']['port']))]
        props += [('minio_bucket', self.raw_data['datasource']['bucket'])]
        props += [('minIO_ACCESS_KEY', self.raw_data['datasource']['accessKey'])]
        props += [('minIO_SECRET_KEY', self.raw_data['datasource']['secretKey'])]
        props += [('use_ssl', use_ssl)]
        return props

    def get_path(self):
        return self.path
