#include <iostream>
int main()
{
    int n;
    std::cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=n-i+1;j>=1;j--)
        {
            std::cout<<' ';
        }
        for(int j=1;j<=i*2-1;j++)
        {
            if(j==1||j==i*2-1)
                std::cout<<'*';
            else 
                std::cout<<' ';
        }
        std::cout<<std::endl;
    }
    for(int i=1;i<=n*2+1;i++)
    {
        if(i==1||i==n*2+1)
            std::cout<<'*';
        else 
            std::cout<<' ';
    }
    std::cout<<std::endl;
    for(int i=n;i>=1;i--)
    {
        for(int j=n-i+1;j>=1;j--)
        {
            std::cout<<' ';
        }
        for(int j=1;j<=i*2-1;j++)
        {
            if(j==1||j==i*2-1)
                std::cout<<'*';
            else 
                std::cout<<' ';
        }
        std::cout<<std::endl;
    }
    return 0;
}