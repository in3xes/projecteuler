#include<iostream>
using namespace std;


#define SIZE 1000000

int max(int a, int b) {
  if(a > b) return a;
  return b;
}

void print(int a[], int size) {
  for(int i = 0; i< size; i++) cout << a[i] << " ";
  cout << endl;
}

int main() {
  int T;
  cin >> T;
  while(T--) {
    int row[SIZE] = {}, next[SIZE] = {}, result[SIZE] = {};
    int size;
    cin >> size;
    cin >> row[0];
    for(int i = 1; i < size; i++) {
      for(int j = 0; j < i + 1; j++) {
	cin >> next[j];
      }
      
      for(int j = 0; j < i + 1; j++) {
	if(j == 0)  {
	  result[0] = next[0] + row[0];
	  continue;
	}
	if(j == i) {
	  result[j] = next[j] + row[j-1];
	  continue;
	}
	result[j] = max(next[j] + row[j - 1], next[j] + row[j]);
      }

      for(int j = 0; j < i + 1; j++) {
	row[j] = result[j];
      }

      // cout << "Row : ";
      // print(row, i + 1);
      // cout << "Next : ";
      // print(next, i + 1);
      // cout << "Result : ";
      // print(result, i + 1);
    }

    int m = 0;
    for(int i = 0; i < size; i++) {
      if(result[i] > m) {
	m = result[i];
      }
    }
    cout << m;
  }
  return 0;
}
