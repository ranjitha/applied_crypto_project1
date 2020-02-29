#include <iostream>
#include <string>
#include <vector>
using namespace std;

string request_plaintext() {
	string plainText;
	cout << "Please enter the PlainText Here: ";
	cin >> plainText;
	return plainText;
}

vector<int> generateKey(int textLength) {
	int maxLength = 24;
	if (textLength < maxLength) {
		maxLength = textLength;
	}

	vector<int> key;
	int keySize = rand() % maxLength + 10;
	
	for (int i = 0; i <= keySize; i++) {
		int num = rand() % 26;
		key.push_back(num);
	}

	return key;
}


int scheduleKey(int i, int t) {
	return 1 + (i % t);
}

vector<int> keysToEncrypt(int t, vector<int> key) {
	vector<int> array;
	for (int i = 0; i < t; i++) {
		int key_sched = scheduleKey(i, t-1);
		array.push_back(key[key_sched]);
	}
	return array;
}


string encrypt(string plaintext,vector<int>& keysToEncrypt) {
	string enc = "";
	int count = 0;
	for (char letter : plaintext) {
		if (int(letter) == 36) {
			//How to Encode Spaces
		}
		int num_letter = letter + keysToEncrypt[count];
		if (num_letter > 122) {
			num_letter -= 26;
		}
		enc += char(num_letter);
		count += 1;
		if (count == keysToEncrypt.size()) {
			count = 0;
		}
	}
	return enc;
}


string get_cipherText() {
	string plain = request_plaintext();
	vector<int> key = generateKey(plain.size());
	vector<int> scheduled_keys = keysToEncrypt(key.size(), key);
	string enc = encrypt(plain, scheduled_keys);
	return enc;
}
