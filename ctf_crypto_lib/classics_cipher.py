def str_bits(string):
    return ''.join(format(ord(c), '08b') for c in string)

def bits_str(bits):
    caracteres = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join([chr(int(b, 2)) for b in caracteres])

def cipher_cesar(displacement, message, language):
    dictionary_english = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
        "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
    }

    dictionary_spanish = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "Ñ": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
    }

    if language == "ES":
        dictionary = dictionary_spanish
        reverse_dict = {v: k for k, v in dictionary_spanish.items()}  
        alphabet_size = 27 
    elif language == "EN":
        dictionary = dictionary_english
        reverse_dict = {v: k for k, v in dictionary_english.items()}  
        alphabet_size = 26 
    else:
        print("Idioma no soportado")
        return

    message = message.upper()

    ciphered_message = []

    for letter in message:
        if letter in dictionary:
            position = dictionary[letter]

            new_position = (position + displacement) % alphabet_size

            ciphered_letter = reverse_dict[new_position]

            ciphered_message.append(ciphered_letter)
        else:
            ciphered_message.append(letter)

    return "".join(ciphered_message)

def decoded_cesar(language, cipher_text, displacement):
    dictionary_english = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
        "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
    }

    dictionary_spanish = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "Ñ": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
    }

    if language == "ES":
        dictionary = dictionary_spanish
        reverse_dict = {v: k for k, v in dictionary_spanish.items()}  
        alphabet_size = 27 
    elif language == "EN":
        dictionary = dictionary_english
        reverse_dict = {v: k for k, v in dictionary_english.items()}  
        alphabet_size = 26 
    else:
        print("Idioma no soportado")
        return

    cipher_text = cipher_text.upper()

    decoded_message = []

    for letter in cipher_text:
        if letter in dictionary:
            position = dictionary[letter]

            new_position = (position - displacement) % alphabet_size

            ciphered_letter = reverse_dict[new_position]

            decoded_message.append(ciphered_letter)
        else:
            decoded_message.append(letter)

    return "".join(decoded_message)

def cipher_XOR(message, key):
    message_bin = str_bits(message) 
    key_bin = str_bits(key)  

    cipher_message = ""
    key_len = len(key_bin)

    for bloqs in range(0, len(message_bin), key_len):
        message_bloqs = message_bin[bloqs: bloqs + key_len]
        key_bloqs = key_bin[:len(message_bloqs)]  

        for i in range(len(message_bloqs)):
            cipher_bit = str(int(message_bloqs[i]) ^ int(key_bloqs[i])) 
            cipher_message += cipher_bit  
    
    return (cipher_message)

def decode_XOR(cipher_text, key): 
    key_bin = str_bits(key)  

    message = ""
    key_len = len(key_bin)

    for bloqs in range(0, len(cipher_text), key_len):
        message_bloqs = cipher_text[bloqs: bloqs + key_len]
        key_bloqs = key_bin[:len(message_bloqs)]  

        for i in range(len(message_bloqs)):
            cipher_bit = str(int(message_bloqs[i]) ^ int(key_bloqs[i])) 
            message += cipher_bit  
    
    return bits_str(message)




                