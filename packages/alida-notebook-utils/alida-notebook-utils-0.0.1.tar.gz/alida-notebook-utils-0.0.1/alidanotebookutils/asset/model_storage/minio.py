import os
from .generic_storage import GenericStorage
import random
import string


def path_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return "m" + ''.join(random.choice(chars) for _ in range(size))


class Minio(GenericStorage):
    storage_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data, type=None, generated=None, regen=None) -> None:
        super().__init__(raw_data=raw_data, type=type)

        self.storage_type = Minio.storage_type

        if generated and regen:
            self.path = self.raw_data['datasource']['prefixPath'] + path_generator()
        else:
            self.path = self.raw_data['location']


    def generate_properties(self):
        
        if not "secure" in self.raw_data['datasource'] or self.raw_data['datasource']['secure'] is None or self.raw_data['datasource']['secure'] == False:
            protocol = "http"
            use_ssl = "False"
        else:
            protocol = "https"
            use_ssl = "True"

        props = super().generate_properties()
        props += [(None, self.path)]
        props += [('minIO_URL', protocol + '://' + self.raw_data['datasource']['host'] + ':' + str(self.raw_data['datasource']['port']))]
        props += [('minio_bucket', self.raw_data['datasource']['bucket'])]
        props += [('minIO_ACCESS_KEY', self.raw_data['datasource']['accessKey'])]
        props += [('minIO_SECRET_KEY', self.raw_data['datasource']['secretKey'])]
        props += [('use_ssl', use_ssl)]
        return props

    def get_path(self):
        return self.path
