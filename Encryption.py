import random
import string

def Encryption():
    print("----Encryption ----")
    text = input("Enter your text to Encryption: ")
    chiper_text = ""

    for letter in text:
        index = all_chars.index(letter)
        chiper_text += key[index]

    print(f"Your Encryption is: {chiper_text}")
    return chiper_text

def Decryption():
    print("----Decryption ----")
    chiper_text = input("Enter your text to Decryption: ")
    text = ""

    for letter in chiper_text:
        index = key.index(letter)
        text += all_chars[index]

    print(f"Your text is: {text}")
    return text

all_chars = string.ascii_letters + string.digits + string.punctuation
all_chars = list(all_chars)

key = all_chars.copy()
random.shuffle(key)
saved_chiper =""


print("*" * 50)

while True:
    try:
        print("\n(1) Encryption (2) Decryption (3) Save this key (4) Exit")
        userchoice = (input("\nHow can i help...: "))
    except ValueError:
        print("You need to choose between 1 and 2 ")

    if userchoice == "1":
        saved_chiper = Encryption()

    elif userchoice == "2":
        text = Decryption()

    elif userchoice == "3":
        filename = input("Give your key file a name: ")
        with open(filename, "w") as file:
            try:
                file.write(str(key)+ "\n\n")
                file.write(str(all_chars)+ "\n\n")
                file.write(str(saved_chiper)+ "\n\n")
            except NameError:
                print("")

    elif userchoice == "4":
        break

    else:
        print("You need to choose between 1 and 4 ")