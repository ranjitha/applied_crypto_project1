#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <valarray>
#include <algorithm>
#include "Encryption.h"
using namespace std;

void longest(string& str, int M, vector<int>& lps)
{
	int length = 0;
	int i = 1;
	lps[0] = 0;
	while (i < M)
	{
		if (str[i] == str[length])
		{
			length++;
			lps[i] = length;
			i++;

		}
		else
		{
			if (length != 0)
			{
				length = lps[length - 1];
			}
			else
			{
				lps[i] = 0;
				i++;
			}
		}
	}
}

bool repeat(string& str)
{
	int n = str.size();
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		arr.push_back(0);
	}
	longest(str, n, arr);
	int len = arr[n - 1];
	if (len > 0 && (n % (n - len) == 0)) {
		return true;
	}
	else {
		return false;
	}
}

//checks if key is valid depending on repetitions
bool check_key_validity(string& key) {
	int n = key.size();
	for (int i = 0;i < min(24, n);i++) { //minimum of 24 or length
		string sub = key.substr(0, n - i);
		if (repeat(sub)) {
			string end = key.substr(n - i, n);
			if (i != 0) {
				for (int j = 0; j < end.size(); j++) {
					if (end[j] != sub[j]) {
						cout << end[j];
						return false;
					}

				}
			}
			return repeat(sub);
		}
	}
	return false;
}


//gives indicies from the alphabet for all the letters in the input string passed as arg
vector<int> get_number_for_letters(string& text) {
	string letters = " abcdefghijklmnopqrstuvwxyz";
	vector<int> number_array_for_text;

	for (int i = 0;i < text.size();i++) {
		bool done = false;
		int j = 0;
		while (done != true) {
			if (text[i] == letters[j]) {
				number_array_for_text.push_back(j);
				done = true;
			}
			else j++;
		}
	}
	return number_array_for_text;
}

int mod(int a, int b) { return (a % b + b) % b; }

string compare_cipher_with_plaintext(string& ciphertext, string& plaintext) {
	string letters = " abcdefghijklmnopqrstuvwxyz";
	vector <int> key_shifts;

	vector<int> cipherarr = get_number_for_letters(ciphertext);
	vector<int> plainarr = get_number_for_letters(plaintext);

	string empty = "";

	for (int i = 0; i < cipherarr.size(); i++) {
		int shift = mod((cipherarr[i] - plainarr[i]), 27);
		key_shifts.push_back(shift);
	}

	vector <char> key;
	
	for (int shift : key_shifts) {
		key.push_back(letters[shift]);
	}

	for (char charac : key) {
		empty += charac;
	}

	return empty;
}

bool guess(string ciphertext, string plaintext) {
	string key = compare_cipher_with_plaintext(ciphertext, plaintext);
	return check_key_validity(key);
}

vector<string> get_dict() {
	vector<string> candidates;
	candidates.push_back("gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee");
	candidates.push_back("intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor");
	candidates.push_back("frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p");
	candidates.push_back("distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg");
	candidates.push_back("undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis");
	return candidates;
}


bool sortbysec(const tuple<int, int>& a,
	const tuple<int, int>& b)
{
	return (get<1>(a) > get<1>(b));
}

int makeList() {
	vector<tuple<int, int> > v;
	v.push_back(make_tuple(10, 5));
	v.push_back(make_tuple(15, 20));
	v.push_back(make_tuple(3, 2));

	// Using sort() function to sort by 2nd element 
	// of tuple 
	sort(v.begin(), v.end(), sortbysec);
	cout << "Sorted Vector of Tuple on basis"
		" of Second element of tuple:\n";

	for (int i = 0; i < v.size(); i++)
		cout << get<0>(v[i]) << " "
		<< get<1>(v[i]) << " "
		<< "\n";
	return 0;
}






int main() {
	makeList();
	//Filled vector with different string candidates from dict 1
	vector<string> candidates = get_dict();
	vector<vector<int>> keys = GenerateKeyRange();
	vector<vector<int>> AllCombos;

	for (vector<int> key : keys) {
		for (int i = 0; i < key.size(); i++) {
			for (int j = 0; j < key.size(); j++) {
				AllCombos.push_back(keysToEncrypt(key.size(), key, i, j));
			}
		}
	}

	vector<string> ciphersOne;
	vector<string> ciphersTwo;
	vector<string> ciphersThree;
	vector<string> ciphersFour;
	vector<string> ciphersFive;
	
	for (vector<int> key : AllCombos) {
		string cipher1 = get_cipherTextTest(candidates[0], key);
		ciphersOne.push_back(cipher1);
		string cipher2 = get_cipherTextTest(candidates[1], key);
		ciphersTwo.push_back(cipher2);
		string cipher3 = get_cipherTextTest(candidates[2], key);
		ciphersThree.push_back(cipher3);
		string cipher4 = get_cipherTextTest(candidates[3], key);
		ciphersFour.push_back(cipher4);
		string cipher5 = get_cipherTextTest(candidates[4], key);
		ciphersFive.push_back(cipher5);
	}
	
	for (string cipher : ciphersOne) {
		for (int i = 0;i < 5;i++) {
			bool ans = guess(cipher, candidates[i]);
			if (ans == true) {
				cout << "The correct guess is: " << endl;
				cout << candidates[i];
				break;
			}
			else {
				cout << "Wrong Guess";
			}
		}
	}
		/*
		for (string candidate : candidates) {
			for (vector<int> key : AllCombos) {
				string cipher_input = get_cipherTextTest(candidate, key);
				//cipherTextList.push_back(cipher);
				for (int i = 0;i < 5;i++) {
					bool ans = guess(cipher_input, candidates[i]);
					if (ans == true) {
						cout << "The correct guess is: " << endl;
						cout << candidates[i];
						break;
					}
					else {
						cout << "Wrong Guess";
					}
				}
			}
			cout << "00000000000000000000000000000000000000000000000000000000000000000000000000000000000" << endl;
		}
		*/


		/*
		string cipher_input = get_cipherTextTest(candidates[0], AllCombos[500]);
		//cout << cipher_input << endl;
		//cout << "Please input ciphertext to be decrypted: ";
		//getline(cin, cipher_input);
		for (int i = 0;i < 5;i++) {
			bool ans = guess(cipher_input, candidates[i]);
			if (ans == true) {
				cout << "The correct guess is: " << endl;
				cout << candidates[i];
				break;
			}
			else
				cout << "Wrong Guess";
		}

		//string ciphered = get_cipherText();
		//int guess = decrypt(ciphered, candidates);
		*/
}




/*

int main() {
	//Filled vector with different string candidates from dict 1
	vector<string> candidates = get_dict();
	//string ciphered = get_cipherText();
	//cout << ciphered << endl;

	vector<vector<int>> keys = GenerateKeyRange();
	vector<vector<int>> AllCombos;

	for (vector<int> key : keys) {
		for (int i = 0; i < key.size(); i++) {
			for (int j = 0; j < key.size(); j++) {
				AllCombos.push_back(keysToEncrypt(key.size(), key, i, j));
			}
		}
	}



	vector<string> cipherTextList;
	for (string candidate : candidates) {
		for (vector<int> key : AllCombos) {
			cout << get_cipherTextTest(candidate, key) << endl;
			//cipherTextList.push_back(cipher);
			//if (cipherTextList.size() == 10) {
				//break;
			//}
		}
	}

	//for (string cipher : cipherTextList) {
		//cout << cipher << endl;
	//}
	
	vector<string> dict2words = getDict2();
	string text = randomText(dict2words);
	cout << text;


}
*/