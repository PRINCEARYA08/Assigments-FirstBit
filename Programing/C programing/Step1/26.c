#include <stdio.h>
int main()
{
    char ch = 'n';
    double price = 5000;
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

    return 0;
}