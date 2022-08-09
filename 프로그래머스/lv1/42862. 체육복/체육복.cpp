#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int studentArr[31]={0,};
    for(int i=0;i<lost.size();i++){
        studentArr[lost[i]+1] += -1;
    }
    for(int i=0;i<reserve.size();i++){
        studentArr[reserve[i]+1] += 1;
    }
    int sum = 0;
    for(int i=0;i<=n+1;i++){
        if ((studentArr[i] == -1 && studentArr[i+1] == 1) || (studentArr[i] == 1 && studentArr[i+1] == -1)){
            studentArr[i] = 0;
            studentArr[i+1] = 0;
        }
        else if(studentArr[i] == -1)
            sum-=1;
    }
    answer = n + sum;
    return answer;
}