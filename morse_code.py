
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}


def encrypting(text):
    coded_dict = []
    for letter in text:
        if letter in MORSE_CODE_DICT.keys():
            coded_dict.append(MORSE_CODE_DICT[letter])
        else:
            coded_dict.append(letter)
    coded_phrase = ' '.join(coded_dict)
    return coded_phrase


def decrypting(morse_code):
    morse_code = morse_code.split(" ")
    decoded_dict = []
    for symbol in morse_code:
        if symbol == '':
            decoded_dict.append(" ")
        else:
            for char, morse in MORSE_CODE_DICT.items():
                if symbol == morse:
                    decoded_dict.append(char)
    decoded_phrase = ''.join(decoded_dict)
    return decoded_phrase


def morse_code_program():
    encrypted_phrase = ''
    while True:
        choice = input("Please choose an option:"
                       "\n--Press 1 to encrypt."
                       "\n--Press 2 to decrypt."
                       "\n--Press 0 to quit."
                       "\nChoice: ")
        if choice == "1":
            phrase_input = input("Type your phrase/text to code: \n").upper()
            encrypted_phrase = encrypting(phrase_input)
            print(encrypted_phrase)
        elif choice == "2":
            if_decode_same_phrase = input("Do you want to decode the last encoded phrase? ").lower()
            if if_decode_same_phrase == "yes":
                decrypted_phrase = decrypting(encrypted_phrase)
                print(decrypted_phrase.title())
            elif if_decode_same_phrase == "No":
                morse_to_decode = input("Please type morse you want to decode.")
                decrypted_phrase = decrypting(morse_to_decode)
                print(decrypted_phrase)
            else:
                print("Sorry, You gave unknown request which I can't complete.")
        elif choice == "0":
            print("Thank You for using our 'Morse Code' program. Good Bye!")
            break
        else:
            print("Invalid choice, please choose from the available options.")


if __name__ == "__main__":
    morse_code_program()
