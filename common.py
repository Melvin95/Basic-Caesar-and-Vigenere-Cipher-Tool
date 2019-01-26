#Standard distribtuion of frequencies of letters for the English language
std_freq = { "a" :  8.167, "b"  :   1.492, "c"  :   2.782,"d"  :   4.253,"e"  :   12.702,"f"  :   2.228,
    "g"  :   2.015,"h"  :   6.094,"i"  :   6.966,"j"  :   0.153,"k"  :   0.772,"l"  :   4.025,"m"  :  2.406,
    "n"  :   6.749, "o"  :   7.507,"p"  :   1.929,"q"  :   0.095,"r"  :   5.987,"s"  :   6.327,
    "t"  :   9.056,"u"  :   2.758, "v"  :   0.978,"w"  :   2.360,"x"  :   0.150,"y"  :   1.974, "z"  :  0.074  }
# https://commons.wikimedia.org/wiki/File:English_letter_frequency_(alphabetic).svg

#Returns contents of a file
def readFile(fileName):
    f = open(fileName,'r')
    message = f.read()
    f.close()
    return message

def getFrequencies(text=None):
    '''
    Returns an array with the frequencies of each letter in text
    '''
    arr = [0 for i in range(26)]
    try:
        #raw count
        for character in text.lower():
            arr[ord(character)-ord('a')] += 1
        #standerdize
        for i in range(len(arr)):
            arr[i] = (float(arr[i])/float(len(text)))*100
        return arr
    except Exception as e:
        print(e,' --getFrequencies')
        return None

def isSupportedCharacter(character):
    '''
    returns whether a character can be encrypted (a->z)
    '''
    try:
        if ord(character)>=ord('a') and ord(character)<=ord('z'):
            return True
        else:
            return False
    except Exception as e:
        print(e,' --isSupportedCharacter')

def chiSquareSummation(text=None):
    '''
    helper function for frequencyAnalysis
    '''
    try:
        import math
        observedFreq = getFrequencies(text)
        sumX = 0
        for i in range(26):
            sumX += math.pow((observedFreq[i]-(std_freq[chr(ord('a')+i)])),2)/(std_freq[chr(ord('a')+i)])
        return sumX
    except Exception as e:
        print(e, '--chiSquareSummation')
    return None

def frequencyAnalysis(ciphertext=None):
    '''
    X = sum( (Observed-Expected)**2/Expected)
    return min X
    '''
    try:
        import math
        import caesar_cipher as CAESAR
        minKey = -1 #most likely key
        minChiDist = math.inf
        #Get chi distances for all keys (0->25 shifts)
        for shift in range(26):
            #shift text (caesar DECRYPTION)
            shiftedText = CAESAR.decrypt(ciphertext,shift)
            chiDist = chiSquareSummation(shiftedText)
            if chiDist<minChiDist:
                minChiDist=chiDist
                minKey = shift
        return minKey
    except Exception as e:
        print(e)

    return None

def removeNoise(text):
    '''
    Removes text that isn't encrypted (non-english characters)
    Returns this text
    '''
    s = ""
    for character in text.lower():
        if isSupportedCharacter(character):
            s+=character
    return s

def getDistancesBetweenRepeatedChars(ciphertext):
    '''
    #find as many repeated set of characters (> length 2) in text as possible
    #then note the distances between them and return the distances (array)
    '''
    ciphertext = removeNoise(ciphertext.lower())
    distances = []
    i = 3
    while i<6 and len(distances)<5: #words of length 3->5 and matches found<5
        for j in range(len(ciphertext)-i):
            matchStartingIndex = ciphertext.find(ciphertext[j:j+i],j+i)
            if matchStartingIndex!=-1:
                distances.append(matchStartingIndex-j)
        i += 1
    return distances

def getFactors(numArray):
    '''
    Given an array of integers, determine and count all factors
    Return factors and counts
    '''
    factors = {}
    for num in numArray:
        #key length likely > 2
        #1 is a factor of every number
        #2 is a factor of every even number
        try:
            factors.__setitem__(num,factors[num]+1)
        except KeyError:
            factors.__setitem__(num,1)
        for i in range(4,int(num/2)+1):
            if num%i==0:
                try:
                    factors.__setitem__(i,factors[i]+1)
                except KeyError:
                    factors.__setitem__(i,1)
    return factors

def getMostCommonFactor(factorDictionary):
    '''
    Returns the key length (factor/dictionary key) with the maximum value (counts)
    '''
    maxKeyLen = 0
    maxKeyValue = 0
    for k in factorDictionary.keys():
        if factorDictionary[k]>maxKeyValue:
            maxKeyLen = k
            maxKeyValue = factorDictionary[k]
    return maxKeyLen
