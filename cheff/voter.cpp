#include<iostream>
#include<vector>
#include<algorithm>

#define MAX 150000
using namespace std;

int main() {
  
  int n1, n2, n3, A[MAX], size;
  cin >> n1 >> n2 >> n3;
  size = n1+n2+n3;
  for(int i = 0; i < size; i++) {
    cin >> A[i];
  }

  vector<int> v1(A, A+n1);
  vector<int> v2(A+n1, A+n1+n2);
  vector<int> v3(A+n1+n2, A+size);
    
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  sort(v3.begin(), v3.end());
  
  int count = 0;
  int ans[MAX] = {};
  
  for(int i = 0; i < size; i++) {
    if(binary_search(ans, ans+count, A[i])) continue;
    if(i < n1) {
      if((binary_search(v2.begin(), v2.end(), A[i]) || binary_search(v3.begin(), v3.end(), A[i]))) {
	ans[count] = A[i];
	count++;
      }
	}
    else if(i < n2+n1) {
      if((binary_search(v1.begin(), v1.end(), A[i]) || binary_search(v3.begin(), v3.end(), A[i]))) {
	ans[count] = A[i];
	count++;
      }
    }
    else {
      if((binary_search(v1.begin(), v1.end(), A[i]) || binary_search(v2.begin(), v2.end(), A[i]))) {
	ans[count] = A[i];
	count++;
      }
    }
    sort(ans, ans+count);
  }
  
  cout << count << endl;
  for(int i = 0; i < count; i++) {
    cout << ans[i] << endl;
  }

  return 0;
}
