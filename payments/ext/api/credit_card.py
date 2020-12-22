from flask import jsonify
from payments.ext.api import utils
from payments.ext.model.CreditCard import CreditCard, db


def get_all():
    credit = CreditCard.query.all()
    if(credit):
        all = []
        for cc in credit:
            new_cc = {
                "id": cc.id,
                "exp_date": dateToString(cc.exp_date),
                "holder": cc.holder,
                "cc_number": utils.decrypt(cc.cc_number),
                "cvv": cc.cvv,
            }
            all.append(new_cc)
        return jsonify({"message": all}), 200

    return jsonify({"message": "0 credit card!"}), 200


def get_by_id(id):
    credit_card = CreditCard.query.filter_by(id=id).first()
    if not credit_card:
        return jsonify({"message": "Not found!"})

    data = {
        "id": credit_card.id,
        "exp_date": credit_card.exp_date,
        "holder": credit_card.holder,
        "cc_number": credit_card.cc_number,
        "cvv": credit_card.cvv
    }

    return jsonify({"message": data}), 200
