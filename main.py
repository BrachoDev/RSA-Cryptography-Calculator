# Initializing variables and lists

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

new_number_list = []

# Function to encrypt word
def encrypt_word():
    # Word to transform
    word = input("Insert your phrase: ")
    word_uppercase = word.upper()
    word_in_list = list(word_uppercase)
    # Loop that goes through the word's list and prints the index value:
    for char in word_in_list:
        if char in alphabet:
            letter_index = alphabet.index(char) + 1
            get_new_number(p, q, letter_index, e)
        elif char == " ":
            new_number_list.append(32)
    print(new_number_list)

# Function to get new encoded number
def get_new_number(p,q,m,e):
    n = p * q
    c = (m ** e) % n
    new_number_list.append(c)

# Function to decode word
def decode_phrase(p,q,e):
    # Function to compute the greatest common divisor using the Euclidean algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Function to compute the modular inverse using the Extended Euclidean Algorithm
    def mod_inverse(e, phi_n):
        # e * d ≡ 1 (mod phi_n), we need to find d
        old_r, r = e, phi_n
        old_s, s = 1, 0
        old_t, t = 0, 1
        
        # Extended Euclidean Algorithm
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        
        # The modular inverse is old_s (which is the value of d)
        # but we need to ensure it is positive
        if old_s < 0:
            old_s += phi_n
        return old_s

    # Compute n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)


    # Calculate the private key d
    d = mod_inverse(e, phi_n)

    encoded_number = input('Input number separated by ",": ').upper()
    list_encoded_number = encoded_number.split(',')
    decoded_list = []
    get_new_decoded_number(list_encoded_number,d,n,decoded_list)

    for number in decoded_list:
        if number <= 26:
            print(alphabet[number-1])
        
        elif number > 26:
            print(" ")

# Function to get new decoded number
def get_new_decoded_number(list_encoded_number,d,n,decoded_list):
    for number in list_encoded_number:
        m = int(number)
        decoded_number = (m ** d) % n
        decoded_list.append(decoded_number)





# Initial values:

# Prime numbers p and q
p = int(input("Input p value: "))

q = int(input("Input q value: "))

# Public key

e = int(input("Input public key: "))

# Menu
user_options = input("Choose 1 to Encrypt or 2 to decode ")
if user_options == "1":
    encrypt_word()
elif user_options == "2":   
    decode_phrase(p,q,e)