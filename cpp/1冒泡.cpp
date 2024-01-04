#include <iostream>
using namespace std;
int a[100]; 
int main()
{
    int n,temp;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cout<<"before\n";
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n";
    for(int j=0;j<n;j++)
    {
        for(int k=0;k<n-j-1;k++)
        {
            if(a[k]>a[k+1])//从小到大
            {
                temp=a[k];
                a[k]=a[k+1];
                a[k+1]=temp;
            }
        }
    }
    cout<<"after\n";
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    return 0;
}