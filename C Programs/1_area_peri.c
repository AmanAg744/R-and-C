#include<stdio.h>
void main()
{
    int h = 20, w = 100, a, p;    // 1m=100cm
    printf("All Dimensions are in cm\n");
    a = h*w;
    p = 2*(h+w);
    printf("Area = %dcm^2\nPerimeter = %dcm",a,p);
}