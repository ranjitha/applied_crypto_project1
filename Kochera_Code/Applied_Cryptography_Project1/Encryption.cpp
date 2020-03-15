#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

string request_plaintext() {
	string plainText;
	cout << "Please enter the PlainText Here: ";
	getline(cin, plainText);
	return plainText;
}

//Genereates Single Random Key of Random length
vector<int> generateKey(int textLength) {
	vector<int> key;
	int keySize = rand() % 24;
	
	for (int i = 0; i <= keySize; i++) {
		int num = rand() % 26;
		key.push_back(num);
	}

	return key;
}

//Generates Key List of all possible sizes
vector<vector<int>> GenerateKeyRange() {
	vector<vector<int>> keyList;

	for (int j = 1; j < 24; j++) {
		vector<int> key = {};
		for (int i = 0; i <= j; i++) {
			int num = rand() % 26;
			key.push_back(num);
		}
		keyList.push_back(key);
	}
	return keyList;
}


int scheduleKey(int i, int t, int num = 0, int skips = 0) {
	return (num + skips*i) % t;
}

//Organizes Key based on scheduler
vector<int> keysToEncrypt(int t, vector<int> key, int num = 0, int skips = 0) {
	vector<int> array;
	for (int i = 0; i < t; i++) {
		int key_sched = scheduleKey(i, t, num, skips);
		array.push_back(key[key_sched]);
	}
	return array;
}


string encrypt(string plaintext,vector<int> key, map<int, char> letterDict, string letters) {
	string enc = "";
	int count = 0;
	int count_plain = 0;
	while (count_plain < plaintext.size()) {
		char letter = plaintext[count_plain];
		int curr_num = letters.find(letter);
		int num_letter_crypt = curr_num + key[count];
		if (num_letter_crypt > 26) {
			num_letter_crypt = (num_letter_crypt % 26) - 1;
		}
		enc += letterDict[num_letter_crypt];
		count += 1;
		if (count == key.size()) {
			count = 0;
		}
		count_plain += 1;
	}
	return enc;
}

//Puts words from dict2 into a list
vector<string> getDict2() {
	ifstream file;
	file.open("dict2.txt");
	string word;
	vector<string> list_words;
	while (file >> word) {
		list_words.push_back(word);
	}
	return list_words;
}

//Returns random text for testing from dict2
string randomText(vector<string> dict2) {
	string plainText;
	while (plainText.size() < 500) {
		int wordIndex = rand() % 40;
		plainText += dict2[wordIndex];
		plainText += " ";
	}
	return plainText;
}

string get_cipherText() {
	map<int, char> letter_dict;
	string letters = " abcdefghijklmnopqrstuvwxyz";
	for (int i = 0; i <= 26; i++) {
		letter_dict[i] = char(letters[i]);
	}
	string plain = request_plaintext();
	vector<int> key = generateKey(plain.size());

	vector<int> scheduled_keys = keysToEncrypt(key.size(), key);

	string enc = encrypt(plain, key, letter_dict, letters);
	return enc;
}

string get_cipherTextTest(string plain, vector<int> key) {
	map<int, char> letter_dict;
	string letters = " abcdefghijklmnopqrstuvwxyz";
	for (int i = 0; i <= 26; i++) {
		letter_dict[i] = char(letters[i]);
	}

	string enc = encrypt(plain, key, letter_dict, letters);
	return enc;
}
