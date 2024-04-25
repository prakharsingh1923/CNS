from cryptography.rsa import generate_private_key, PrivateKey, RSAPublicKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate RSA key pair (**do this offline and keep private key secret!** )
private_key = generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get the public key (can be distributed)
public_key = private_key.public_key()

# Message to encrypt (needs padding for RSA)
message = "INDIA".encode()  # Encode to bytes for encryption

# Encryption (assuming proper padding is done before feeding to RSA)
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
