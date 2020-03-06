#ifndef ENCRYPTION_H
#define ENCRYPTION_H
#include <string>
#include <vector>
#include <map>
using namespace std;

string request_plaintext();

vector<int> generateKey(int textLength);

int scheduleKey(int i, int t, int num, int skips);

vector<int> keysToEncrypt(int t, vector<int> key, int num = 0, int skips = 0);

string encrypt(string plaintext, vector<int> key, map<int, char> letterDict, string letters);

string get_cipherText();

vector<string> getDict2();

string randomText(vector<string> dict2);

vector<vector<int>> GenerateKeyRange();

string get_cipherTextTest(string plain, vector<int> key);

#endif