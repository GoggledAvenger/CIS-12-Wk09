# Lab 7 from https://github.com/THartmanOfTheRedwoods/PyLab007

# Part 1 - Building the Vigenere Square

alpha_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {k: v for v, k in enumerate(alpha_string)}

def vig_alpha_list_of_lists(alphabet):
    rows = []
    for i in range(len(alphabet)):
        if i == 0:
            row = ' ' + alphabet[i:] + alphabet[:i]
            rows.append(list(row))
        row = alphabet[i] + alphabet[i:] + alphabet[:i]
        rows.append(list(row))
    return rows

def format_vigenere_sq(rows):
    for i, row in enumerate(rows):
        print(f'| { " | ".join(row) } |')
        if i == 0:
            print('|---' * len(row) + '|')

list_in_list = vig_alpha_list_of_lists(alpha_string)
# format_vigenere_sq(list_in_list)

# Part 2 - Encryption

def letter_to_index(letter):
    if letter in alpha_dict:
        return alpha_dict[letter]

def index_to_letter(index,alphabet):
    if 0 >= index < len(alphabet):
        return alphabet[index]
    return -1

def vigenere_index(key_letter, plaintext_letter):
    k_index = letter_to_index(key_letter)
    p_index = letter_to_index(plaintext_letter)
    vigenere_cipher = (p_index + k_index) % len(alpha_dict)
    return index_to_letter(vigenere_cipher)

def encrypt_vigenere(keyword, plaintext):
    cipher_text = []
    for i, l in enumerate(plaintext):
        cipher_text.append(vigenere_index(keyword[i % len(keyword)], l) if l != ' ' else l)
    return ''.join(cipher_text)

key = 'DAVINCI'
message = 'the eagle has landed'

# print(encrypt_vigenere(key, message, alpha_string + ' '))

# Part 3 - Decryption

def undo_vigenere_index(key_letter, cypher_letter):
    k_index = letter_to_index(key_letter)
    vigenere_cipher = letter_to_index(cypher_letter)
    p_index = (vigenere_cipher - k_index) % len(alpha_dict)
    return index_to_letter(p_index)

def decrypt_vigenere(key_word, cipher_text, alphabet):
    plain_text = []
    for i, l in enumerate(cipher_text):
        plain_text.append(undo_vigenere_index(key_word[i % len(key_word)], l) if l != ' ' else l)
    return ''.join(plain_text)

secret_message = 'WHZHRCOOEUPNUHOAHLRF'

# print(decrypt_vigenere(key, secret_message, alpha_string + ' '))

# Part 4 - App w/ Menu

def execute(menu, encrypted_list):
    while True:
        for i in range(0, len(menu) - 1):
            print(menu[i][0])
        try:
            choice = input(f"Make your selection {menu[-1]}:\n")
            if choice in menu[-1]:
                choice -= 1
                menu[choice][1](*menu[choice][2])
            else:
                raise ValueError
        except ValueError:
            print("Improper selection. You must select one of:" + str(menu[-1]))

def enc_menu(key, encrypted_list):
    plaintext = input("Enter the text you would like to encrypt:\n")
    encrypted_list.append(encrypt_vigenere(key, plaintext))

def dec_menu(key, encrypted_list):
    for ciphertext in encrypted_list:
        print(decrypt_vigenere(key, ciphertext))

def dump_menu(encrypted_list):
    for enc_text in encrypted_list:
        print(enc_text)

def main_program():
    encrypted_list = []
    key1 = 'DAVINCI'
    menu = [
        ['1) Encrypt', enc_menu, (key, encrypted_list)],
        ['2) Decrypt', dec_menu, [key,encrypted_list]],
        ['3) Dump Encrypted Text', dump_menu, [encrypted_list]],
        ['4) Quit', exit],
        [1,2,3,4]
    ]
    execute(menu,encrypted_list)
    print(encrypted_list)

main_program()

# still doesn't work but my brain is pudding so I give up again