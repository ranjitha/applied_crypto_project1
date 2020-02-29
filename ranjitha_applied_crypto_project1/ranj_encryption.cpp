#include <iostream>
#include <string>
#include <vector>

using namespace std;
#pragma GCC diagnostic ignored "-Wc++11-extensions"

const string requestPlaintext(){
    string plainText;
    cout << "Enter plaintext here: ";
    cin >> plainText;
    return plainText;
}

string encrypt(string plainText, vector<int> key){
    string ans = " ";
    for(int i:key){
        cout<<i<<", ";
        ans += ('a'+i);
    }
    return ans;
}

int generateIndex(int i, int t){
    return 1+((i*i) % t);
}

vector<int> generateKey(int messageLength){
    vector<int> k;
    int randomValue = rand()%23 + 1;
    for(int i=0; i<messageLength; i++){
        k.push_back(generateIndex(i, randomValue));
    }
    return k;
}


int main(){
    string message = requestPlaintext();
    vector<int> keys;
    keys = generateKey(message.size());
    string cipher = encrypt(message, keys);
    cout<<cipher<<"\n";
}
