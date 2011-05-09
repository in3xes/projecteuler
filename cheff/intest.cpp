#include<iostream>
#include<cstdio>

int main() {
  using std::cin;
  using std::cout;
  
  int n; 
  long k, num, count = 0;
  cin >> n >> k;
  while(n--) {
    scanf( "%ld", &num);
    if(num % k == 0) count++;
  }
  cout << count;
  return 0;
}
