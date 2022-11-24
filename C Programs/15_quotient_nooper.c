#include<stdio.h>
void main()
{
    int a,b,q=0;
    printf("enter your dividend and divisor respectively\n");
    scanf("%d%d",&a,&b);
    while(a>=b)
    {
        a = a - b;
        q++;
    }
    printf("quotient is %d",q);
}