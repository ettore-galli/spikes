#include <stdio.h>
#include <stdlib.h>

int main()
{
    int count = 21;
    int c = 0;
    int cmp = 5;
    for (size_t i = 0; i < count; i++)
    {
        c =  (c + 1) & ((c + 1) < cmp);
        printf("%i   \n", c);
    }
    short value = 1521;
    printf("%i   \n", value);
    printf("%i   \n", value/32);
    printf("%i   \n", value >> 5);
    printf("%i   \n", value/16);
    printf("%i   \n", value >> 4);

    float coso = 123.4567890;
    printf("%i   \n", (int) coso);


    return (0);
};