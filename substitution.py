def substitution_encrypt(message, key, replacement_sequence):
    _substitution_encrypt = []

    for line in message:
        line_encrypt = ""
        for char in line:
            if char in key[0] or char in key[1]:  # same as 'char.isalpha()' but more specific
                if char.isupper():
                    char_index = key[0].index(char)
                    line_encrypt += key[0][(char_index + replacement_sequence) % len(key[0])]
                else:
                    char_index = key[1].index(char)
                    line_encrypt += key[1][(char_index + replacement_sequence) % len(key[1])]
            else:
                line_encrypt += char
        _substitution_encrypt.append(line_encrypt)

    return _substitution_encrypt
