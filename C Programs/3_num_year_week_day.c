#include<stdio.h>
void main ()
{
    int n,y,w,d,r;
    printf("Enter the number of days\n");
    scanf("%d",&n);
    y = n / 365;
    w = (n%365)/7;
    r = (n%365)-(w*7);
    d = r%7;

    printf("%d years %d weeks %d days ",y,w,d);
}