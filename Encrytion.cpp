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

const vector<int> generateKey(size_t textLength) {
	int maxLength = 24;
	if (textLength < maxLength) {
		maxLength = textLength;
	}

	vector<int> key;
	int keySize = rand() % maxLength + 1;
	
	for (int i = 0; i <= keySize; i++) {
		int num = rand() % 26;
		key.push_back(num);
	}

	return key;
}

int schedule(int textLength, int keyLength, int currentIndex) {

}

string encrypt(const string& plaintext, const vector<int>& key) {

}


int main() {
	string plainText = request_plaintext();
	vector<int> key = generateKey(plainText.size());
	string cipherText = encrypt(plainText, key);
}