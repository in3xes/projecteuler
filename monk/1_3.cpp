#include <stdio.h>
#include <iostream>
#include <cstring>


using namespace std;

int main() {

  int T;
  scanf("%d", &T);
  int N = 1000001;
  int arr[N];
  while(T--) {
    int size, X, sum = 0, start = 0, end, found = 0;
    scanf("%d %d", &size, &X);
    for(int i = 0; i < size; i++) {
      int tmp;
      scanf("%d", &tmp);
      arr[i] = tmp;
    }
    for(int i = 0; i < size; i++) {
      if(found)
	break;
      if((sum + arr[i]) < X)
	sum = sum + arr[i];
      else if(sum + arr[i] == X) {
	found = 1;
	end = i;
      }
      else {
	sum = sum + arr[i];
	while(start < i) {
	  sum = sum - arr[start];
	  start++;
	  if(sum == X) {
	    found = 1;
	    end = i - 1;
	  }
	  else if(sum < X)
	    break;
	}
      }
    }
    if(found)
      printf("%s\n", "YES");
    else
      printf("%s\n", "NO");
  }
  return 0;
}
