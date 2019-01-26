import common

def encrypt(plaintext=None,key=1):
    '''
    Encrypts a plaintext and returns the subsequent ciphertext
    Simple shift cipher (by integer key), if character isn't in alphabet then it is simply added
    to the ciphertext
    '''
    ciphertext = ""
    try:
        for character in plaintext.lower():
            if common.isSupportedCharacter(character):
                val = ord("a")+ (((ord(character)-ord("a"))+key)%26)
                ciphertext += chr(val)
            else:
                ciphertext += character
        return ciphertext
    except Exception as e:
        print(e,' --encrypt(CAESAR)')
    return None

def decrypt(ciphertext=None,key=1):
    '''
    Decrypts a ciphertext and returns the plaintext given a key
    '''
    plaintext = ""
    try:
        for character in ciphertext.lower():
            if common.isSupportedCharacter(character):
                val = ord('a')+(((ord(character)-ord('a'))-key)%26) #decrypt
                plaintext += chr(val)
            else:
                plaintext += character
        return plaintext
    except Exception as e:
        print(e,' --decrypt(CAESAR)')
    return None

def breakCaesar(ciphertext=None):
    '''
    Frequency analysis on ciphertext using chi-square distance
    Ideal for large body of text
    Returns key
    '''
    try:
        ciphertext_mod = common.removeNoise(ciphertext)
        return common.frequencyAnalysis(ciphertext_mod)
    except Exception as e:
        print(e,' --breakCaesar')
    return None

if __name__=="__main__":
    print("--caesar_cipher.py--")
