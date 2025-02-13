letterBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Repeats the Key to Match Length of Message
def extendKey(message, key):
    fullKey = [] #Key Repeated for Length of Message
    keyIndex = 0 #Track Position in Key

    for char in message: #Iterate Through Message
        if char.upper() in letterBase:
            fullKey.append(key[keyIndex % len(key)])
            keyIndex += 1
        else:
            fullKey.append(char)
    return "".join(fullKey)

# Ensure Key Doesn't Contain Non-Letters
def cleanKey(key):
    key = key.upper() #Convert to Uppercase
    return "".join([char.upper() for char in key if char.upper() in letterBase]) #Remove Invalid Characters

#Encrypt Message Given Valid Key
def vigenereEncrypt(message, key):
    message = message.upper()
    key = extendKey(message, key) #Grab Full Length Key
    encryptedText = []

    #Iterate Through Message
    for i in range(len(message)):
        if message[i] in letterBase: #If Iterated Character is a Letter
            shift = letterBase.index(key[i])
            newIndex = (letterBase.index(message[i]) + shift) % 26
            encryptedText.append(letterBase[newIndex])
        else:
            encryptedText.append(message[i])
    return "".join(encryptedText)


def vigenereDecrypt(message, key):
    message = message.upper()
    key = extendKey(message, key)
    decryptedText = []
    for i in range(len(message)):
        if message[i] in letterBase:
            shift = letterBase.index(key[i])
            newIndex = (letterBase.index(message[i]) - shift) % 26
            decryptedText.append(letterBase[newIndex])
        else:
            decryptedText.append(message[i])
    return "".join(decryptedText)

def display_menu(options):
    for key, value in options.items():
        print(f"[{key}] {value}")

def get_user_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid, please try again.")

def encrypt_menu():
    message = input("Enter the message you'd like to encrypt: ")
    key = input("Enter the encryption key: ")
    cleanedKey = cleanKey(key)
    print("Encrypted Message:", vigenereEncrypt(message, cleanedKey))
    print ("Encryption Key: ", cleanedKey)

def decrypt_menu():
    message = input("Enter the message you'd like to decrypt: ")
    key = input("Enter the decryption key: ")
    cleanedKey = cleanKey(key)
    print("Decrypted Message:", vigenereDecrypt(message, cleanedKey))

def main():
    options = {"1": "Encrypt", "2": "Decrypt", "3": "Quit"}
    while True:
        print("\nWelcome to the Vigenère Cipher Encoder & Decoder!")
        display_menu(options)
        choice = get_user_choice("Enter your choice: ", options.keys())
        if choice == "1":
            encrypt_menu()
        elif choice == "2":
            decrypt_menu()
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
