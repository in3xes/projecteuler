#include<iostream>
using namespace std;

int main() {
  
  int size;
  while(true) {
    cin >> size;
    int * values;
    values = new int[size + 1];
    bool b = true;
    if(size == 0) break;
    
    for(int i = 0; i < size; i++) {
      cin >> values[i];
    }
    for(int i = 0; i < size; i++) {
      //      cout << values[i] << " : " << values[values[i] - 1] << " : " << (i+1) << endl;
	if(values[values[i] - 1] == (i +1)) continue;
      else {
	b = false;
	break;
      }
    }
    if(b) cout << "ambiguous" << endl;
    if(!b) cout << "not ambiguous" << endl;
    
    delete[] values;
  }
  
  return 0;
}
