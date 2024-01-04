#include <iostream>
int main()
{
    int x,y;
    std::cin>>x;
    if(x<1)
    {
        y=x;
    }
    else if(x<10)
    {
        y=2*x-1;
    }
    else
    {
        y=3*x-11;
    }
    std::cout<<y;
    return 0;
}