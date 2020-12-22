from flask import Blueprint
from payments.ext.api import credit_card

bp = Blueprint("api", __name__)


@bp.route("/v1/credit-card", methods=["GET"])
def list_credit_card():
    response = credit_card.get_all()
    return response


@bp.route("/v1/credit-card/<id>", methods=["GET"])
def detail_credit_card(id):
    response = credit_card.get_by_id(id)
    return response
