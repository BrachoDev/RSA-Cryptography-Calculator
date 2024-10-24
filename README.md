# RSA-Cryptography-Calculator
This project is a simple Python implementation of RSA encryption and decryption, which allows you to encrypt messages and decode them using prime numbers and public keys.

## Features

- **Encrypt a message:** Convert a phrase into a series of encrypted numbers using RSA encryption.
- **Decrypt a message:** Decode a series of numbers back into the original phrase.
- Handles both letters and spaces in the input message.

## How It Works

1. **RSA Encryption:** 
   - The user inputs two prime numbers (p and q) and a public key (e).
   - The message is encrypted by converting each character into its corresponding position in the alphabet, and then performing RSA encryption on those numbers.

2. **RSA Decryption:** 
   - The user inputs the same prime numbers (p and q), the public key (e), and a list of encrypted numbers.
   - The tool calculates the private key and decrypts the numbers back into the original message.

## Example Usage

1. **Encrypt a Message**
   ```bash
   Input prime p: 3
   Input prime q: 11
   Input public key e: 7
   Insert your phrase: HELLO WORLD
   Encrypted values: [2, 14, 12, 12, 27, 32, 23, 27, 6, 12, 16]

2. **Decrypt a Message**
    ```bash
    Input prime p: 3
    Input prime q: 11
    Input public key e: 7
    Input numbers separated by commas: 2,14,12,12,27,32,23,27,6,12,16
    Decoded message: HELLO WORLD

## Requirements    
* Python 3.x
* `string` module (comes with Python's standard library)

## How to run:
Just clone this repository and run the main.py file. Follow the prompts to either encrypt or decrypt your message ;)