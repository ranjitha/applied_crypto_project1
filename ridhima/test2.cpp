#include <iostream> 
#include <cstring>
#include <string>
#include <vector>
#include <map> 
using namespace std;

LETTERS = " abcdefghijklmnopqrstuvwxyz";
ETAOIN = "etaoinsrhdlucmfywgpbvkxqjz";
NUM_MOST_FREQ_LETTERS = 10; //attempts this many letters per subkey
MAX_KEY_LENGTH = 10; //will not attempt keys longer than this
DICTIONARY2 = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose', ' ', '']


string decryptMessage(string key, string message) {
	return translateMessage(key, message, 'decrypt');
}

string translateMessage(string key, string message, string mode) {
	vector <char> translated;
	offsets = as_list(key);
	for(int i=0; i< strlen(message); i++) {
		char symbol = message[i];
		auto index = LETTERS.find(symbol);
		int new_index=0;
		if(mode=="encrypt") {
			new_index = (index + offsets[i % offsets.size()]) % strlen(LETTERS);
		}
		else {
			new_index = (index - offsets[i % offsets.size()]) % strlen(LETTERS);
		}
		translated.push_back(LETTERS[new_index]);
	}
	string trans = "";
	for(int j=0; j< translated.size(); j++) {
		trans+=translated[j];
	}
	return trans;
}


vector <char> as_list(string key) {
	vector <char> keyletters; //for each char in key, finds its corres index in LEtters and adds it to the list
	for(int i=0; i< strlen(key); i++) {
		auto index = LETTERS.find(key[i]);
		keyletters[i]= index;
	}
	return keyletters;
}

map <char,int> getLetterCount(string message) {
	// Returns a dictionary with keys of single letters and values of the
    // count of how many times they appear in the message parameter.
	map <char,int> lettercount = {{'a', 0},{'b', 0}, {'c', 0}, {'d', 0}, {'e', 0}, {'f', 0}, {'g', 0}, {'h', 0}, {'i', 0}, {'j', 0}, {'k', 0}, {'l', 0}, {'m', 0}, {'n', 0}, {'o', 0}, {'p', 0}, {'q', 0}, {'r', 0}, {'s', 0}, {'t', 0}, {'u', 0}, {'v', 0}, {'w', 0}, {'x', 0}, {'y', 0}, {'z', 0}, {' ',0};
	int ind =0;
	for(int l=0; l<strlen(message); l++) {
		ind = LETTERS.find(message[l]);
		if(ind<=strlen(LETTERS)) { //find returns index if char is in Letters, if not it returns max length of the data type
			lettercount[message[l]] +=1;
		}
	}
	return lettercount;
}

string getFrequencyOrder(string message) {

}

int englishFreqMatchScore(string message) {
	string freqOrder = getFrequencyOrder(message);
	int matchScore =0;

}

map <string,vector<int>> findRepeatSequences(string message) {
	// remove non letters and spaces from the message?
	// Goes through the message and finds any 3 to 5 letter sequences
    //that are repeated. Returns a dict with the keys of the sequence and
    //values of a list of spacings (num of letters between the repeats).
    //Use a regular expression to remove non-letters from the message.
    //message = NONLETTERS_PATTERN.sub('', message.lower())

    // Compile a list of seqLen-letter sequences found in the message.
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
	// Returns a list of useful factors of num. By "useful" we mean factors
    // less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
    // returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]
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
	//First, get a count of how many times a factor occurs in seqFactors.
	map<int,int> factorcounts;
	map<int,int> iterator it2 = factorcounts.begin();
	map <string, vector<int>>::iterator it1 = seqfactors.begin();
	//seqFactors keys are sequences, values are lists of factors of the
     // spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
     //18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
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
	/* # Find out the sequences of 3 to 5 letters that occur multiple times
     # in the ciphertext. repeatedSeqSpacings has a value like:
     # {'EXG': [192], 'NAF': [339, 972, 633], ... } */
	repeatSpacings = findRepeatSequences(ciphertext); 
	map <string,vector<int>> seqfactors; //factors of each number in the sequences list
	map <string, vector<int>>::iterator it = repeatSpacings.begin();
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
	/* Returns every Nth letter for each keyLength set of letters in text.
     # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
     #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
     #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
     #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

     # Use a regular expression to remove non-letters from the message.
     #message = NONLETTERS_PATTERN.sub('', message) */
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

string attemptHackWithKeyLength(string ciphertext, int mostLikelyKeyLength) {
	// Determine the most likely letters for each letter in the key.
    // allFreqScores is a list of mostLikelyKeyLength number of lists.
    // These inner lists are the freqScores lists.
	vector <vector<int>> allFreqScores;
	for (int nth=1; nth <mostLikelyKeyLength+1; nth++) {
		string nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertext);
		vector <tuple<char,int>> freqScores; 
		//freqScores is a list of tuples like: [(<letter>, <Eng. Freq. match score>), ... ]

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
	

