from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, DES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from hashlib import sha256
import string
import random

def caesar_cipher(text, key, decrypt=False):

    """
    # Example usage:
    
    plaintext = "Hello, World!"
    key = 3
    encrypted_text = caesar_cipher(plaintext, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = caesar_cipher(encrypted_text, key, decrypt=True)
    print("Decrypted:", decrypted_text)
    
    """

    result = ""
    
    # Define the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the 'decrypt' flag
            if decrypt:
                shift = -key
            else:
                shift = key
            
            # Shift the character within the alphabet
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # If the character is not a letter, leave it unchanged
            shifted_char = char
        
        result += shifted_char
    
    return result


def generate_monoalphabetic_key(seed=None):

    """
    # Example usage:

    plaintext = "Hello, World!"
    key = generate_monoalphabetic_key(seed=42)  # You can specify a seed for reproducibility
    print("Key:", key)
    """

    # Generate a random key for the monoalphabetic cipher
    alphabet = list(string.ascii_lowercase)
    
    if seed is not None:
        random.seed(seed)
    
    random.shuffle(alphabet)
    
    return ''.join(alphabet)

def monoalphabetic_cipher(text, key, decrypt=False):
    """
    # Example usage:

    encrypted_text = monoalphabetic_cipher(plaintext, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = monoalphabetic_cipher(encrypted_text, key, decrypt=True)
    print("Decrypted:", decrypted_text)
    """
    source_alphabet = string.ascii_lowercase
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine whether to encrypt or decrypt based on the 'decrypt' flag
            if decrypt:
                char_index = key.index(char.lower())
                decrypted_char = source_alphabet[char_index]
                if char.isupper():
                    decrypted_char = decrypted_char.upper()
                result += decrypted_char
            else:
                char_index = source_alphabet.index(char.lower())
                encrypted_char = key[char_index]
                if char.isupper():
                    encrypted_char = encrypted_char.upper()
                result += encrypted_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    
    return result

def extend_keyword(keyword, length):
    # Extends the keyword to match the length of the plaintext
    extended_keyword = ""
    keyword_length = len(keyword)
    for i in range(length):
        extended_keyword += keyword[i % keyword_length]
    return extended_keyword

def vigenere_cipher(text, keyword, decrypt=False):
    """
    # Example usage:

    plaintext = "HELLO"
    keyword = "KEY"
    print("Plaintext:", plaintext)
    print("Keyword:", keyword)

    encrypted_text = vigenere_cipher(plaintext, keyword)
    print("Encrypted:", encrypted_text)

    decrypted_text = vigenere_cipher(encrypted_text, keyword, decrypt=True)
    print("Decrypted:", decrypted_text)
    """
    alphabet = string.ascii_uppercase
    result = ""
    
    extended_keyword = extend_keyword(keyword, len(text))
    
    for i in range(len(text)):
        if text[i].isalpha():
            key_char = extended_keyword[i].upper()
            if decrypt:
                shift = (alphabet.index(text[i].upper()) - alphabet.index(key_char)) % 26
            else:
                shift = (alphabet.index(text[i].upper()) + alphabet.index(key_char)) % 26
            shifted_char = alphabet[shift]
            
            # Preserve the case of the original character
            if text[i].islower():
                shifted_char = shifted_char.lower()
            
            result += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            result += text[i]
    
    return result


def aes_encrypt(plaintext, key):
    """
    # Example usage:

    plaintext = "Hello, AES!"
    key = get_random_bytes(16)  # 128-bit key
    print("Plaintext:", plaintext)

    ciphertext = aes_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

    decrypted_text = aes_decrypt(ciphertext, key)
    print("Decrypted:", decrypted_text)
    """
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return nonce + ciphertext + tag

def aes_decrypt(ciphertext, key):
    nonce = ciphertext[:16]
    tag = ciphertext[-16:]
    ciphertext = ciphertext[16:-16]
    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

def des_encrypt(plaintext, key):
    """
    # Example usage:
    
    plaintext = "Hello, DES!"
    key = get_random_bytes(8)  # 64-bit key
    print("Plaintext:", plaintext)

    ciphertext = des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted:", decrypted_text)
    """
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = plaintext + (8 - len(plaintext) % 8) * " "  # Padding
    ciphertext = cipher.encrypt(padded_plaintext.encode())
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext).decode().rstrip()
    return decrypted_text

