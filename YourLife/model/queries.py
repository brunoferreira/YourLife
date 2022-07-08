from YourLife import db
from YourLife.model.tables import User, Post, Follow

def username_available(username):
    query = User.query.filter_by(username=username).first()
    if query == None:
        return True
    return False

def email_available(email):
    query = User.query.filter_by(email=email).first()
    if query == None:
        return True
    return False

def login(username, password):
    query = User.query.filter_by(username=username, password=password).first()
    if query == None:
        return False
    return True