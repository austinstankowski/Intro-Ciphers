letterBase = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


'''
[cipherChar]

Inputs:
char = Capital Letter
shiftNumber = Positive Integer

return: Capital Letter
'''

def cipherChar(char, shiftNumber):
    for i in range(len(letterBase)):
        if char == letterBase[i]:
            newLetter = letterBase[(i + shiftNumber) % 25]
    return newLetter