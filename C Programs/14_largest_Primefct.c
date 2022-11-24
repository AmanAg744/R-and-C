#include<stdio.h>
void main()
{
    int n,i,j,flag=0,l=0,arr[80],lar;
    printf("Enter the number\n");
    scanf("%d",&n);
    for(i=2;i<=n/2;i++)
    {
        if(n%i==0)
        {
            for(j=2;j<=i/2;j++)
            {
                if(i%j!=0)
                {
                    continue;
                }
                else
                {
                    flag = 1;
                }
            }
            if(flag==0)
            {
                arr[l] = i;
                l++;
            }
            flag=0;
        }   
    }
    lar = arr[0];
    for(i=1;i<l;i++)
    {
        if(arr[i]>lar)
        {
            lar = arr[i];
        }
    }
    printf("the largest prime factor of %d is %d",n,lar);

}