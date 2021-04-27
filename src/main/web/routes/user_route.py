from flask import Blueprint, request
from src.main.factories.user.remove_user.remove_user_factory import remove_user_factory
from src.main.factories.user.register_user import register_user_factory
from src.main.factories.user.fetch_users import fetch_users_factory
from src.main.factories.user.find_user import find_user_factory
from src.main.web.config.route_adapt import route_adapter

user_routes_bp = Blueprint("api_routes", __name__)


@user_routes_bp.route("/register", methods=["POST"])
def register_user():
    """ register user route """

    return route_adapter(request=request, controller=register_user_factory())


@user_routes_bp.route("/find", methods=["GET"])
def find_user():
    """ find user route """

    return route_adapter(request=request, controller=find_user_factory())


@user_routes_bp.route("/fetch", methods=["GET"])
def fetch_users():
    """ fetch users route """

    return route_adapter(request=request, controller=fetch_users_factory())


@user_routes_bp.route("remove", methods=["GET"])
def remove_user():
    """ remove user route """

    return route_adapter(request=request, controller=remove_user_factory())
