def generate_dictionary():

    base_words = [
        "welcome",
        "student",
        "cybersecurity",
        "password",
        "testing",
        "computer"
    ]

    variations = set()

    for word in base_words:
        variations.add(word)
        variations.add(word.upper())
        variations.add(word.capitalize())
        variations.add(word + "123")
        variations.add(word + "@123")

    return sorted(variations)


def save_dictionary(words, filename="sample_data/test_dictionary.txt"):

    with open(filename, "w") as file:
        for word in words:
            file.write(word + "\n")

    return filename
