#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 801

bool condition (int i,int j) { return (i>j); }

int main() {
  
  ifstream in("input.txt");

  int cases;
  in >> cases;

  for(int i = 0; i < cases; i++) {
    
    int size = 0;
    int v1[MAX] = {},  v2[MAX] = {};
    long long ans = 0;
    in >> size;
    

    for(int j = 0; j < size; j++) {
      in >> v1[j];
    }
    for(int j = 0; j < size; j++) {
      in >> v2[j];
    }
    
    vector<long long> vec1(v1, v1+size);
    vector<long long> vec2(v2, v2+size);

    sort(vec1.begin(), vec1.end());
    sort(vec2.begin(), vec2.end(), condition);

    // for(int j = 0; j < size; j++)
    //   cout << vec1[j] << " ";
    // cout << endl;

    // for(int j = 0; j < size; j++)
    //   cout << vec2[j] << " ";
    // cout << endl;


    for(int j = 0; j < size; j++) {
      //cout << j << " : " << ans << " : " << vec1[j] << " : " << vec2[j] << " : " << vec1[j] * vec2[j] << "   ";
      ans = ans + vec1[j] * vec2[j];
      //cout << ans << endl;
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
    
  }

  return 0;
}
