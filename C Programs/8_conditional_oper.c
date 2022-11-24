#include<stdio.h>
void main ()
{
    int a,b,c,lar;
    printf("enter your three numbers\n");
    scanf("%d %d %d",&a,&b,&c);
    lar = (a>b)?((a>c)?a:c):((b>c)?b:c);
    printf("%d is the largest",lar);
}
