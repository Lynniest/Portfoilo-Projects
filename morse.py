def convert_text_to_morse(text):
    result = ""
    for letter in text:
        if letter.upper() in morse_dict:
            result += morse_dict[letter.upper()] + " "
        else:
            result += letter
    return result

def convert_morse_to_text(code):
    result = ""
    code_founded = False
    for code in code.split():
        for key in morse_dict:
            if morse_dict[key] == code:
                result += key
                code_founded = True
                break
        if not code_founded:
            result += code
    return result


morse_dict = {'A': ".-", 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

code_again = True
while code_again:
    code_type = input("Type 1 to convert text to morse code and type 2 to convert morse code to text.  ")

    if code_type == "1":
        text_input = input("Please enter text that you want to convert:  ")
        print(f"This is the morse code you requested for:\n{convert_text_to_morse(text_input)}")

    elif code_type == "2":
        code_input = input("Please enter your morse code separated by a space between the letters in one word:\n")
        print(f"This is decoded text you requested for:\n{convert_morse_to_text(code_input)}")

    else:
        print(f"{code_type} is not an option! Please read the instruction carefully.")

    try_again = input("Enter 't' if you want to try again.")
    if try_again.lower() == "t":
        code_again = True
    else:
        code_again = False

