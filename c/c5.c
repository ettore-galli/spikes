#include <stdio.h>
#include <math.h>
#include <string.h>

// char getInputString(char *str){

//}

int main()
{

    char a, b, c;

    char *p;
    p = &a;
    *p = 'A';

    b = *p;

    p = &c;
    *p = 'Z';

    int array[7]; 

    printf("%c %c %c\n", a, b, c);
    printf("%pc\n", array);
    return (0);
};