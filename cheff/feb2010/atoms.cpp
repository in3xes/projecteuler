#include<iostream>
using namespace std;

int main() {
  
  int T;
  cin >> T;
  while(T--) {
    int n, m;
    cin >> n >> m;
    bool matrix[100][100] = {false};
    for(int i = 0; i < 10000; i++) {
      int y = i/100;
      int x = i%100;
      cout << i << " : " << matrix[x][y] << endl;
    }
  }
    return 0;
    
  }
	
