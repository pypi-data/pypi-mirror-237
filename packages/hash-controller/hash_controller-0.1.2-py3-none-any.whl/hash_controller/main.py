import hashlib
import json
import os
import time
from pymongo import MongoClient


class HashClient:
    __db_user = os.environ["DB_USER"]
    __db_password = os.environ["DB_PASS"]
    __db_host = os.environ["DB_HOST"]
    __db_port = os.environ["DB_PORT"]
    __db_name = os.environ["DB_NAME"]
    __db_collection = os.environ["DB_COLLECTION"]

    __client = MongoClient(f"mongodb://{__db_host}:{__db_port}/")
    __database = __client[__db_name]
    __collection = __database[__db_collection]

    @staticmethod
    def exist_obj(customer_uuid: str, type: str, obj):
        if obj is None:
            raise TypeError(f"Obj of type None is not valid.")

        if customer_uuid and not str(customer_uuid):
            raise ValueError(f"customer_uuid not valid. Value: {customer_uuid}")

        if type and not str(type):
            raise ValueError(f"type not valid. Value: {type}")

        jsonObj = json.dumps(obj)
        hash = hashlib.md5(jsonObj.encode("utf-8")).hexdigest()
        id = f"{customer_uuid}/{type}/{hash}"
        item = HashClient.__collection.find_one(id)
        if item is None:
            return False
        else:
            return True

    @staticmethod
    def create_obj(customer_uuid: str, type: str, obj):
        if obj is None:
            raise TypeError(f"Obj of type None is not valid.")

        if customer_uuid and not str(customer_uuid):
            raise ValueError(f"customer_uuid not valid. Value: {customer_uuid}")

        if type and not str(type):
            raise ValueError(f"type not valid. Value: {type}")

        jsonObj = json.dumps(obj)
        hash = hashlib.md5(jsonObj.encode("utf-8")).hexdigest()
        id = f"{customer_uuid}/{type}/{hash}"
        document = {
            "_id": id,
            "customer_uuid": str(customer_uuid),
            "type": str(type),
            "obj": obj,
            "created_at": int(time.time()),
        }
        return HashClient.__collection.insert_one(document).inserted_id

    @staticmethod
    def get_objs(filter: dict = None, date_comparasion: str = "$gt"):
        if "created_at" in filter:
            filter["created_at"] = {date_comparasion: filter["created_at"]}
        items = HashClient.__collection.find(filter=filter)
        return list(items)
