#include<stdio.h>
int sum=0,num,d;
void sum_digits(int num)
{
    while(num!=0)
    {
        d = num%10;
        num = num/10;
        sum = sum + d;

    }

    if(sum/10==0)
    {
        printf("%d",sum);
    }
    else
    {
        
        num = sum;
        sum = 0;
        sum_digits(num);
    }
}
void main ()
{
    
    printf("Enter your number\n");
    scanf("%d",&num);
    sum_digits(num);
    
}