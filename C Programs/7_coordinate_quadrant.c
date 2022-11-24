#include<stdio.h>
void main ()
{
    int x,y;
    printf("Enter your x and y coordinate respectively\n");
    scanf("%d %d",&x,&y);
    if(x>=0&&y>=0)
    {
        printf("First Quadrant");
    }
    if(x<0&&y>=0)
    {
        printf("Second Quadrant");
    }
    if(x<0&&y<0)
    {
        printf("Third Quadrant");
    }
    if(x>=0&&y<0)
    {
        printf("Fourth Quadrant");
    }
}
