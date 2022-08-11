#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int minw = -1;
    int minh = -1;
    for(int i=0;i<sizes.size();i++){
        if(sizes[i][0] > sizes[i][1]){
            minw = max(sizes[i][0],minw);
            minh = max(sizes[i][1],minh);
        }
        else{
            minw = max(sizes[i][1],minw);
            minh = max(sizes[i][0],minh);
        }
    }
    answer = minw * minh;
    return answer;
}