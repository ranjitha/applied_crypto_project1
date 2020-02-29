#ifndef ENCRYPTION_H
#define ENCRYPTION_H
#include <string>
#include <vector>
using namespace std;

string request_plaintext();

vector<int> generateKey(int textLength);

int scheduleKey(int i, int t);

vector<int> keysToEncrypt(int t, vector<int> key);

string encrypt(string plaintext, vector<int>& keysToEncrypt);

string get_cipherText();

#endif