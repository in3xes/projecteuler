#include<iostream>
using namespace std;

#define SIZE 200

void print(int a[], int size) {
  for(int i = size - 1; i > -1; i--) {
    cout << a[i] ;
  }
  cout << endl;
}

int main() {
  
  int T, num, pr[SIZE];
  cin >> T;
  while(T--) {
    int tmp = 0, x,m = 0;
    cin >> num;
    int t = num;
    while(t) {
      pr[m] = t % 10;
      m++;
      t = t / 10;
    }
    for(int j = num - 1; j > 0; j--) {
      for(int i = 0; i < m; i++) {
	x = pr[i] * j + tmp;
	pr[i] = x % 10;
	tmp = x / 10;
	// cout << x << " " << tmp << " " << pr[i] << " " << m << endl;
      }
      if(tmp > 0){
	while(tmp) {
	  pr[m] = tmp % 10;
	  tmp = tmp / 10;
	  m++;
	}
      }
    }
    print(pr, m);
  }
  return 0;
}

