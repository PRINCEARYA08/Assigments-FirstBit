#include <stdio.h>
int main()
{
    int no = 1;
    while (no <= 1000)
    {
        // printf("no");
        if (no % 2 == 0)
        {
            printf("%d\n", no);
            // no++;
        }
        no++;
        // printf("%d\n",no);
        // no++;
    }

    return 0;
}
// 1 to 1000 with while loop