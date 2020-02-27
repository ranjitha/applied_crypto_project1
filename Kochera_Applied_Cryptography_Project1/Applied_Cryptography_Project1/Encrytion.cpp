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

vector<int> generateKey(size_t textLength) {
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
	for (int i = 1; i <= t; i++) {
		array.push_back(key[scheduleKey(i, t)])
	}
	return array;
}


string encrypt(const string& plaintext, const vector<int>& keysToEncrypt) {
	string enc = "";
	int count = 0;
	for (string letter : plaintext) {
		int num_letter = int(letter) + keysToEncrypt[count];
		if (num_letter > 122) {
			num_letter -= 26;
		}
		enc.append(char(num_letter))
		count += 1;
		if (count == keysToEncrypt.size()) {
			count = 0;
		}
	}
	return enc
}


int main() {
	string plain = request_plaintext();
	vector<int> key = generateKey(plain.size());
	vector<int> scheduled_keys = keysToEncrypt(key.size(), key);
	string enc = encrypt(plain, scheduled_keys)
}