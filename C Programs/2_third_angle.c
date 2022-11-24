#include<stdio.h>
void main()
{
    int a,b,c;
   printf("enter two angles in degrees\n");
   scanf("%d%d",&a,&b);
   c = 180-(a+b);
   printf("%d is the third angle",c);
}
