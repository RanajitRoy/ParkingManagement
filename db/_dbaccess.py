from pymongo import MongoClient
from uuid import uuid4
from bson import Binary

class _DBAccessObj:
    def __init__(self, host="localhost", port=27017, db="parking-management"):
        self.client = MongoClient(f"mongodb://{host}:{port}")
        self.db = self.client[db]
        self.registered_users = self.db["reg_users"]
        print("Done Connecting")
    
    
    def register_user(self, username, plate_no, id=None):
        if id is None:
            id = uuid4()
        res = self.registered_users.insert_one({
            "_id" : Binary.from_uuid(id),
            "user": username,
            "lp" : plate_no
        })
        if res.inserted_id:
            return True
        else:
            return False

    def unregister_user(self, username, plate_no, id=None):
        find_dict = {
            "user": username,
            "lp" : plate_no
        }
        if id is not None:
            find_dict['_id'] = Binary.from_uuid(id)
        res = self.registered_users.delete_many(find_dict)
        return res.deleted_count


    def is_registered(self, username, plate_no):
        found = self.registered_users.find_one({
            "user": username,
            "lp" : plate_no
        })
        if found is not None:
            return True
        else:
            return False
    

if __name__ == "__main__":
    dbo = _DBAccessObj(host="172.28.80.1")
    dbo.register_user("Ranajit", "19028A")
    print(dbo.is_registered("Ranajit", "19028A"))
    dbo.unregister_user("Ranajit", "19028A")
