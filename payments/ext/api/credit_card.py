from flask import jsonify
from payments.ext.api import utils
from payments.ext.model.CreditCard import CreditCard, db
from payments.ext.creditcard.creditcard import CreditCard as cc
from payments.ext.creditcard.creditcard.exceptions import BrandNotFound

def get_all():
    credit = CreditCard.query.all()
    if(credit):
        all = []
        for cc in credit:
            new_cc = {
                "id": cc.id,
                "exp_date": utils.date_to_string(cc.exp_date),
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
        "cc_number": utils.decrypt(credit_card.cc_number),
        "cvv": credit_card.cvv
    }

    return jsonify({"message": data}), 200


def add_credit_card(data):    
    try:  
        card = cc(data['cc_number'])
        new_date = validate_date(data["exp_date"])
        if(new_date != False and card.is_valid()):            
            new_user = CreditCard(exp_date=new_date, holder=data['holder'],cc_number=utils.encripty(data['cc_number']), cvv=data['cvv'])
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message' : '200'})
        return jsonify({'message' : 'Invalid Date!'})        
    except NotUniqueError as e:
        return jsonify(dict(message=e.message)), 409    
    
def validate_date(exp_date):
    if(utils.is_date_valid(exp_date)):
        new_date = utils.format_exp_date(exp_date)
        return new_date
    else:
        return False

def validate_credit_card(card_number):
    card = cc(card_number)
    if(card.is_valid()):
        try:
            brand = card.get_brand()
            return jsonify({'brand' : brand })  
        except BrandNotFound:
            return jsonify({'message' : 'No Brand!'})  

    return jsonify({'message' : 'Not a valid Credit Card Number!'})  
 
