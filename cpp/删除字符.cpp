#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int inf=0x3f3f3f3f;
const int N=1e5+1;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int m=0;
    char a[1000];
    char b[1000];
    gets(a);
//    for(int i=0;i<strlen(a);i++)
//    {
//    	cout<<a[i];
//	}
    char del;
    cin>>del;
    for(int i=0;i<strlen(a);i++)
    {
        if(a[i]==del)continue;
        b[m++]=a[i];
    }
    for(int i=0;i<m;i++)
    {
        cout<<b[i];
    }
    return 0;
}
