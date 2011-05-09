#include<iostream>
using namespace std;

int main() {
  int withdraw;
  float balance;
  cin >> withdraw >> balance;
  if(withdraw + 0.5 < balance) {
    if(withdraw % 5 == 0) {
      cout << balance - withdraw - 0.5;
    }
    else
      cout << balance;
  }
  else {
    cout << balance;
  }

  return 0;
}
