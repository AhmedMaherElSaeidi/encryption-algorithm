from substitution import substitution_encrypt
from transposition import transposition_encrypt_by_word, transposition_encrypt_without_ws, transposition_encrypt_with_ws

# reading file 1 'key' into a two-dimension array
with open('assets/file_number_1.txt', encoding='utf-8') as file1:
    file_number_1 = file1.readlines()

alpha_2d = []
for line in file_number_1:
    alpha_2d.append(line.replace("\n", "").split(","))

# reading file 2 'message file to be encrypted'
with open('assets/file_number_2.txt', encoding='utf-8') as file2:
    file_number_2 = file2.readlines()

# Applying substitution encryption algorithm
substitution_encrypt = substitution_encrypt(file_number_2, alpha_2d, 3)

# Applying transposition encryption algorithms on the output of 'substitution_encrypt'
transposition_by_word = transposition_encrypt_by_word(substitution_encrypt)
transposition_with_ws = transposition_encrypt_with_ws(substitution_encrypt)
transposition_without_ws = transposition_encrypt_without_ws(substitution_encrypt)

# Writing encrypted message in file 3
with open("assets/file_number_3_substitution_encrypt_line.txt", "w") as file3_substitution:
    for substitution_encrypt_line in substitution_encrypt:
        file3_substitution.write(substitution_encrypt_line)

with open("assets/file_number_3_transposition_by_word_line.txt", "w") as file3_transposition1:
    for transposition_by_word_line in transposition_by_word:
        file3_transposition1.write(transposition_by_word_line)

with open("assets/file_number_3_transposition_with_ws_line.txt", "w") as file3_transposition2:
    for transposition_with_ws_line in transposition_with_ws:
        file3_transposition2.write(transposition_with_ws_line)

with open("assets/file_number_3_transposition_without_ws_line.txt", "w") as file3_transposition3:
    for transposition_without_ws_line in transposition_without_ws:
        file3_transposition3.write(transposition_without_ws_line)