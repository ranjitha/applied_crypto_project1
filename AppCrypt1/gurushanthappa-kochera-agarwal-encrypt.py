import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
DICT = ['awesomeness', 'hearkened', 'aloneness', 'beheld',
        'courtship', 'swoops', 'memphis', 'attentional',
        'pintsized', 'rustics', 'hermeneutics', 'dismissive',
        'delimiting', 'proposes', 'between', 'postilion',
        'repress', 'racecourse', 'matures', 'directions',
        'pressed', 'miserabilia', 'indelicacy', 'faultlessly',
        'chuted', 'shorelines', 'irony', 'intuitiveness',
        'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded',
        'combusting', 'unconvertible', 'successors', 'footfalls',
        'bursary', 'myrtle', 'photocompose']
MAX_PLAINTEXT_LEN = 500


class Crypto():
    def __init__(self, alphabet):
        self.alphabet = alphabet

        def create_default_scheduler(keylen):
            def default_scheduler(i):
                return i % keylen
            return default_scheduler

        self.create_default_scheduler = create_default_scheduler

    def gen_key(self, keylen):
        return [random.randint(0, len(self.alphabet)) for _ in range(keylen)]

    def encrypt(self, message, key, scheduler=None):
        encrypted = ''
        if scheduler is None:
            scheduler = self.create_default_scheduler(len(key))
        for i in range(len(message)):
            encrypted += self.shift(message[i], key[scheduler(i)])
        return encrypted

    def decrypt(self, ciphertext, key, scheduler=None):
        decrypted = ''
        if scheduler is None:
            scheduler = self.create_default_scheduler(len(key))
        for i in range(len(ciphertext)):
            decrypted += self.shift(ciphertext[i], 0-key[scheduler(i)])
        return decrypted

    def shift(self, letter, shift_amount):
        shift_amount = shift_amount % len(self.alphabet)
        new_index = (self.alphabet.index(letter) + shift_amount)
        return self.alphabet[new_index % len(self.alphabet)]


def gen_random_plaintext(dictionary, max_len):
    plaintext = ''
    while len(plaintext) < max_len:
        plaintext += random.choice(dictionary)
        plaintext += ' '
    return plaintext

def main():

    crypto = Crypto(ALPHABET)
    key = crypto.gen_key(keylen=10)
    print('key       : %s\n' % key)
    candidates = []
    candidates.append(
        "gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee");
    candidates.append(
        "intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor");
    candidates.append(
        "frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p");
    candidates.append(
        "distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg");
    candidates.append(
        "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis");
    print("Test 1 ciphertext generation")
    for i in range(5):
        print('candidate ' + str(i) + ': "%s\n' % candidates[i])
        print('ciphertext: "%s"\n\n' % crypto.encrypt(candidates[i], key))
    print("Test 2 ciphertext generator")
    for i in range(10):
        plaintext = gen_random_plaintext(DICT, MAX_PLAINTEXT_LEN)
        print('plaintext : "%s"\n' % plaintext)
        print('ciphertext: "%s"\n\n' % crypto.encrypt(plaintext, key))

main()

