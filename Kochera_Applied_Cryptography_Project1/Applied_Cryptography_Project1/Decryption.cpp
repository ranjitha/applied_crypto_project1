#include <iostream>
#include <string>
#include <vector>
#include "Encryption.h"
using namespace std;

void longest(char str[], int length, int arr[])
{
	int len=0;
	int i=1;
	arr[0]=0;
	while (i<length)
	{
		if (str[i]==str[len])
		{
			len++;
			arr[i]=len;
			i++;

		}
		else
		{
			if(len!=0)
			{
				len = arr[len-1];
			}
			else
			{
				arr[i]=0;
				i++;
			}
		}
	}

}

bool repeat(char str[])
{
	int n=strlen(str);
	int arr[n];
	longest(str,n,arr);
	int len = arr[n-1];
	if (len>0 && n%(n-len)==0)
		return true
	else
		return false 
}



vector<string> get_dict() {
	vector<string> candidates;
	candidates.push_back("gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee");
	candidates.push_back("intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor");
	candidates.push_back("frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p");
	candidates.push_back("distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg");
	candidates.push_back("undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis");
	return candidates;
}

int decrypt(string cipher, vector<string> candidates) {
	int key_size = 10;
	for (string cand : candidates) {

	}
	return 0;
}

int main() {
	//Filled vector with different string candidates from dict 1
	vector<string> candidates = get_dict();
	string ciphered = get_cipherText();

	int guess = decrypt(ciphered, candidates);

}
