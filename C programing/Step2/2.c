#include <stdio.h>
int main()
{
    int no = 1;
    int count = 0;
    while (no <= 1000)
    {
        // printf("no");
        if (no % 2 == 0)
        {
            printf("%d\n", no);
            // no++;
            count++;
        }
        no++;
        // printf("%d\n",no);
        // no++;
        
    }
     printf("%d\n", count);

    return 0;
}
// 1 to 1000 with while loop