#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define filename "input.txt"

ifstream infileobject(filename);

void readline(string line) {
  if (infileobject.is_open())
    cout << "File is open" << endl;
  getline(infileobject, line);
  cout << line << endl;

  infileobject.close();
}
