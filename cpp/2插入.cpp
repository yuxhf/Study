#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int inf=0x3f3f3f3f;
const int N=1e5+1;
int a[N];
int main()
{
    ios::sync_with_stdio(false);
    int n=100;
    for(int i=1;i<=100;i++)
    {
        a[i]=rand()%100+1;//1-100随机数
    }    
    sort(a+1,a+101);
    for(int i=1;i<=100;i++)
    {
        cout<<a[i]<<" ";
    }
    //查找x 
    int x;
    cin>>x;
    int flag=1;
    for(int i=1;i<=100;i++)
    {
        if(a[i]==x)flag=0;
    }
    if(flag==0)puts("YES");
    else
    {
        a[101]=x;
        sort(a+1,a+102);
        for(int i=1;i<=101;i++)
        {
            cout<<a[i]<<" ";
        }
    }
    return 0;
}