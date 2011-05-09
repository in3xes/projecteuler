#include<iostream>
using namespace std;

int main() {
  int T, num;
  cin >> T;
  while(T--) {
    cin >> num;
    int n = 1;
    while(n * 2 < num){
      n = n * 2;
    }
    cout << n << endl;
  }
  return 0;
}
    
