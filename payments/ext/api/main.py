from flask import Blueprint, g, jsonify, request
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

validation = {
  "type": "object",
  "properties": {
    "cc_number": { "type": "string", "minLength": 16, "maxLength": 16, "error_msg": "Please provide a valid Credit Card Number" },    
    "exp_date": {"type": "string", "minLength": 7, "error_msg": "Please provide a valid Expiration Date YYYY/MM"},
    "holder": { "type": "string", "minLength": 2 , "error_msg": "Please provide a Holder name"},    
    "cvv": {"type":"string","minLength": 3, "maxLength": 4, "error_msg": "Please provide a valid CVV" }  
  },
  "required": ["exp_date","holder"]
}

@bp.route("/v1/credit-card", methods=['POST'])
@expects_json(validation)
def add_credit_card():    
    data = g.data
    response = credit_card.add_credit_card(data)
    return response

cc_validation = {
  "type": "object",
  "properties": {        
    "cc_number": { "type": "string", "minLength": 16, "maxLength": 16, "error_msg": "Please provide a valid Credit Card Number" },    
  },
  "required": ["cc_number"]
}
@bp.route("/v1/credit-card-validation", methods=['POST'])
@expects_json(cc_validation)
def validate_credit_card():  
    data = g.data
    cc_number = data["cc_number"]
    response = credit_card.validate_credit_card(cc_number)
    return response 