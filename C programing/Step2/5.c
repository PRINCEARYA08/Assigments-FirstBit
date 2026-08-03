#include<stdio.h>
int main(){

    int num = 28;
   int i = 0,sum= 0;
   while (i<=num/2)
   {
if (num%i==0)
{
    sum=sum+i;

}
i++;
   }
   printf("%d",sum);

    return 0;
}