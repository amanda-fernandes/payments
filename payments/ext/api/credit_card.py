from flask import jsonify
from payments.ext.api import utils
from payments.ext.model.CreditCard import CreditCard, db
#from creditcard import CreditCard

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
        "cc_number": credit_card.cc_number,
        "cvv": credit_card.cvv
    }

    return jsonify({"message": data}), 200

def validate_credit_card(cc_number): 
    try:
        #validate credit card     
        data = "200"
        return jsonify({'message' : data}) , 200    
    except NotUniqueError as e:
        return jsonify(dict(message=e.message)), 409

def add_credit_card(data):    
    try:
        #validate credit card     
        #cc = CreditCard(card_number)
        #if(cc.is_valid() and cc.get_brand() and utils.is_date_valid()):
        new_date = validate_date(data["exp_date"])
        if(new_date != False):            
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