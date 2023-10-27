import json
from storage import Storage
from .minio import Minio
from .hive import Hive


with open("storage/input.json", 'r', encoding='utf-8') as f:
    data = json.load(f)


storage = Storage(data)


print(storage.generate_properties())