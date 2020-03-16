import itertools
import time
from collections import Counter
from scipy import stats


def test1_decryption(cipher_input): # Input ciphertext here to be decrypted

    def get_longest_common_substring(string, m, lcs):
        length = 0
        i = 1
        lcs[0] = 0
        while i < m:
            if string[i] == string[length]:
                length += 1
                lcs[i] = length
                i += 1
            else:
                if length != 0:
                    length = lcs[length-1]
                else:
                    lcs[i] = 0
                    i += 1
    
    
    # Return true if string is repetition of one of its substrings; else return false.
    def isRepeat(string):
        n = len(string)
        lcs = [0] * n
        get_longest_common_substring(string, n, lcs)
        length = lcs[n-1]
        if length > 0 and n%(n-length) == 0:
            return True
        else:
            return False
    
    
    # Check if key is valid depending on repititions
    def check_key_validity(key):
        n = len(key)
        for i in range(min(24, n)):
            if isRepeat(key[:n-i]):
                if i!=0 and key[n-i:] not in key:
                    return False
                else:
                    return isRepeat(key[:n-i])
        return False
    
    
    # Give indicies from the alphabet for all the letters in the input string passed as arg
    # For example, given "abc apple", it returns [1,2,3,0,1,16,16,12]
    def get_number_for_letters(text):
        letters = " abcdefghijklmnopqrstuvwxyz"
        number_array_for_text = []
        
        for i in range(len(text)):
            done = False
            j = 0
            while not done:
                if text[i] == letters[j]:
                    number_array_for_text.append(j)
                    done = True
                else:
                    j+=1
        
        return number_array_for_text
    
    
    # Compare ciphertext with plaintext and return the key
    def compare_cipher_with_plaintext(ciphertext, plaintext):
        letters = " abcdefghijklmnopqrstuvwxyz"
        key_shifts = []
        
        ciphertext_array = get_number_for_letters(ciphertext)
        plaintext_array = get_number_for_letters(plaintext)
        
        for i in range(len(ciphertext_array)):
            shift = (ciphertext_array[i] - plaintext_array[i]) % 27
            key_shifts.append(shift)
        
        key = []
        for shift in key_shifts:
            key += letters[shift]
    
        return ("".join(key))
    
    
    def guess(ciphertext, plaintext):
        key = compare_cipher_with_plaintext(ciphertext, plaintext)
        return check_key_validity(key)
    
    
    def test1(cipher_input):
        dict = {
        0: "gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee",
        1: "intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor",
        2: "frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p",
        3: "distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg",
        4: "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"}
        for i in range(5):
            bool = guess(cipher_input, dict[i])
            if bool is True:
                print("This is the decrypted message: \n", dict[i])
                return dict[i]
        return None
    
    return test1(cipher_input)
    #end of test 1

