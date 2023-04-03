from re import sub


# message 'hello world', it transposes word by word and produces 'hloel wrdol'
def transposition_encrypt_by_word(message):
    _transposition_encrypt = []

    for line in message:
        line_encrypt = ""
        words = line.replace("\n", "").split(" ")
        for word in words:
            index = 0
            transpose_upper = ""
            transpose_lower = ""
            for char in word:
                if index % 2 == 0:
                    transpose_upper += char
                else:
                    transpose_lower += char
                index += 1
            line_encrypt += transpose_upper + transpose_lower + " "
        _transposition_encrypt.append(line_encrypt.rstrip() + "\n")

    _last_index = len(_transposition_encrypt) - 1
    _transposition_encrypt[_last_index] = _transposition_encrypt[_last_index].replace("\n", "")
    return _transposition_encrypt


# message 'hello world', it treats whitespaces as a normal char and produces 'hlowrdel ol'
def transposition_encrypt_with_ws(message):
    _transposition_encrypt = []

    for line in message:
        index = 0
        transpose_upper = ""
        transpose_lower = ""
        line = line.replace("\n", "")
        for char in line:
            if index % 2 == 0:
                transpose_upper += char
            else:
                transpose_lower += char
            index += 1
        _transposition_encrypt.append(transpose_upper + transpose_lower + "\n")

    _last_index = len(_transposition_encrypt) - 1
    _transposition_encrypt[_last_index] = _transposition_encrypt[_last_index].replace("\n", "")
    return _transposition_encrypt


# message 'hello world', it removes any whitespace 'helloworld' and produces 'hloolelwrd'
def transposition_encrypt_without_ws(message):
    _transposition_encrypt = []

    for line in message:
        index = 0
        transpose_upper = ""
        transpose_lower = ""
        line = sub(r"\s", "", line)
        for char in line:
            if index % 2 == 0:
                transpose_upper += char
            else:
                transpose_lower += char
            index += 1
        _transposition_encrypt.append(transpose_upper + transpose_lower + "\n")

    _last_index = len(_transposition_encrypt) - 1
    _transposition_encrypt[_last_index] = _transposition_encrypt[_last_index].replace("\n", "")
    return _transposition_encrypt
