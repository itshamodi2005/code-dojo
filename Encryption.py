import random
import string
import json

all_chars = string.ascii_letters + string.digits + string.punctuation
all_chars = list(all_chars)

key = all_chars.copy()
random.shuffle(key)
saved_chiper =""

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

def save_key(filename, key, all_chars):

    data = {"key": key, "all_chars":all_chars}
    with open(filename,"w") as file:
        json.dump(data, file)

def load_key(filename):

    with open(filename, "r") as file:
        data = json.load(file)

    key = data["key"]
    all_chars = data["all_chars"]
    print(f"Key loaded from {filename}")
    return key, all_chars



while True:
    try:
        print("\n\n")
        print("*" * 100)
        print("\n\n(1) Encryption (2) Decryption (3) Save this key (4) Loud a key file (5) Exit")
        userchoice = (input("\nHow can i help...: "))
    except ValueError:
        print("You need to choose between 1 and 2 ")

    if userchoice == "1":
        saved_chiper = Encryption()

    elif userchoice == "2":
        text = Decryption()

    elif userchoice == "3":
        filename = input("Give your key file a name: ")
        if not filename.endswith(".json"):
            filename += ".json"
        save_key(filename, key, all_chars)

    elif userchoice == "4":
        filename = input("Filename to load key from: ")
        if not filename.endswith(".json"):
            filename += ".json"

        try:
            key, all_chars = load_key(filename)
        except FileNotFoundError:
            print(f"\nThere is no saved file with the name {filename} please try agian. ")
    
    elif userchoice == "5":
        break

    else:
        print("You need to choose between 1 and 5 ")