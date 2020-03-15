import itertools
import time
from collections import Counter
from scipy import stats


def get_Dict2_Frequencies(dict2):
    list = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized',
            'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress',
            'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted',
            'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting',
            'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose']
    test_str = "".join(list)
    all_freq = Counter(test_str)

    freq_list=[]
    ordered_letters = ""
    for key in all_freq:
        all_freq[key] = (all_freq[key]/348) * 100

    sorted_freq = {}
    for w in sorted(all_freq, key=all_freq.get, reverse=True):
        sorted_freq[w] = all_freq[w]
        freq_list.append(all_freq[w])
        ordered_letters += w

    return (sorted_freq, ordered_letters, freq_list)

DICTIONARY2 = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose', ' ', '']

frequencies = get_Dict2_Frequencies(DICTIONARY2)
english_Letter_Freq = frequencies[0]
english_Letter_Freq['j'] = 0
english_Letter_Freq['q'] = 0
english_Letter_Freq['x'] = 0
ordered_freq_letters = frequencies[1] + "jqx"
LETTERS = ' abcdefghijklmnopqrstuvwxyz'
Top_Freq_Letter = 5
Max_KeyLen = 24


#No Longer Using
def index_of_coincidence(ciphertext, alpha):
    common = Counter(ciphertext)
    ioc = 0

    for index in alpha:
        ioc = ioc + (common[index] * (common[index] - 1))

    ioc = ioc / (len(ciphertext) *(len(ciphertext) - 1))
    return ioc

#No Longer Using
def friedman_test(ciphertext, alpha):
    l = 0

    n = len(ciphertext)
    i = index_of_coincidence(ciphertext, alpha)
    l = n * (0.027) / ((n - 1) * i  - 0.0385 * n + 0.0655)


    return l

def decrypt(key, message):
    translated = []
    offsets = [LETTERS.index(letter) for letter in key]
    for i in range(len(message)): # loop through each character in message
        symbol = message[i]
        indx = LETTERS.index(symbol)
        new_index = (indx - offsets[i % len(offsets)]) % len(LETTERS)
        translated.append(LETTERS[new_index])
    return "".join(translated)

# Returns a string of the alphabet letters arranged in order of most frequently occurring in the message parameter.
def Freq_Ord(message):
    char_freq = Counter(message.lower())

    freq_char = {}
    for letter in LETTERS:
        if char_freq[letter] not in freq_char:
            freq_char[char_freq[letter]] = [letter]
        else:
            freq_char[char_freq[letter]].append(letter)

    for freq in freq_char:
        freq_char[freq].sort(key=ordered_freq_letters.find, reverse=True)
        freq_char[freq] = ''.join(freq_char[freq])

    freq_pairs = list(freq_char.items())
    freq_pairs.sort(key=lambda x:x[0], reverse=True)
    freq_order = []

    for freqPair in freq_pairs:
        freq_order.append(freqPair[1])

    return ''.join(freq_order)

