#include <iostream>
int main()
{
    int score;
    std::cin>>score;
    int ch=score/10;
    switch(ch)
    {
        case 10:
            std::cout<<"A";
            break;
        case 9:
            std::cout<<"A";
            break;
        case 8:
            std::cout<<"B";
            break;
        case 7:
            std::cout<<"C";
            break;
        case 6:
            std::cout<<"D";
            break;
        default:
            std::cout<<"E";
    }
    return 0; 
}
