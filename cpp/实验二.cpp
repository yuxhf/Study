#include <iostream>
void swap(int &a,int &b)
{
    int temp=a;
    a=b;
    b=temp;
}
int main()
{
    int a[10];
    for(int i=1;i<=4;i++)
    {
        std::cin>>a[i];
    }
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4-i;j++)
        {
            if(a[j]>a[j+1])
            {
                swap(a[j],a[j+1]);
            }
        }
    }
    std::cout<<"small to large output\n";
    for(int i=1;i<=4;i++)
    {
        std::cout<<a[i]<<' ';
    }
    std::cout<<std::endl;
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4-i;j++)
        {
            if(a[j]<a[j+1])
            {
                swap(a[j],a[j+1]);
            }
        }
    }
    std::cout<<"large to small output\n";
    for(int i=1;i<=4;i++)
    {
        std::cout<<a[i]<<' ';
    }
    return 0;
}
