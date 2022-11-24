#include<stdio.h>
void main()
{
    int i,j;
    printf("Enter the value of n\n");
    scanf("%d",&i);
   
        for(j=1;j<=10;j++)
        {
            printf("%dx%d = %d\n",i,j,i*j);
        }
    
}
