import string

# Initializing variables and lists
alphabet = list(string.ascii_uppercase)

new_number_list = []

# Function to encrypt a word
def encrypt_word(p, q, e):
    word = input("Insert your phrase: ")
    word_uppercase = word.upper()
    
    for char in word_uppercase:
        if char in alphabet:
            letter_index = alphabet.index(char) + 1
            encrypted_char = encrypt_character(p, q, letter_index, e)
            new_number_list.append(encrypted_char)
        elif char == " ":
            new_number_list.append(32)  # Space representation
    
    print("Encrypted values:", new_number_list)

# Function to encrypt a character
def encrypt_character(p, q, m, e):
    n = p * q
    return pow(m, e, n)  # Efficient modular exponentiation

# Function to decode a phrase
def decode_phrase(p, q, e):
    def mod_inverse(e, phi_n):
        old_r, r = e, phi_n
        old_s, s = 1, 0
        
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
        
        if old_s < 0:
            old_s += phi_n
        return old_s

    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)

    encoded_numbers = input('Input numbers separated by commas: ').split(',')
    decoded_list = []
    
    for number in encoded_numbers:
        decoded_number = decrypt_character(int(number), d, n)
        decoded_list.append(decoded_number)
    
    decoded_message = ''.join([alphabet[num-1] if 1 <= num <= 26 else ' ' for num in decoded_list])
    print("Decoded message:", decoded_message)

# Function to decrypt a character
def decrypt_character(c, d, n):
    return pow(c, d, n)  # Efficient modular exponentiation

# Main execution flow
p = int(input("Input prime p: "))
q = int(input("Input prime q: "))
e = int(input("Input public key e: "))

user_choice = input("Choose 1 to Encrypt or 2 to Decode: ")
if user_choice == "1":
    encrypt_word(p, q, e)
elif user_choice == "2":
    decode_phrase(p, q, e)
