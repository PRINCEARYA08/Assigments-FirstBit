#include <stdio.h>
int main()
{
    int no = 1;
    int count = 0;
    while (no <= 1000)
    {

        if (no % 3 &&  no % 5 == 0)
        {
            printf("%d\n", no);
             count++;
        }
        no++;
    }
     printf("%d\n", count);

    return 0;
}

// 1 to 1000 with while loop where number is divisible by 3 and 5