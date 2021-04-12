
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P",
            "R", "S", "Ş", "T", "U", "V", "Y", "Z"]


def separated_alphabet(count):
    alp_first = []
    alp_second = []
    for item in range(len(alphabet)):
        if item < count:
            alp_first.append(alphabet[item])
        else:
            alp_second.append(alphabet[item])
    alp_second.extend(alp_first)
    return alp_second


def coder(cipher, count):
    last_alphabet = separated_alphabet(count)
    return_words = []
    for item in cipher:
        if item == " ":
            return_words.append(" ")
        else:
            index = alphabet.index(item.upper())
            letter = last_alphabet[index]
            return_words.append(letter)
    word = ""
    for item in return_words:
        word += item
    return word


def decoder(cipher, count):
    last_alphabet = separated_alphabet(count)
    return_words = []
    for item in cipher:
        if item == " ":
            return_words.append(" ")
        else:
            index = last_alphabet.index(item.upper())
            letter = alphabet[index]
            return_words.append(letter)
    word = ""
    for item in return_words:
        word += item
    return word


running = True

while running:
    print("Welcome to cipher!!")
    cipher_words = input("What is your words : ")
    cipher_count = int(input("How much count do you want : "))
    coder_or_decoder = input("Coder or decoder : ")
    if coder_or_decoder == "coder":
        print(coder(cipher_words, cipher_count).lower())
    elif coder_or_decoder == "decoder":
        print(decoder(cipher_words, cipher_count).lower())
    choice = input("Do you cipher want again(Y/N) : ")
    if choice.upper() == "N":
        running = False
