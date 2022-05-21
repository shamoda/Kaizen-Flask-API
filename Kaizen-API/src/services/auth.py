from flask import Blueprint, request
from src.constants.common_const import BASE_API
from src.modules.auth_module import Auth

auth = Blueprint("auth", __name__, url_prefix=BASE_API+"/auth")
auth_module = Auth()


@auth.post('/register')
def register():
    return auth_module.register(request)


@auth.post('/login')
def login():
    return auth_module.login(request)


@auth.get('/all')
def get_all_users():
    return auth_module.get_all_users()


@auth.patch('/update/<id>')
def update_rank(id):
    return auth_module.update_rank(id, request)


@auth.delete('/delete/<id>')
def delete_user(id):
    return auth_module.delete_user(id)
        