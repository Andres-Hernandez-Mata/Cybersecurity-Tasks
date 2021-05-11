"""
Uso: Spanish
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

UPPERLETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÄËÏÖÜ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():    
    dictionaryFile = open('dictEsp.txt', encoding="utf8")    
    spanishWords = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        spanishWords[word] = None
    dictionaryFile.close()
    return spanishWords

SPANISH_WORDS = loadDictionary()

def getSpanishCount(message):
    message = message.upper()    
    message = removeNonLetters(message)    
    possibleWords = message.split()    
    
    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:        
        if word in SPANISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isSpanish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).    
    wordsMatch = getSpanishCount(message) * 100 >= wordPercentage    
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
