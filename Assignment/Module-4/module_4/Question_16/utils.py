import hashlib
import random
import string
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class PaytmChecksum:
    IV = "@@@@&&&&####$$$$"

    @staticmethod
    def encrypt(input_str, key):
        key_bytes = key.encode('utf-8')
        if len(key_bytes) not in [16, 24, 32]:
            key_bytes = key_bytes[:32].ljust(32, b'\0')
        iv_bytes = PaytmChecksum.IV.encode('utf-8')
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes), backend=default_backend())
        encryptor = cipher.encryptor()
        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(input_str.encode('utf-8')) + padder.finalize()
        
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted_data).decode('utf-8')

    @staticmethod
    def decrypt(encrypted_str, key):
        encrypted_data = base64.b64decode(encrypted_str)
        key_bytes = key.encode('utf-8')
        if len(key_bytes) not in [16, 24, 32]:
            key_bytes = key_bytes[:32].ljust(32, b'\0')
        iv_bytes = PaytmChecksum.IV.encode('utf-8')
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes), backend=default_backend())
        decryptor = cipher.decryptor()
        
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data.decode('utf-8')

    @staticmethod
    def generateSignature(params, merchant_key):
        if not isinstance(params, dict):
            raise Exception("Parameters must be a dictionary")
        
        data = "|".join([str(params[key]) for key in sorted(params.keys())])
        salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
        data = data + "|" + salt
        
        hash_string = hashlib.sha256(data.encode('utf-8')).hexdigest()
        hash_string = hash_string + salt
        
        return PaytmChecksum.encrypt(hash_string, merchant_key)

    @staticmethod
    def verifySignature(params, merchant_key, signature):
        try:
            decoded_password = PaytmChecksum.decrypt(signature, merchant_key)
            salt = decoded_password[-4:]
            
            data = "|".join([str(params[key]) for key in sorted(params.keys())])
            data = data + "|" + salt
            
            hash_string = hashlib.sha256(data.encode('utf-8')).hexdigest()
            hash_string = hash_string + salt
            
            return hash_string == decoded_password
        except Exception:
            return False
