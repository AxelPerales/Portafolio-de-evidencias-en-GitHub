def cifrar(mensaje, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ""
    
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symboIndex = SYMBOLS.find(symbol)
            translatedIndex = symboIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print("Mensaje cifrado: ",translated)

def descifrar(mensaje, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ""
    
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symboIndex = SYMBOLS.find(symbol)
            translatedIndex = symboIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print("Mensaje descifrado: ",translated)

def crackeo(mensaje):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    lista = list()

    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in mensaje:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol

        lista.append(translated)
    detectar_palabras(lista)

UPPERLETTERS = 'AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictEsp.txt', encoding="utf-8")

    spanishhWords = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        spanishhWords[word] = None
    dictionaryFile.close()
    return spanishhWords

SPANISH_WORDS = loadDictionary()

def removeNonLetters(mensaje):
    lettersOnly = []
    for symbol in mensaje:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def getSpanishCount(mensaje):
    mensaje = mensaje.upper()
    mensaje = removeNonLetters(mensaje)
    possibleWords = mensaje.split()

    if possibleWords == []:
        return 0.0
    
    matches = 0
    
    for word in possibleWords:
        if word in SPANISH_WORDS:
            matches +=1
    return float(matches)/len(possibleWords)
    
def detectar_palabras (lista, wordPercentaje=90, LetterPercentaje=100):
    for mensaje in lista:
        wordsMatch = getSpanishCount(mensaje) * 100 >= wordPercentaje
        numLetters = len(removeNonLetters(mensaje))
        messageLettersPercentaje = float(numLetters) /len(mensaje) * 100
        lettersMatch = messageLettersPercentaje >= LetterPercentaje
        if wordsMatch is True or lettersMatch is True:
            print("Posible mensaje : ", mensaje)
