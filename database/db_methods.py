'''Module for any database related methods
'''
from sqlalchemy import select
from database.db_connector import Session
from models.user import User


session = Session()

def insert_user(user):
    '''insert user record into table
    '''
    session.add(user)
    session.commit()


def select_all_users():
    '''retrieve all records from user table
    '''
    users = []
    stmt = select(User)
    for user in session.scalars(stmt):
        users.append(user)
    return users

def get_user(id):
    user = session.query(User).get(id)
    session.close()
    return user

def delete_user(uid):
    user = get_user(uid)
    session.delete(user)
    session.commit()