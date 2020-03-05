import string

def computeLPSArray(string, M, lps):
    length = 0
    i = 1
    lps[0] = 0
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1


# returns true if string is repetition of one of its substrings; else return false.
def isRepeat(string):
    n = len(string)
    lps = [0] * n
    computeLPSArray(string, n, lps)
    length = lps[n-1]
    if length > 0 and n%(n-length) == 0:
        return True
    else:
        return False

# checks if key is valid depending on repititions
def check_key_validity(key):
    #done = False
    n = len(key)
    for i in range(min(24, n)): #minimum of 24 or length
        if isRepeat(key[:n-i]):
            #print(key[:n-i])
            #sneed to fix
            return isRepeat(key[:n-i])
    return False
#print(check_key_validity("ae gmae gmae gmae"))


# gives indicies from the alphabet for all the letters in the input string passed as arg
# for example, given "abc apple", it returns [1,2,3,0,1,16,16,12]
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


# compares ciphertext with plaintext and returns the key
def compare_cipher_with_plaintext(ciphertext, plaintext):
    letters = " abcdefghijklmnopqrstuvwxyz"
    key_shifts = []
    
    ciphertext_array = get_number_for_letters(ciphertext)
    plaintext_array = get_number_for_letters(plaintext)
    
    for i in range(len(ciphertext_array)):
        shift = (ciphertext_array[i] - plaintext_array[i]) % 27
        key_shifts.append(shift)
    
    key = [letters[shift] for shift in key_shifts]

    return ("".join(key))
#compare_cipher_with_plaintext("jeatmwjremtyrletjd", "i am very stressed")


def guess(ciphertext, plaintext):
    key = compare_cipher_with_plaintext(ciphertext, plaintext)
    return check_key_validity(key)


if __name__ == '__main__':
    #five_plaintext_file = open("plaintext_dictionary_test1.txt", "r")
    #word_dictionary_file = open("word_dictionary_test2.txt", "r")
    #five_plaintext_file_content = five_plaintext_file.read()
    #word_dictionary_file_content = word_dictionary_file.read()
    dict = {
    0: "gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee",
    1: "intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor",
    2: "frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p",
    3: "distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg",
    4: "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"}
    cipher_input = input("Please input ciphertext to be decrypted: ")
    for i in range(5):
        bool = guess(cipher_input, dict[i])
        #print(bool)
        if bool is True:
            print("The correct guess is: ", dict[i])
        else:
            print("Wrong guess: ", dict[i])

