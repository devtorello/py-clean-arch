from typing import Type
from flask.json import jsonify
from sqlalchemy.exc import IntegrityError
from src.controller.contracts import Controller, HttpRequest
from src.controller.errors import HttpErrors


def route_adapter(request: any, controller: Type[Controller]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=request.args.to_dict()
    )

    try:
        response = controller.handle(http_request)
    except IntegrityError:
        http_error = HttpErrors.conflict_error()

        return jsonify(http_error)
    except Exception as exc:
        print(exc)

        http_error = HttpErrors.server_error(str(exc))

        return jsonify(http_error)

    return jsonify({"data": response.body}), response.status_code
