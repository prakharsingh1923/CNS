from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate sender's RSA key pair (private and public key)
sender_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

sender_public_key = sender_private_key.public_key()

# Generate recipient's RSA key pair (private and public key)
recipient_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

recipient_public_key = recipient_private_key.public_key()

# Create a message to be signed
message = b"Hello, this is a message."

# Sign the message with sender's private key
signature = sender_private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Hash the signature
digest = hashes.Hash(hashes.SHA256())
digest.update(signature)
hashed_signature = digest.finalize()

# Encrypt the hashed signature with recipient's public key
encrypted_signature = recipient_public_key.encrypt(
    hashed_signature,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original message:", message)
print('/n')
print("Digital signature:", signature)
print('/n')
print("Encrypted digital signature:", encrypted_signature)
