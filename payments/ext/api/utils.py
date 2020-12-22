import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

#Date
def dateToString(mysql_date):
    return mysql_date.isoformat()

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

def decrypt():
    key = generating_password()
    cripto = Fernet(key)
    decrypted_message = cripto.decrypt(credit_card.cc_number)
    decrypted_message = decrypted_message.decode()
    data['cc_number'] = decrypted_message
    return decrypted_message