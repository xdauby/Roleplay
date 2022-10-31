import hashlib

def hash_password(to_hash:str):
    return hashlib.sha256(str.encode(to_hash)).hexdigest()

