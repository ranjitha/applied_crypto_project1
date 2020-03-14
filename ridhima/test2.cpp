#include <iostream> 
#include <cstring>
#include <string>
#include <vector>
#include <map> 
using namespace std;

map <string,vector<int>> findRepeatSequences(string message) {
	// remove non letters and spaces from the message?
	map <string, vector <int> > seqSpace; //keys are sequences, values are list of spaces between them 
	map <string,vector<int>>::iterator it;
	string sequence ="";
	for(int len=3;len<6;len++) { //for all lengths between 3 and 5
		for(int start=0; start<strlen(message); start++) {
			sequence=message.substr(start,start+len); //find a sequence of length 
			for(int i=start+len;i<strlen(message)-len;i++) {
				if(message.substr(i,i+len)==sequence) {  //compare it with similar sequence in msg
					it=seqSpace.find(sequence); //is it there in the map from befor?
					if(it==seqSpace.end()) {
						seqSpace.insert({sequence,[]});
					}
				seqSpace[sequence].push_back(i-start); //append the space gap between original seq and repeated seq
				}
			}
		}
	}
	return seqSpace;
}

vector <int> getUsefulFactors(int num) {
	//returns a list of factors of a number. each factor should be at max 24
	vector <int> factors;
	if num<2 return factors;
	for(int i=2;i<25;i++){
		if(num%i==0 && int(num/i)!=1){ //no point using 1 as a factor
			factors.push_back(i);
			factors.push_back(int(num/i));
		}
	}

	sort(factors.begin(), factors.end());
	unique(factors.begin(),factors.end()); //unique factors only to avoid repeats
	return factors;
}

vector <tuple<int,int>> MostCommonfactors(map <string,vector<int>> seqfactors) {
	map<int,int> factorcounts;
	map<int,int> iterator it2 = factorcounts.begin();
	map <string, vector<int>> iterator it1 = seqfactors.begin();
	while(it1!=seqfactors.end()){
		vector<int> factorList=it1->second;
		for(int factor=0;factor<factorList.size();factor++) {
			while(factorList[factor]!=it2->first){
				it2++;
			}
			if(it2==factorcounts.end()) {
				elem = factorList[factor];
				factorcounts[elem]=0;
			}
			else {
				elem = factorList[factor];
				factorcounts[elem]+=1;
			}
			
		}
		it1++;
	}
	vector<tuple<int,int>> factorsByCount;
	it2=factorcounts.begin();
	while(it2!=factorcounts.end()) {
		if(it2->first <= 24) {
			tuple <int,int> foo = {it2->first,it2->second};
			factorsByCount.push_back(foo);
		}
	}
	// sort the list of tuples based on the 2nd element in descending order(higher count means higher prob of it being the key length)
	tuple<int,int> tuplefirst;
	int max = get<1> (tuplefirst);
	for(tuple<int,int> tup : list) {
		if(get<1>(tup) > max):

	}
}

vector <int> kasiski(string ciphertext){
	repeatSpacings = findRepeatSequences(ciphertext); 
	map <string,vector<int>> seqfactors; //factors of each number in the sequences list
	map <string, vector<int>> iterator it = repeatSpacings.begin();
	vector <int> listFactors;
	vector <int> mostfrequent;
	while(it!=repeatSpacings.end()) {
		for(int j=0;j< it->second.size();j++) {
			listFactors = getUsefulFactors(it->second[j]);
			seqfactors[it->first]=listFactors;
		}
		it++;
	}
	vector<tuple<int,int>> mostfrequent;
	mostfrequent = MostCommonfactors(seqfactors); //list of tuples in descending order of factor count(eg, [(2,4),(4,4),(8,4)..])
	vector<int> allLikelyKeyLengths; //vector containing index[0] for tuples with highest factor count
	for(tuple<int,int> tup : list) {
		allLikelyKeyLengths.push_back(get<0>(tup));
	}
	return allLikelyKeyLengths;

}

string getNthSubkeysLetters(int n, int keylength, string message ) {
	//remove non letters from the message
	int i =n-1;
	string letter = "";
	vector <char> letters;
	while(i<strlen(message)) {
		letters.push_back(message[i]);
		i+=keyLength;
	}
	for(int j=0;j<letters.size();j++) {
		letter+=letters[j];
	}	
}


void main() {
	ciphertext=""; //add the ciphertext
	string hackedMessage = hackVigenere(ciphertext);
	if(hackedMessage!=NULL) {
		cout << "Copying hacked message to clipboard" ;
		cout << hackedMessage; 
	}
	else {
		cout << "Failed to hack encryption";
	}
}
	

