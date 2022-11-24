#include<stdio.h>
void main()
{
    int i,j,n,k;
    printf("Enter the number of rows\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=0;j<i;j++)
        {
            k=i+j;
            if(k%2==0)
            {
                printf("0 ");
               
            }
            else
            {
                printf("1 ");
                
            }
        }
        printf("\n");
    }
}