code = {'A': '.-', 'B': "-...",
        'C': "-.-.", "D": "-..",
        'E': ".", "F": "..-.",
        'G': "--.", "H": "....",
        'I': "..", "J": ".---",
        "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.",
        "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.",
        "S": '...', "T": "-",
        "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        '1': ".----", '2': "..---",
        '3': "...--", '4': "....-",
        '5': '.....', "6": '-....',
        "7": "--...", "8": "---..",
        "9": "----.", "0": "-----"
        }


def to_morse(text):
    morse_text = ""
    for char in text:
            try:
                morse_text += f'{code[char.upper()]} '
            except:
                continue
    return morse_text


def to_word(morse_text):
    text = ""
    list_char = morse_text.split()
    for char in list_char:
        for k, v in code.items():
            if v == char:
                text += k
                break
    return text





word = input("Input word or text: ")
print(to_morse(word))
print(to_word('.. -. .--. ..- - .-- --- .-. -.. --- .-. - . -..- - '))


