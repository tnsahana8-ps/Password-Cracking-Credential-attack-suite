from modules.hash_generator import generate_hash

def dictionary_simulation(target_hash, test_passwords):

    attempts = 0
    found = False

    for password in test_passwords:

        attempts += 1

        if generate_hash(password) == target_hash:
            found = True
            break

    return {
        "match_found": found,
        "attempts": attempts
    }
