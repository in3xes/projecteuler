#include<iostream>
#include<string>
#include<sstream>

using namespace std;

int main() {
  
  long int num;
  int size;
  cin >> num;
  string num_s;
  
  stringstream num_ss;
  num_ss << num;
  num_s = num_ss.str();

  size = num_s.length();
  int count = 0;
  while(size - 2*(count+1) > 2) {
    if(num_s[count] != num[size - 1])
    
  return 0;

}
