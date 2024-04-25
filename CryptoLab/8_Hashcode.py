from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto import Random

def generate_key_pair():
    random_generator = Random.new().read
    key_pair = RSA.generate(1024, random_generator)
    return key_pair

def sign_message(private_key, message):
    hash_obj = SHA256.new(message.encode())
    private_key_obj = RSA.import_key(private_key)
    signer = PKCS1_v1_5.new(private_key_obj)
    signature = signer.sign(hash_obj)
    return signature

def verify_signature(public_key, message, signature):
    hash_obj = SHA256.new(message.encode())
    public_key_obj = RSA.import_key(public_key)
    verifier = PKCS1_v1_5.new(public_key_obj)
    if verifier.verify(hash_obj, signature):
        print('Signature is valid. Message integrity and source are guaranteed.')
    else:
        print('Signature is invalid. Message integrity and source cannot be guaranteed.')
        
key_pair = generate_key_pair()
print('Key pair generated: \n', key_pair)
print('\n')
private_key = key_pair.export_key()
print('Private key: \n', private_key)
print('\n')
public_key = key_pair.public_key().export_key()
print('Public key: \n', public_key)
print('\n')
message = 'Hello, this is a test message.'
signature = sign_message(private_key, message)
verify_signature(public_key, message, signature)