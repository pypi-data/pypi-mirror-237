import os

class Asset:
    def __new__(cls, *args, **kw):
        
        if "datasetFileType" in kw['raw_data']:
            asset_type="dataset"
        else:
            asset_type="model"

        # Create a map of all subclasses based on storage type property (present on each subclass)
        subclass_map = {subclass.asset_type: subclass for subclass in cls.__subclasses__()}
   
        # Select the proper subclass based on
        subclass = subclass_map[asset_type.lower()]
        instance = super(Asset, subclass).__new__(subclass)
        return instance

    def __init__(self) -> None:
        pass
    
    def properties_as_dict(self):
        tmp = {}
        self.generate_properties()
        for prop in self.properties:
            if prop[0] is not None:
                tmp[prop[0]]=prop[1]
        return tmp
    
    def properties_to_env(self):
        envs = []
        self.generate_properties()
        for prop in self.properties:
            if prop[0] is None:
                envs.append(((self.name), prop[1]))  #envs.append(((self.name).upper(), prop[1]))
            else:
                envs.append(((self.name + "." + prop[0]), prop[1])) #envs.append(((self.name + "." + prop[0]).upper(), prop[1]))
        return envs

    def set_properties_as_env(self):
        envs = self.properties_to_env()
        for env in envs:
            os.environ[env[0]] = env[1]
        return envs
    
