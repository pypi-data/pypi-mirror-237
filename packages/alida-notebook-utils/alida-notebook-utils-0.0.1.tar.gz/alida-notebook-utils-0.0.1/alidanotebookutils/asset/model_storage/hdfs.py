import os
from .generic_storage import GenericStorage
import string
import random

def path_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return "m" + ''.join(random.choice(chars) for _ in range(size))


class Hdfs(GenericStorage):
    storage_type = os.path.basename(__file__).split('.py')[0]

    def __init__(self, raw_data, type, generated, regen=None):
        super().__init__(raw_data=raw_data, type=type)
        self.storage_type = Hdfs.storage_type

        if generated and regen:
            self.path = "/tmp/" + path_generator()
        else:
            self.path = raw_data['location']


    def generate_properties(self):
        props = super().generate_properties()

        props += [('webHdfsUrl', "http://" + self.raw_data['datasource']['host'] + ":" + "50070")]
        props += [('hdfsUrl', "http://" + self.raw_data['datasource']['host'] + ":" + str(self.raw_data['datasource']['port']))]
        props += [(None, self.path)]

        return props

    def get_path(self):
        return self.path

