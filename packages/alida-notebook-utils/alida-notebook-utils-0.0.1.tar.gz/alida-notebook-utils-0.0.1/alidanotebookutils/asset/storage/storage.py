from abc import abstractclassmethod

class Storage:
    def __init__(self, raw_data=None, type=None, generated=None, regen=None):
        self.type = type
        self.raw_data = raw_data

    def __new__(cls, *args, **kw):
        
        # Get storage type from properties 
        if 'raw_data' in kw:
            storage_type = kw['raw_data']['datasource']['driverType']
        elif len(args)>0:
            storage_type = args[0]['datasource']['driverType']
        else:
            raise Exception("Error, no storage info found! Cannot parse...")
        
        # Create a map of all subclasses based on storage type property (present on each subclass)
        subclass_map = {subclass.storage_type: subclass for subclass in cls.__subclasses__()}
   
        # Select the proper subclass based on
        subclass = subclass_map[storage_type.lower()]
        instance = super(Storage, subclass).__new__(subclass)
        return instance

    @abstractclassmethod
    def generate_properties(self):
        return [('storage_type', self.storage_type)]

    @abstractclassmethod
    def get_path(self):
        pass
