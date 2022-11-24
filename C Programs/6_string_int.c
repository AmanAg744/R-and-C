#include<stdio.h>
#include<stdlib.h>
void main()
{
    char str[80];
    int a;
    
    printf("Enter your string with numerical characters\n");
    gets(str);
    a = atoi(str);
    printf("%d",a);
    
    
}