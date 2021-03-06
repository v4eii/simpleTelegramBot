from pymongo import MongoClient

client: MongoClient = MongoClient(host="localhost", port=27017)

db = client["bot_client"].bot_client


def insert_data(user_dict):
    return db.insert_one(user_dict)


def find_all_users():
    return list([x for x in db.find()])


def remove(user_dict):
    return db.delete_one(user_dict)


def find_by_username(username):
    try:
        return db.find({"username": username}).next()
    except StopIteration:
        return {}


def update(user_dict, old_user_dict):
    return db.update_one(old_user_dict, user_dict)
