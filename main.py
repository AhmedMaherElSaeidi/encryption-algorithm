from substitution import substitution_encrypt
from transposition import transposition_encrypt_by_word, transposition_encrypt_without_ws, transposition_encrypt_with_ws

# reading file 1 'key' into a two-dimension array
with open('file_number_1.txt', encoding='utf-8') as file1:
    file_number_1 = file1.readlines()
alpha_2d = [file_number_1[0].replace("\n", "").split(","), file_number_1[1].replace("\n", "").split(",")]

# reading file 2 'message file to be encrypted'
with open('file_number_2.txt', encoding='utf-8') as file2:
    file_number_2 = file2.readlines()

# Applying substitution encryption algorithm
substitution_encrypt = substitution_encrypt(file_number_2, alpha_2d, 3)

# Applying transposition encryption algorithms on the output of 'substitution_encrypt'
transposition_by_word = transposition_encrypt_by_word(substitution_encrypt)
transposition_with_ws = transposition_encrypt_with_ws(substitution_encrypt)
transposition_without_ws = transposition_encrypt_without_ws(substitution_encrypt)

# Writing encrypted message in file 3
file3 = open("file_number_3.txt", "w")

for substitution_encrypt_line in substitution_encrypt:
    file3.write(substitution_encrypt_line)

file3.write("\n\n")
for transposition_by_word_line in transposition_by_word:
    file3.write(transposition_by_word_line)

file3.write("\n\n")
for transposition_with_ws_line in transposition_with_ws:
    file3.write(transposition_with_ws_line)

file3.write("\n\n")
for transposition_without_ws_line in transposition_without_ws:
    file3.write(transposition_without_ws_line)

file3.close()
