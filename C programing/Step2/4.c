#include<stdio.h>
int main(){
    int num = 997;
    int count=0;
    for (int i = 2; i <= 10; i++)
    {
       if (num%i==0)
       {
        count++;
       }
       

    }
    
if (count>=2)
{
    printf("number is not prime");
}
else{
      printf("number is  prime ");
}
//printf("%d",count);
return 0;
}