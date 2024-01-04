#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll N = 1010;
ll a[N];
const ll MOD=1e9+7;
ll comb[N][N];
void solve()
{
    for(ll i=0;i<N;i++)
    {
        comb[i][0]=comb[i][i] = 1;
        for(ll j=1;j<i;j++)
        {
            comb[i][j]=comb[i-1][j]+comb[i-1][j-1];
            comb[i][j]%=MOD;
        }
    }
}
int main()
{
    solve();
    int n;
    cin>>n;
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            cout<<comb[i][j]<<"\t";
        }
        cout<<"\n";
    }
    return 0;
}