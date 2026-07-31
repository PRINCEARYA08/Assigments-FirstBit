#include <stdio.h>
int main()
{
    int number;
    scanf("%d", &number);
    if (number % 2 == 0)
    {
       // printf("Number is less then 2");
       printf("Number is even");
    }
    // else if (number==0)
    // {
    //     printf("zero");
    // }
    
    else
    {
        printf("number is odd");
    }
    return 0;
}
