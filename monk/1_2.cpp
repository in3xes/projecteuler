#include <stdio.h>
#include <iostream>
#include <cstring>


using namespace std;

int main() {

  int T;
  scanf("%d", &T);
  
  char S[30];
  while(T--) {
    scanf("%s", S);
    int len = strlen(S), index=0;
    char R[30];
    char last ='\0', current;
    for(int i = 0; i < len; i++) {
      current = S[i];
      if(last != current) {
  	R[index] = current;
  	last = current;
  	index++;
      }
    }
    R[index] = '\0';
    printf("%s\n", R);
  }
  return 0;
}