def triple_des_encrypt(plaintext, key):
    """
    # Example usage:
    
    plaintext = "Hello, 3DES!"
    key = get_random_bytes(24)  # 192-bit key for 3DES
    print("Plaintext:", plaintext)

    ciphertext = triple_des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

    decrypted_text = triple_des_decrypt(ciphertext, key)
    print("Decrypted:", decrypted_text)
    """
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_plaintext = plaintext + (8 - len(plaintext) % 8) * " "  # Padding
    ciphertext = cipher.encrypt(padded_plaintext.encode())
    return ciphertext

def triple_des_decrypt(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext).decode().rstrip()
    return decrypted_text

def generate_rsa_keypair(key_size=2048):
    """
    # Example usage:
    
    plaintext = "Hello, RSA!"
    keypair = generate_rsa_keypair()
    public_key = keypair.publickey()
    private_key = keypair
    """

    # Generate an RSA key pair
    key = RSA.generate(key_size)
    return key

def rsa_encrypt(plaintext, public_key):
    """
    # Example usage:

    ciphertext = rsa_encrypt(plaintext, public_key)
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("Decrypted message:", decrypted_message)
    """
    # Encrypt a message with the public key
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    # Decrypt the message with the private key
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(ciphertext).decode()
    return decrypted_message

def create_rsa_signature(message, private_key):
    """
    # Example usage:

    message_to_sign = "This is a signed message."
    signature = create_rsa_signature(message_to_sign, private_key)
    is_valid_signature = verify_rsa_signature(message_to_sign, signature, public_key)
    print("Signature is valid:", is_valid_signature)
    """
    # Create a digital signature for a message
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_rsa_signature(message, signature, public_key):
    # Verify the digital signature for a message
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Diffie-Hellman Key Exchange
def diffie_hellman(p, g):
    """
    # Example usage:
    p = 23  # A small prime number for demonstration purposes
    g = 5   # A primitive root modulo p

    # Alice and Bob perform Diffie-Hellman key exchange
    alice_private_key, alice_public_key = diffie_hellman(p, g)
    bob_private_key, bob_public_key = diffie_hellman(p, g)

    # Both Alice and Bob compute the shared secret key
    shared_secret_alice = (bob_public_key ** alice_private_key) % p
    shared_secret_bob = (alice_public_key ** bob_private_key) % p

    # Convert the shared secret to bytes (for AES key)
    shared_secret_bytes = shared_secret_alice.to_bytes((shared_secret_alice.bit_length() + 7) // 8, byteorder='big')

    # Derive AES key from shared secret
    aes_key = derive_aes_key(str(shared_secret_bytes))

    # Use the derived AES key for AES encryption and decryption
    plaintext = "Hello, Diffie-Hellman!"
    ciphertext, tag, nonce = aes_encrypt(plaintext, aes_key)
    decrypted_text = aes_decrypt(ciphertext, tag, nonce, aes_key)

    print("Original:", plaintext)
    print("Decrypted:", decrypted_text)
    """
    private_key = random.randint(1, p - 1)
    public_key = (g ** private_key) % p
    return private_key, public_key

# Key drivation for DES
def derive_des_key(shared_secret):
    return shared_secret[:8]

# Key derivation for 3DES
def derive_3des_key(shared_secret):
    return shared_secret[:24]

# Key derivation for AES (256-bit)
def derive_aes_key(shared_secret):
    return sha256(shared_secret).digest()

# Key derivation for Caesar Cipher
def derive_caesar_key(shared_secret):
    return int.from_bytes(shared_secret, byteorder='big') % 26

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_d(e, phi):
    d = 0
    while True:
        d += 1
        if (e * d) % phi == 1:
            return d

def generateMinRSA_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 7
    d = find_d(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def MinRSA_encrypt(message, public_key):
    """
    #Example Useage:

    public, pvt = generateMinRSA_keys(11,13)
    plaintext = "Hello World"
    cipher = MinRSA_encrypt(plaintext, public)
    print(cipher)
    print(MinRSA_decrypt(cipher, pvt))
    """
    n, e = public_key
    ciphertext = []
    for block in message:
        m = ord(block)
        c = pow(m, e, n)
        ciphertext.append(c)
    return ciphertext

def MinRSA_decrypt(ciphertext, private_key):
    n, d = private_key
    message = []
    for block in ciphertext:
        c = block
        m = pow(c, d, n)
        message.append(chr(m))
    return ''.join(message)
