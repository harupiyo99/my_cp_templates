// https://github.com/harupiyo99/my_cp_templates/blob/main/Heur_template.cpp
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

#include<random>
#include<chrono>

using namespace std;

using ll = long long;

template<class T> using vector2 = vector<vector<T>>;
template<class T> using vector3 = vector<vector2<T>>;
template<class T> using vector4 = vector<vector3<T>>;
template<class T> using vector5 = vector<vector4<T>>;
template<class T> using vector6 = vector<vector5<T>>;

template<class T> using min_pq = priority_queue<T, v<T>, greater<T>>;

const string small_al = "abcdefghijklmnopqrstuvwxyz";
const string large_al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const vector<ll> dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};

class RandomGenerator {
    public:
    mt19937 randG;
    
    RandomGenerator(unsigned int seed = 1337) : randG(seed) {}

    // [l, r] の整数を無作為に出力
    long long RandomInt(long long l, long long r) {
        return uniform_int_distribution<long long>(l, r)(randG);
    }

    // [l, r) の実数を無作為に出力
    double RandomReal(double l, double r) {
        return uniform_real_distribution<double>(l, r)(randG);
    }
};

class Timer {
    chrono::high_resolution_clock::time_point start_time;
    public:
        Timer() {reset(); }

        void reset() {
            start_time = chrono::high_resolution_clock::now();
        }

        // 経過時間(秒)を取得
        double elapsed() const {
            auto end_time = chrono::high_resolution_clock::now();
            return chrono::duration<double>(end_time - start_time).count();
        }
};

void process() {
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    RandomGenerator random;
    Timer timer;

    while (true) {
        double elapsed_time = timer.elapsed();

        if (elapsed_time > 1.95) break;
        process();
    }

    return 0;
}