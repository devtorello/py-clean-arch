from flask import Blueprint, request
from src.main.factories.register_user import register_user_factory
from src.main.web.config.route_adapt import route_adapter

user_routes_bp = Blueprint("api_routes", __name__)


@user_routes_bp.route("/user/register", methods=["POST"])
def register_user():
    """ register user route """

    return route_adapter(request=request, controller=register_user_factory())
