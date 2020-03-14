import itertools

englishLetterFreq = {'e': 12.02, 't': 9.1, 'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95, 's': 6.28, 'r': 6.02, 'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88, 'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11, 'w': 2.09, 'g': 2.03, 'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11, 'j': 0.10, 'z': 0.07}
ETAOIN = 'etaoinsrhdlucmfywgpbvkxqjz'
LETTERS = ' abcdefghijklmnopqrstuvwxyz'
NUM_MOST_FREQ_LETTERS = 5 # attempts this many letters per subkey
MAX_KEY_LENGTH = 12 # will not attempt keys longer than this
DICTIONARY2 = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose', ' ', '']


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string
    offsets = as_list(key)

    for i in range(len(message)): # loop through each character in message
        symbol = message[i]
        indx = LETTERS.index(symbol)
        if mode == 'encrypt':
            new_index = (indx + offsets[i % len(offsets)]) % len(LETTERS)
        else:
            new_index = (indx - offsets[i % len(offsets)]) % len(LETTERS)
        translated.append(LETTERS[new_index])
    return "".join(translated)
            # offsets = [2, 9, 5]
            # ptxt =     a  b  c  g  a
            # ctxt =     c  k  h  i  j


def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, ' ':0}
    for letter in message.lower():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount


def getItemAtIndexZero(x):
    return x[0]


def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most frequently occurring in the message parameter.
    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s) with that frequency
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # fourth, convert the freqToLetter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def englishFreqMatchScore(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # Find how many matches for the six most common letters there are.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # Find how many matches for the six least common letters there are.
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore


def findRepeatSequencesSpacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).
    # Use a regular expression to remove non-letters from the message.
    #message = NONLETTERS_PATTERN.sub('', message.lower())

    # Compile a list of seqLen-letter sequences found in the message.
    seqSpacings = {}  # keys are sequences, values are list of int spacings

    for seqLen in range(3, 20):
        for seqStart in range(len(message) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = message[seqStart:seqStart + seqLen]
            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []  # initialize blank list
                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings


def getUsefulFactors(num):
     # Returns a list of useful factors of num. By "useful" we mean factors
     # less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
     # returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]
     if num < 2:
         return [] # numbers less than 2 have no useful factors
     factors = [] # the list of factors found
     # When finding factors, you only need to check the integers up to
     # MAX_KEY_LENGTH.
     for i in range(2, MAX_KEY_LENGTH + 1): # don't test 1
         if num % i == 0:
             factors.append(i)
             factors.append(int(num / i))
     if 1 in factors:
         factors.remove(1)
     return list(set(factors))


def getItemAtIndexOne(x):
     return x[1]


def getMostCommonFactors(seqFactors):
     # First, get a count of how many times a factor occurs in seqFactors.
     factorCounts = {} # key is a factor, value is how often if occurs
     # seqFactors keys are sequences, values are lists of factors of the
     # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
     # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
     for seq in seqFactors:
         factorList = seqFactors[seq]
         for factor in factorList:
             if factor not in factorCounts:
                 factorCounts[factor] = 0
             factorCounts[factor] += 1
     # Second, put the factor and its count into a tuple, and make a list
     # of these tuples so we can sort them.
     factorsByCount = []
     for factor in factorCounts:
         # exclude factors larger than MAX_KEY_LENGTH
         if factor <= MAX_KEY_LENGTH:
             # factorsByCount is a list of tuples: (factor, factorCount)
             # factorsByCount has a value like: [(3, 497), (2, 487), ...]
             factorsByCount.append( (factor, factorCounts[factor]) )
     # Sort the list by the factor count.
     factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

     return factorsByCount


def kasiskiExamination(ciphertext):
     # Find out the sequences of 3 to 5 letters that occur multiple times
     # in the ciphertext. repeatedSeqSpacings has a value like:
     # {'EXG': [192], 'NAF': [339, 972, 633], ... }
     repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)
     # See getMostCommonFactors() for a description of seqFactors.
     seqFactors = {}
     for seq in repeatedSeqSpacings:
         seqFactors[seq] = []
         for spacing in repeatedSeqSpacings[seq]:
             seqFactors[seq].extend(getUsefulFactors(spacing))
     # See getMostCommonFactors() for a description of factorsByCount.
     factorsByCount = getMostCommonFactors(seqFactors)
     # Now we extract the factor counts from factorsByCount and
     # put them in allLikelyKeyLengths so that they are easier to
     # use later.
     allLikelyKeyLengths = []
     for twoIntTuple in factorsByCount:
         allLikelyKeyLengths.append(twoIntTuple[0])
     return allLikelyKeyLengths



def getNthSubkeysLetters(n, keyLength, message):
     # Returns every Nth letter for each keyLength set of letters in text.
     # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
     #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
     #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
     #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

     # Use a regular expression to remove non-letters from the message.
     #message = NONLETTERS_PATTERN.sub('', message)
     i = n - 1
     letters = []
     while i < len(message):
         letters.append(message[i])
         i += keyLength

     return ''.join(letters)


def as_list(key):
     return [LETTERS.index(letter) for letter in key]


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
     # Determine the most likely letters for each letter in the key.
     # allFreqScores is a list of mostLikelyKeyLength number of lists.
     # These inner lists are the freqScores lists.
     allFreqScores = []
     for nth in range(1, mostLikelyKeyLength + 1):
         nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertext)
         # freqScores is a list of tuples like: [(<letter>, <Eng. Freq. match score>), ... ]

         freqScores = []
         for possibleKey in LETTERS:
             decryptedText = decryptMessage(possibleKey, nthLetters)
             keyAndFreqMatchTuple = (possibleKey, englishFreqMatchScore(decryptedText))
             freqScores.append(keyAndFreqMatchTuple)
         # Sort by match score
         freqScores.sort(key=getItemAtIndexOne, reverse=True)
         allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])


     # Try every combination of the most likely letters for each position
     # in the key.
     for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
         # Create a possible key from the letters in allFreqScores
         possibleKey = ''
         for i in range(mostLikelyKeyLength):
             possibleKey += allFreqScores[i][indexes[i]][0]

         decryptedText = decryptMessage(possibleKey, ciphertext)
         #print(len(decryptedText), len(ciphertext))
         # Set the hacked ciphertext to the original casing.
         origCase = []
         for i in range(len(ciphertext)):
             origCase.append(decryptedText[i].lower())
         
         decryptedText = ''.join(origCase)
         
         list_of_words = decryptedText.split(" ")
         if set(list_of_words) <= set(DICTIONARY2):
             return decryptedText
     return None



def hackVigenere(ciphertext):
     # use kasiskixamination to figure out what the length of the ciphertext's encryption key is.
     allLikelyKeyLengths = kasiskiExamination(ciphertext)
     for keyLength in allLikelyKeyLengths:
         hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
         if hackedMessage != None:
             break

     # brute-force key lengths if none were found thro' kasiskiExamination
     if hackedMessage == None:
         for keyLength in range(1, MAX_KEY_LENGTH + 1):
             # no re-checking key lengths already tried from Kasiski
             if keyLength not in allLikelyKeyLengths:
                 hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                 if hackedMessage != None:
                     break
     return hackedMessage


def main():
     ciphertext = input("Enter CipherText Here: ")
     hackedMessage = hackVigenere(ciphertext)
     if hackedMessage != None:
         print("This is the decrypted message: \n", hackedMessage)
     else:
         print('Failed to hack encryption.')

if __name__ == '__main__':
     main()
