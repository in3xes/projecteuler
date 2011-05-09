#include<stdio.h>
using namespace std;

#define MAX 1500100
int main() {
  
  long int n1, n2, n3, size, count = 0;
  long int values[MAX] = {0};
  scanf("%ld%ld%ld", &n1, &n2, &n3);
  size = n1 + n2 + n3;

  long int tmp;
  long int max = 0;
  for(long int i = 0; i < size; i++) {
    scanf("%ld", &tmp);
    max = (max > tmp ? max:tmp);
    if(values[tmp] >= 1) {
      values[tmp] = values[tmp] + 1;
    }
    else values[tmp] = 1;
  }
  for(long int i = 0; i < max; i++) {
    if(values[i] > 1) count ++;
  }
  printf("%ld\n",count);
  for(long int i = 0; i < max; i++) {
    if(values[i] > 1) printf("%ld\n", i);
  }
  return 0;
}
