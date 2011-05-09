#include<iostream>
#include<string>
#include<stack>
#include<cctype>
using namespace std;

bool isin(string a, char b) {
  int size = a.length();
  for(int i = 0; i < size; i++) {
    if(a[i] == b)return true;
  }
  return false;
}

int main() {

  int T;
  cin >> T;
	
  while(T--) {
    string input, add = "+-";
    stack <char> symbols;
    cin >> input;

    // cout << T <<" : " << input <<" : " << input.length() << endl;

    //Shunting Yard Algorithm

    int len = input.length();
    for(int i = 0; i < len; i++) {
      if(isalpha(input[i])) 
	cout << input[i];
      else {
	if(add.find(input[i]) != string::npos) {
	  symbols.push(input[i]);
	  continue;
	}
	if(mul.find(input[i]) != string::npos) {
	  while(mul.find(str(symbols.top())) != string:npos) {
	    symbols.pop();
	  }
	  if(add.find(str(symbols.top())) != string:npos)
	    symbols.push(input[i]);
	}
      }
    }
  }
  return 0;
}
