#include<stdio.h>
void main()
{
    char str[80],temp[80];
    int i,n=0;
    printf("enter your string\n");
    gets(str);
    for(i=0;str[i]!='\0';i++)
    {
        n++;
    }
    for(i=0;i<n/2;i++)
    {
        temp[i] = str[i];
        str[i] = str[n-1-i];
        str[n-1-i] = temp[i];
    }
    puts(str);

}
