import common

def encrypt(plaintext=None,key=None):
    '''
    Vigenere encryption
    '''
    try:
        ciphertext = ""
        keyIndex = 0 #which letter is to be used in the key
        key = key.lower()
        for character in plaintext.lower():
            if common.isSupportedCharacter(character):
                #reduce to range 0->26, shift, keep in range(%26), convert back to ord('a')->ord('z')
                val = ord('a')+(((ord(character)-ord('a'))+(ord(key[keyIndex])-ord('a')))%26)
                ciphertext += chr(val)
                keyIndex = (keyIndex+1)%len(key) #shift to next character, wrap around
            else:
                ciphertext += character
        return ciphertext
    except Exception as e:
        print(e,' --encrypt(VIGENERE)')

def decrypt(ciphertext=None,key=None):
    '''
    Vigenere decryption
    '''
    try:
        plaintext = ""
        keyIndex = 0
        key = key.lower()
        for character in ciphertext.lower():
            if common.isSupportedCharacter(character):
                val = ord('a')+(((ord(character)-ord('a'))-(ord(key[keyIndex])-ord('a')))%26)
                plaintext += chr(val)
                keyIndex = (keyIndex+1)%len(key)
            else:
                plaintext += character
        return plaintext
    except Exception as e:
        print(e,' --decrypt(VIGENERE)')

def estimateKeyLength(ciphertext):
    '''
    Repeated sets of characters and the distance between them gives
    an estimate of key length. Key length can't exceed this distance
    & is a factor of this distance
    '''
    try:
        distances = common.getDistancesBetweenRepeatedChars(ciphertext)
        factors = common.getFactors(distances)
        keyLength = common.getMostCommonFactor(factors)
        return keyLength
    except Exception as e:
        print(e,'--estimateKeyLength')

def getColumnText(ciphertext_mod,column_index,key_len):
    '''
    Returns
    column_index = kth
    return every kth letter in ciphertext_mod
    '''
    column_text = ""
    try:
        for i in range(column_index,1+len(ciphertext_mod)-key_len,key_len):
            column_text += ciphertext_mod[i]
        return column_text
    except Exception as e:
        print(e,' --getColumnText')
    return None

def breakVigenere(ciphertext):
    '''
    Breaks a vigenere encryption (no key given with ciphertext)
    Only suitable with large body of text since columns would have
    to be quite large for frequency analysis to be accurate
    Returns key
    '''
    try:
        #estimate number of characters in key
        keyLen = estimateKeyLength(ciphertext)
        #every kth letter is encoded with the same letter in the key
        #split ciphertext into k-columns, a column is essentially a
        #caesar cipher (same letter = same shift)
        #solve with freq analysis on limited 26 shifts (0->25)
        ciphertext_mod = common.removeNoise(ciphertext)
        key = ""
        for column_index in range(keyLen):
            column_text = getColumnText(ciphertext_mod,column_index,keyLen)
            column_key =  common.frequencyAnalysis(column_text) #0->25
            key += chr(ord('a')+column_key)
        return key
    except Exception as e:
        print(e,' --breakVignere')
    return None
