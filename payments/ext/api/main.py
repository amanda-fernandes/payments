from flask import Blueprint, g
from flask_expects_json import expects_json
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

schema = {
  "type": "object",
  "properties": {
    "exp_date": {"type": "string", "minLength": 7, "error_msg": "Please provide a valid Expiration Date YYYY/MM"},
    "holder": { "type": "string", "minLength": 2 , "error_msg": "Please provide a Holder name"},
    "cc_number": { "type": "string", "minLength": 16, "error_msg": "Please provide a valid Credit Card Number" },
    "cvv": {"type":"number","minimum": 100, "maximum": 9999, "error_msg": "Please provide a valid CVV" }  
  },
  "required": ["exp_date","holder","cc_number"]
}

@bp.route("/v1/credit-card", methods=['POST'])
@expects_json(schema)
def add_credit_card():    
    data = g.data
    response = credit_card.add_credit_card(data)
    return response

