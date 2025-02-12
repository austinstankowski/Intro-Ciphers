letterBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cipherChar(char, shiftNumber):
    for i in range(len(letterBase)):
        if char == letterBase[i]:
            newLetter = letterBase[(i + shiftNumber) % 26]
            return newLetter

def cipherString(string, shiftNumber):
    updatedWords = []

    #Split Up Words
    words = string.split()

    for word in words:

        newChars = [] #Add Updated Characters to Temporary List

        #Iterate Through Characters in Order to Update Them
        for char in word:

            #Handles Characters
            if char.upper() in letterBase:
                char = char.upper()
                char = cipherChar(char, shiftNumber)
                newChars.append(char)

            #Don't Encrypt (Numbers, Symbols, etc)
            else:
                newChars.append(char)

        #Merge Updated Characters from newChars & Add to updatedWords
        updatedWords.append("".join(newChars))
    
    stringOut = " ".join(updatedWords)
    
    return stringOut

def bruteDecrypt(string):
    for i in range(26):
        decryptAttempt = cipherString(string, i)
        print(f"Shifted {26-i}: {decryptAttempt}")

def decrypt(string, shiftNumber):
    print(cipherString(string, 26-(shiftNumber % 26)))


def displayMenu(options):
    for key, value in options.items():
        print(f"[{key}] {value}")

def getUserChoice(prompt, validChoices):
    while True:
        choice = input(prompt).strip()
        if choice in validChoices:
            return choice
        else:
            print("Invalid, please try again.")

def encryptMenu():
    message = input("Enter the message you'd like to encrypt:")
    shift = int(input("Enter the shift amount:"))
    print("Encrypted Message: ", cipherString(message, shift))

def decryptMenu():
    decryptOptions = {"1": "Specific Decryption", "2": "Brute Force Decryption", "3": "Back"}

    while True:
        print("\n Decryption Options:")
        displayMenu(decryptOptions)
        
        choice = getUserChoice("Choose an Option:", decryptOptions.keys())

        if choice == "1":
            message = input("Enter the message you'd like to decrypt: ")
            shift = int(input("Enter the original shift amount: "))
            print("Decrypted Message:", cipherString(message, 26-(shift%26)))
        elif choice == "2":
            message = input("Enter the message you'd like to decrypt: ")
            bruteDecrypt(message)
        elif choice == "3":
            break


def main():
    options = {"1": "Encrypt", "2": "Decrypt", "3": "Quit"}
    while True:
        print("\nWelcome to the Caesar Cipher Encoder & Decoder!")
        displayMenu(options)
        choice = getUserChoice("Enter your choice: ", options.keys())

        if choice == "1":
            encryptMenu()
        elif choice == "2":
            decryptMenu()
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()