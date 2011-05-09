#include <iostream>
#include <fstream>
using namespace std;

#define MAX 2001

int main() {

  ifstream in("input.txt");
  int cases;
  in >> cases;

  for(int kase = 0; kase < cases; kase++) {
    int credit, size, items[MAX];
    in >> credit;
    in >> size;
    for(int i = 0; i < size; i++) {
      in >> items[i];
    }
    for(int i = 0; i < size; i++) {
      int value = items[i];
      for(int j = i+1; j < size; j++) {
	if (items[j]+items[i] == credit) {
	  cout << "Case #" << kase+1 << ": " << i+1 << " " << j+1 << endl;
	  break;
	}
      }
    }
  }

  return 0;
}
	
