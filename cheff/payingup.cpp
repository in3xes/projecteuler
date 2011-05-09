#include<iostream>
#include<cmath>
using namespace std;

void print(int a[], int b) {
  int sum = 0;
  for(int i = 0; i < b; i++) {
    cout << a[i];
    sum = sum + a[i]*pow(2, b - i - 1);
  }
  cout << sum << endl;

}

int main() {
  
  int T;
  cin >> T;
  while(T--) {
    int count, bid, *notes;
    cin >> count;
    cin >> bid;
    notes = new int[count + 1];
    int possible = false;
    for(int i = 0; i < count; i++) {
      cin >> notes[i];
    }
    for(long i = 0; i < pow(2, count); i++) {
      int tmp = i;
      int sum = 0;
      bool yn = false;
      int bin[22] = {}, i_count = 0;

      while(tmp) {
	bin[i_count] = tmp % 2;
	tmp = tmp >> 1;
	i_count++;
      }
      // int b[14] = {1,0,0,1,0,0,0,0,0,0,0,1,0};
      // i_count = 13;
      for(int j = 0; j < i_count; j++) {
	sum = sum + bin[j] * notes[j];
	//cout << (j) << " : " << bin[j] << " * " << notes[j] << endl;

	if(sum == bid) {
	  //print(bin, i_count);
	  //	  cout << sum << " : " << bid << endl;
	  yn = true;
	  break;
	}
      }
      if(yn) {
	possible = true;
	break;
      }
    }
    if(possible) cout << "Yes" << endl;
    else cout << "No" << endl;
  }

  
  return 0;
}
