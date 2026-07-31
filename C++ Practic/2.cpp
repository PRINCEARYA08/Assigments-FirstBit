#include <iostream>
using namespace std;
int main()
{
    int number, n1, n2, n3, n4, n5, q1, q2, q3, q4;

    number = 54372;
    n1 = number % 10;
    q1 = number / 10;

    n2 = q1 % 10;
    q2 = q1 / 10;

    n3 = q2 % 10;
    q3 =  q2 / 10;
     
    n4 = q3%10;
    q4 = q3/10;

n5= q4%10;

// cout<<n1;
// cout<<n2;
// cout<<n3;
// cout<<n4;
// cout<<n5;
 
int sum;
sum= n1+n2+n3+n4+n5;
cout<<sum;
    return 0;
}