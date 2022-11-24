#include<stdio.h>
void main ()
{
    int i,n,a[10],e;
    printf("enter number of elements in the array\n");
    scanf("%d",&e);
    printf("enter your array\n");
    for(i=0;i<e;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter your number\n");
    scanf("%d",&n);
    for(i=0;i<e;i++)
    {
        if(n==a[i])
        {
            if(n==a[i+1])
            {
                if(n==a[i+2])
                {
                    printf("%d is a triple\t",n);
                }
                else
                {
                    continue;
                }
            }
            else
            {
                continue;
            }
        }
        else
        {
            continue;
        }
    }

}
