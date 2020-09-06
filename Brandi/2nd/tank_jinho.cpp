#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cassert>
#include <cmath> //pow
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <climits>
#include <list>
#include <iomanip>
#include <map>
#pragma warning(disable:4996)
using namespace std;
typedef long long ll;
typedef pair<int, int> pii; typedef pair<ll, ll> pll;
typedef pair<int, ll> pil; typedef pair<ll, int> pli;
const int INF = 1087654321;


const int N = 1005;
int arr[N][N];
int dp[N][N];

int moveArr[][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
void solve()
{
   int n, life;
   cin >> n >> life;   

   for (int i = 0; i < n; ++i)
   {
      for (int j = 0; j < n; ++j)
      {
         cin >> arr[i][j];
         dp[i][j] = -1;
      }
   }

   queue<int> Q;
   Q.push(0);
   dp[0][0] = life - arr[0][0];

   while (!Q.empty())
   {
      int pos = Q.front(); Q.pop();

      int y = pos / n;
      int x = pos % n;
      int curLife = dp[y][x];
      if (x == n - 1 && y == n - 1)
      {
         continue;
      }

      for (int i = 0; i < 4; ++i)
      {
         int nx = x + moveArr[i][1];
         int ny = y + moveArr[i][0];

         if (nx >= 0 && nx < n && ny >= 0 && ny < n && dp[ny][nx] < dp[y][x] - arr[ny][nx])
         {
            dp[ny][nx] = dp[y][x] - arr[ny][nx];
            Q.push(ny*n + nx);
         }
      }
   }
   if (dp[n - 1][n - 1] <= 0)
   {      
      cout << -1;
      return;
   }
   cout << dp[n-1][n-1];
}
int main()
{

   freopen("1.txt", "r", stdin);

   ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

   solve();/*
   int testCase;   
   cin >> testCase;

   for (int tt = 0; tt < testCase; ++tt)
   {
      cout << "Case #" << tt + 1 << ": ";
      solve();
   }
   */
   return 0;
}