def test2_decryption(ciphertext, start_time): # Pass inputed ciphertext here to be decrypted if test1 doesnt find a valid decryption

    # Get frequency of all the letters from the given dictionary
    def get_dictionary2_frequencies(dict2):
        list = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose']
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
    
    frequencies = get_dictionary2_frequencies(DICTIONARY2)
    english_Letter_Freq = frequencies[0]
    english_Letter_Freq['j'] = 0
    english_Letter_Freq['q'] = 0
    english_Letter_Freq['x'] = 0
    ordered_freq_letters = frequencies[1] + "jqx"
    LETTERS = ' abcdefghijklmnopqrstuvwxyz'
    Top_Freq_Letter = 5
    max_key_length = 24
    
    
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
    
    
    # Decrypt message using key passed as argument
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
    def frequency_order(message):
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
        freq_order = frequency_order(message)
    
        matchScore = 0
        for commonLetter in ordered_freq_letters[:9]:
            if commonLetter in freq_order[:9]:
                matchScore += 1
    
        for uncommonLetter in ordered_freq_letters[-6:]:
            if uncommonLetter in freq_order[-6:]:
                matchScore += 1
    
        return matchScore
    
    
    # Goes through the message and finds any 3 to 5 letter sequences that are repeated.
    def find_repeated_spaces(message):
        seq_spacings = {}
    
        for seqLen in range(3, 6):
            for seqStart in range(len(message) - seqLen):
                seq = message[seqStart:seqStart + seqLen]
                for i in range(seqStart + seqLen, len(message) - seqLen):
                    if message[i:i + seqLen] == seq:
                        if seq not in seq_spacings:
                            seq_spacings[seq] = []
                        seq_spacings[seq].append(i - seqStart)
    
        return seq_spacings
    
    
    # Returns a list of useful factors of num. By "useful" we mean factors less than MAX_KEY_LENGTH + 1.
    def get_useful_factors(num):
        if num < 2:
            return []
    
        factors = []
        for i in range(2, max_key_length + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(int(num / i))
    
        return list(set(factors))


    # Give sorted list of common factors in descending order of frequency of occurence
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
            if factor <= max_key_length:
                factor_by_count.append( (factor, factor_counts[factor]) )
    
        factor_by_count.sort(key=lambda x:x[1], reverse=True)
    
        return factor_by_count
    
    
    # Find out the sequences of 3 to 5 letters that occur multiple times
    def kasiski_test(ciphertext):
        repeated_seq_spacings = find_repeated_spaces(ciphertext)
        sequence_factors = {}
        for seq in repeated_seq_spacings:
            sequence_factors[seq] = []
            for spacing in repeated_seq_spacings[seq]:
                sequence_factors[seq].extend(get_useful_factors(spacing))
    
        factors_by_count = get_common_factors(sequence_factors)
    
        probable_key_lengths = []
    
        for tup in factors_by_count:
            probable_key_lengths.append(tup[0])
        return probable_key_lengths
    
    
    # Returns every Nth letter for each keyLength set of letters in text
    def get_n_jumped_crypt(n, keyLength, message):
        i = n - 1
        letters = []
        while i < len(message):
            letters.append(message[i])
            i += keyLength
    
        return ''.join(letters)
    
    
    # Determine the most likely letters for each letter in the key
    def try_key_length(ciphertext, probable_keyLen,start_time):
        all_freq_scores = []
        for nth in range(1, probable_keyLen + 1):
            nthLetters = get_n_jumped_crypt(nth, probable_keyLen, ciphertext)
    
            freq_scores = []
            for possibleKey in LETTERS:
                decrypted = decrypt(possibleKey, nthLetters)
                keyAndFreqMatchTuple = (possibleKey, englishFreqMatchScore(decrypted))
                freq_scores.append(keyAndFreqMatchTuple)
            # Sort by match score
            freq_scores.sort(key=lambda x:x[1], reverse=True)
            all_freq_scores.append(freq_scores[:Top_Freq_Letter])
    
        # Brute Force with possible Key Length and likely letters
        for indexes in itertools.product(range(Top_Freq_Letter), repeat=probable_keyLen):
            possibleKey = ''
            for i in range(probable_keyLen):
                possibleKey += all_freq_scores[i][indexes[i]][0]
    
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
    
    
    # Give all possible decrypted messages
    def poly_substitution_decrypt(ciphertext, start_time):
        all_likely_key_lengths = kasiski_test(ciphertext)
    
        for keyLength in all_likely_key_lengths:
            potential_decrypted_message = try_key_length(ciphertext, keyLength, start_time)
            if potential_decrypted_message != None:
                break
    
            #Never going to get to this in 3 minutes
            # brute-force key lengths if none were found thro' kasiskiExamination
            #if potential_decrypted_message == None:
                #for keyLength in range(1, max_key_length + 1):
                    # no re-checking key lengths already tried from Kasiski
                    #if keyLength not in all_likely_key_lengths:
                        #potential_decrypted_message = try_key_length(ciphertext, keyLength, start_time)
                        #if (time.time() - start_time > 180):
                            #break
                        #if potential_decrypted_message != None:
                            #break
        return potential_decrypted_message
    
    
    def main(ciphertext, start_time):
        potential_decrypted_message = poly_substitution_decrypt(ciphertext, start_time)
        if potential_decrypted_message != None:
            print("This is the decrypted message: \n", potential_decrypted_message)
            print("The program took", time.time() - start_time, "sec to run")
        else:
            print('Failed to hack encryption in time.')
    

    main(ciphertext, start_time)
    #end of test 1


def main():
    ciphertext = input("Enter CipherText Here: ")
    start_time = time.time()
    if(len(ciphertext) == 500):
        test1 = test1_decryption(ciphertext)
    else:
        test1 = None
    if(test1 == None):
        test2 = test2_decryption(ciphertext, start_time)


if __name__ == '__main__':
    main()
     
