#include <iostream>
#include <string>
#include <fstream>
#include <stack>
#include <sstream>

using namespace std;

#define MAX 2000

int main() {
  
  ifstream in;
  int cases;
  string line;

  in.open("input.txt");
  getline(in, line);
  istringstream sin(line);
  sin >> cases;

  for(int i = 0; i < cases; i++) {
    getline(in, line);
    stack<string> words;
    istringstream sin(line);
    do { 
      string word;
      sin >> word;
      words.push(word);
    } while(sin);

    cout << "Case #"<< i+1 << ":";
    while(!words.empty()) {
      cout << words.top() << " ";
      words.pop();
    }
    cout << endl;
  }
  
  in.close();

  return 0;
  
}
