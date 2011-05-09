#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--) {
		int min;
		cin >> min;
		int a1, a2,  b1, b2, c1, c2;
		double dab, dbc, dca;
		cin >> a1 >> a2 >> b1 >> b2 >> c1 >> c2;
		dab = sqrt(pow(a1 - b1, 2)+pow(a2 - b2, 2));
		dbc = sqrt(pow(b1 - c1, 2)+pow(b2 - c2, 2));
		dca = sqrt(pow(c1 - a1, 2)+pow(c2 - a2, 2));
		//cout << dab << " : " << dbc << " : " << dca << endl;
		
		int count = 0;
		if(dab <= min) count++;
		if(dbc <= min) count++;
		if(dca <= min) count++;
		
		if (count >= 2) {
			cout << "yes" << endl;
		}
		else {
			cout << "no" << endl; 
		}
	}
	return 0;
}
