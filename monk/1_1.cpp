#include <stdio.h>
#include <iostream>
#include <cstring>


using namespace std;

int main() {

  int T;
  char S[30];
  scanf("%d", &T);
  
  while(T--) {
    scanf("%s", S);
    int len = strlen(S);
    char R[30];
    for(int i = len-1; i >=0; i--) {
      R[len-1-i] = S[i];
    }
    R[len] = '\0';
    printf("%s\n", R);
  }
  return 0;
}
