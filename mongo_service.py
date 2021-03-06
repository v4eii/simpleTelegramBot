import mongo_repo as db
from user import User


def save(user):
    result = db.find_by_username(user.username)
    if len(result) != 0:
        db.remove(result)
    return db.insert_data(user_to_user_dict(user))


def find_all():
    user_dict_list = db.find_all_users()
    return [User(x['name'], x['surname'], x['age'], x['username'], x['personal_links']) for x in user_dict_list]


def remove(user):
    return db.remove(user_to_user_dict(user))


def user_to_user_dict(user):
    return {
        "name": f"{user.name}",
        "surname": f"{user.surname}",
        "age": user.age,
        "username": f"{user.username}",
        "personal_links": user.personal_links
    }
