from fileioutilities import FileIO
from .asset import Asset


def download_file(raw_data, local_path="./file"):
    asset = Asset(raw_data=raw_data)
    asset.set_properties_as_env()
    
    file_io = FileIO(name=str(asset.id))
    file_io.download(local_path=local_path)
    return local_path


def download_model(raw_data, local_path="./model"):
    return download_file(raw_data=raw_data, local_path=local_path)
