#include <iostream>
using namespace std;
int main()
{
    char ch;
    cout<<"Enter are you Student ";
    cin>>ch;

    double price ;
      cout<<"Enter price you buy";
    cin>>price;
    if (ch == 'y')
    {
        if (price >= 5000)
        {
            printf("dicount for you");
        }
        else{
             printf("no");
        }
    }
    else if(ch == 'n')
    {
        printf("dicount not for you");
    }
    else{
        cout<<"sorry we can't help you";
    }

    return 0;
}