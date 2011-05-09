#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main() {

  ifstream fin("input.txt");

  int length, size, cases;
  fin >> length;
  fin >> size;
  fin >> cases;

  string words[size];
  string input;

  //cout << size << endl;
  for(int i = 0; i < size; i++) {
    fin >> words[i];
  }

  // for(int i = 0; i < size; i++) {
  //   cout << i << " : ";
  //   cout << words[i] << endl;
  // }

  while(cases--) {
    fin >> input;
    cout << input << endl;
    
    int pos = 0;
    int ans = 0;
    set<int> location, temp;
    for(int i = 0; i < size; i++) location.insert(i);

    for(int i = 0; i < input.length(); ++i) {
      int iter = (int) location.size();
      if(input[i] == '(') {
  	++i;
  	while(input[i] != ')') {
  	  set<int>::iterator it = location.begin();
  	  for(int j = 0; j < iter; ++it) {
  	    if(words[*it][pos] == input[i])
  	      temp.insert(*it);
  	  }
  	  ++i;
  	}
      }
      else {
  	set<int>::iterator it = location.begin();
  	for(int j = 0; j < iter; ++it) {
  	  if(words[*it][pos] == input[i])
  	    temp.insert(*it);
  	}
      }
      location.clear();
      location = temp;
      temp.clear();
      pos++;
      ans = (int) location.size();
    }
    cout << ans;
  }
    
  return 0;
}
