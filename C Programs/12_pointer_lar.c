#include<stdio.h>
void main ()
{
    int a,b,*pA,*pB;
    printf("enter your two numbers\n");
    scanf("%d%d",&a,&b);
    pA = &a;
    pB = &b;
    if(*pA>*pB)
    {
       printf("largest %d",*pA);
    }
    else
    {
        printf("largest %d",*pB);
    }

}