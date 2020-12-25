import base64
import calendar
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import datetime
from datetime import date

#Date
def date_to_string(mysql_date):
    return mysql_date.isoformat()

def is_date_valid(exp_date):
    inputed_date = string_to_date(exp_date)
    now = date.today()
    min_date = datetime.datetime(now.year, now.month, 28)
    print(min_date)
    print(inputed_date)
    if(min_date <= inputed_date):
        return True
    return False

def string_to_date(str_date):
    inputed = str_date.split("/")
    inputed_date = datetime.datetime(int(inputed[0]),int(inputed[1]),28)
    return inputed_date

#YYYY-MM-DD
def format_exp_date(format_date):
    inputed = format_date.split("/")
    last_day = calendar.monthrange(int(inputed[0]), int(inputed[1]))[1]
    formatted = format_date + "/" + str(last_day)
    return formatted

#Criptography
def generating_password():
    password_provided = "password"
    password = password_provided.encode() 
    salt = b'salt_' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) 
    return key

def encripty(message):
    key = generating_password()
    cripto = Fernet(key)
    encoded = message.encode()
    encrypted = cripto.encrypt(bytes(encoded))   
    return encrypted

def decrypt(message):
    key = generating_password()
    cripto = Fernet(key)
    decrypted_message = cripto.decrypt(message)
    decrypted_message = decrypted_message.decode()
    return decrypted_message