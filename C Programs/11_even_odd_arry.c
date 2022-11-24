#include<stdio.h>
void main()
{
    int arr[50],even[50],odd[50],n,i,c1=0,c2=0;
    printf("enter the number of integers in the array\n");
    scanf("%d",&n);
    printf("enter your integers\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
        {
            if(arr[i]%2==0)
            {
                even[c1]=arr[i];
                c1++;
            }
            else 
            {
                odd[c2]=arr[i];
                c2++;
            }
        }
    printf("Even \n ");  
    for(i=0;i<c1;i++)
    {
        printf("%d ",even[i]);
    }  
    printf("\nOdd \n");
    for(i=0;i<c2;i++)
    {
        printf("%d ",odd[i]);
    }
}
