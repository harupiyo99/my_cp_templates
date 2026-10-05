// https://github.com/harupiyo99/my_cp_templates/blob/main/Algo_template.cpp
// ↑リンク

#include <iostream>
#include <vector>    
#include <string>    
#include <algorithm>
#include <utility> 
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <unordered_set>
#include <set>
#include <cmath>
#include <iomanip>

using namespace std;

using ll = long long int;

template<class T> using vector2 = vector<vector<T>>;
template<class T> using vector3 = vector<vector2<T>>;
template<class T> using vector4 = vector<vector3<T>>;
template<class T> using vector5 = vector<vector4<T>>;
template<class T> using vector6 = vector<vector5<T>>;

template<class T> using min_pq = priority_queue<T, vector<T>, greater<T>>;
template<class T> using pq = priority_queue<T>;

const string small_al = "abcdefghijklmnopqrstuvwxyz";
const string large_al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const vector<ll> dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};

void solve() {
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}