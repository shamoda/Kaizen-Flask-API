from flask import Blueprint

from src.constants.common_const import BASE_API

your_component = Blueprint("your_component", __name__, url_prefix=BASE_API+"/your_component")

@your_component.get('/')
def get_all():
    return {"all_items": []}
