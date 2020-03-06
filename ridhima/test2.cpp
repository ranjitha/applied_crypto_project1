#include <iostream> 
#include <cstring>
#include <string>
#include <vector>
#include <map> 

map <string,vector<int>> findRepeatSequence(string message) {
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
				seqSpace[sequence].push_back(i-start);
				}
			}
		}
	}
	return seqSpace;
}

vector <int> getFactors(int num) {
	//returns a list of factors of a number. each factor should be at max 24
	vector <int> factors;
	if num<2 return factors;
	for(int i=2;i<25;i++){
		if(num%i==0 && int(num/i)!=1){ //no point using 1 as a factor
			factors.push_back(i);
			factors.push_back(int(num/i));
		}
	}
	return factors;
}

vector <int> frequentfactors()

void kasiski(string ciphertext){
	repeatSpacings = findRepeatSequence(ciphertext); 

}