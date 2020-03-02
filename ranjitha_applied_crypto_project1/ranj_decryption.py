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
        False

def compare_cipher_with_plaintext(ciphertext, plaintext):
    # ord is a function in python which returns the ascii value of the character
    # the following two lines of code gives an array of ascii values for both plaintext and ciphertext
    ords_plaintext = [ord(c) for c in plaintext]
    ords_ciphertext = [ord(c) for c in ciphertext]
    key_shifts = []
    for i in ords_plaintext:
        if i == 32:
            
        key_shifts = key_shifts.append(ords_ciphertext[i] - ords_plaintext[i]

if __name__ == "__main__":
    pass
    five_plaintext_file = open("plaintext_dictionary_test1.txt", "r")
    word_dictionary_file = open("word_dictionary_test2.txt", "r")
    five_plaintext_file_content = five_plaintext_file.read()
    word_dictionary_file_content = word_dictionary_file.read()
    

'''
def limits_correction(character, distance, start, end):
    char = character
    if char >= start and char < end:
        if char + distance >= end:
            char = char + distance - 26
        else:
            char = char + distance
    return char

def modify_string(string, distance):
    # string here is the plaintext that we need to shift
    ords = [ord(c) for c in string]

    corrected_distance = 0
    if distance > 26:
        corrected_distance = distance % 26
    elif distance > 0 and distance <= 26:
        corrected_distance = distance

    lower_start = 97
    lower_end = lower_start + 26

    shifted_string = []

    for char in ords:
        if char >= lower_start and char < lower_end:
            char = limits_correction(char, corrected_distance, lower_start, lower_end)
        shifted_string.append(chr(char))
    
    print(''.join(shifted_string))
    return ''.join(shifted_string)

modify_string("abc", 28)
'''

    
    

