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

            #Handles Symbols & Numbers
            else:
                newChars.append(char)

        #Merge Updated Characters from newChars & Add to updatedWords
        updatedWords.append("".join(newChars))
    
    stringOut = " ".join(updatedWords)
    
    return stringOut



def bruteDecrypt(string):
    for i in range(26):
        print(cipherString(string, i))

def decrypt(string, shiftNumber):
    print(cipherString(string, 26-shiftNumber))




