from uu import encode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower().strip()
shift = int(input("Type the shift number:\n")) % len(alphabet)

def caesar(original_text, shift_amount, encode_or_decode):
    output_word_list = []
    len_alphabet = len(alphabet)
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        letters_position = alphabet.index(letter)
        shifted_letter_position = (letters_position + shift_amount) % len_alphabet
        output_word_list.append(alphabet[shifted_letter_position])
    output_word = "".join(output_word_list)
    print(f"Here is {encode_or_decode}d result: {output_word}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# def encrypt(original_text, shift_amount):
#     encoded_word_list = []
#     len_alphabet = len(alphabet)
#     for letter in original_text:
#         letters_position = alphabet.index(letter)
#         shifted_letter_position = (letters_position + shift_amount) % len_alphabet
#         encoded_word_list.append(alphabet[shifted_letter_position])
#     encoded_word = "".join(encoded_word_list)
#
#     print(f"Here is encoded result: {encoded_word}")
#
# def decrypt(original_text, shift_amount):
#     decoded_word_list = []
#
#     for letter in original_text:
#         letters_position = alphabet.index(letter)
#         shifted_letter_position = (letters_position - shift_amount) % len_alphabet
#         decoded_word_list.append(alphabet[shifted_letter_position])
#     decoded_word = "".join(decoded_word_list)
#
#     print(f"Here is decoded result: {decoded_word}")





# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.



# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# encrypt(original_text=text, shift_amount=shift)
#
# def decrypt(original_text, shift_amount):
#     decoded_cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decoded_cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {decoded_cipher_text}")
#
# decrypt(original_text=text, shift_amount=shift)
#
# def ceaser(direction):
#     if direction == "encode":
#         encrypt(text, shift)
#     elif direction == "decode":
#         decrypt(text, shift)
#
# ceaser(direction)