#Counts the most commone and uncommon letters that are found in message
def englishFreqMatchScore(message):
    freqOrder = Freq_Ord(message)

    matchScore = 0
    for commonLetter in ordered_freq_letters[:9]:
        if commonLetter in freqOrder[:9]:
            matchScore += 1

    for uncommonLetter in ordered_freq_letters[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore

# Goes through the message and finds any 3 to 5 letter sequences that are repeated.
def find_repeat_Spaces(message):
    seqSpacings = {}

    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []
                    seqSpacings[seq].append(i - seqStart)

    return seqSpacings


# Returns a list of useful factors of num. By "useful" we mean factors less than MAX_KEY_LENGTH + 1.
def getUsefulFactors(num):
     if num < 2:
         return []

     factors = []
     for i in range(2, Max_KeyLen + 1):
         if num % i == 0:
             factors.append(i)
             factors.append(int(num / i))

     return list(set(factors))


def get_common_factors(seq_factors):
     factor_counts = {}
     for seq in seq_factors:
         factorList = seq_factors[seq]
         for factor in factorList:
             if factor not in factor_counts:
                 factor_counts[factor] = 0
             factor_counts[factor] += 1
     factor_by_count = []
     for factor in factor_counts:
         if factor <= Max_KeyLen:
             factor_by_count.append( (factor, factor_counts[factor]) )

     factor_by_count.sort(key=lambda x:x[1], reverse=True)

     return factor_by_count

# Find out the sequences of 3 to 5 letters that occur multiple times
def kasiski_test(ciphertext):
     repeatedSeqSpacings = find_repeat_Spaces(ciphertext)
     seqFactors = {}
     for seq in repeatedSeqSpacings:
         seqFactors[seq] = []
         for spacing in repeatedSeqSpacings[seq]:
             seqFactors[seq].extend(getUsefulFactors(spacing))

     factors_by_count = get_common_factors(seqFactors)

     probable_keyLens = []

     for tup in factors_by_count:
         probable_keyLens.append(tup[0])
     return probable_keyLens


# Returns every Nth letter for each keyLength set of letters in text.
def get_n_jumped_crypt(n, keyLength, message):
     i = n - 1
     letters = []
     while i < len(message):
         letters.append(message[i])
         i += keyLength

     return ''.join(letters)

# Determine the most likely letters for each letter in the key.
def try_key_length(ciphertext, probable_keyLen,start_time):
     allFreqScores = []
     for nth in range(1, probable_keyLen + 1):
         nthLetters = get_n_jumped_crypt(nth, probable_keyLen, ciphertext)

         freqScores = []
         for possibleKey in LETTERS:
             decrypted = decrypt(possibleKey, nthLetters)
             keyAndFreqMatchTuple = (possibleKey, englishFreqMatchScore(decrypted))
             freqScores.append(keyAndFreqMatchTuple)
         # Sort by match score
         freqScores.sort(key=lambda x:x[1], reverse=True)
         allFreqScores.append(freqScores[:Top_Freq_Letter])


     # Brute Force with possible Key Length and likely letters
     for indexes in itertools.product(range(Top_Freq_Letter), repeat=probable_keyLen):
         possibleKey = ''
         for i in range(probable_keyLen):
             possibleKey += allFreqScores[i][indexes[i]][0]

         decrypted = decrypt(possibleKey, ciphertext)

         origCase = []
         for i in range(len(ciphertext)):
             origCase.append(decrypted[i].lower())
         
         decrypted = ''.join(origCase)
         
         list_of_words = decrypted.split(" ")
         if set(list_of_words) <= set(DICTIONARY2):
             return decrypted
         if(time.time() - start_time > 180):
             break
     return None


def hackVigenere(ciphertext, start_time):
     allLikelyKeyLengths = kasiski_test(ciphertext)

     for keyLength in allLikelyKeyLengths:
         hackedMessage = try_key_length(ciphertext, keyLength, start_time)
         if hackedMessage != None:
             break

         #Never going to get to this in 3 minutes
         # brute-force key lengths if none were found thro' kasiskiExamination
         #if hackedMessage == None:
             #for keyLength in range(1, Max_KeyLen + 1):
                 # no re-checking key lengths already tried from Kasiski
                 #if keyLength not in allLikelyKeyLengths:
                     #hackedMessage = try_key_length(ciphertext, keyLength, start_time)
                     #if (time.time() - start_time > 180):
                         #break
                     #if hackedMessage != None:
                         #break
     return hackedMessage

def main():
    ciphertext = input("Enter CipherText Here: ")
    start_time = time.time()
    hackedMessage = hackVigenere(ciphertext, start_time)
    if hackedMessage != None:
        print("This is the decrypted message: \n", hackedMessage)
        print("My program took", time.time() - start_time, "sec to run")
    else:
        print('Failed to hack encryption in time.')

if __name__ == '__main__':
     main()
