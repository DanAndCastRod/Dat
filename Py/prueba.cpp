#include <stdio.h>
int max( int a, int b)
{
    if (a > b) return a;
    return b;
}
char *max(char *a, char *b)
{
    if (stremp(a,b) > 0) return a;
    return b;
}
int main()
{
    printf("max(19,69) = %d\n", max(16,69))
}