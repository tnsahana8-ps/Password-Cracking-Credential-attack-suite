import hashlib
import re

def generate_hash(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def identify_hash(hash_value):

    if re.fullmatch(r"[a-fA-F0-9]{32}", hash_value):
        return "Possible MD5"

    elif re.fullmatch(r"[a-fA-F0-9]{40}", hash_value):
        return "Possible SHA-1"

    elif re.fullmatch(r"[a-fA-F0-9]{64}", hash_value):
        return "Possible SHA-256"

    elif re.fullmatch(r"[a-fA-F0-9]{128}", hash_value):
        return "Possible SHA-512"

    else:
        return "Unknown hash format"

