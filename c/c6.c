#include <stdio.h>
 

int main()
{
    char *stringa;
  
    for (int i=0; i<10; i++){
        stringa[i] = '.';
    }
    stringa[7] = 'q';

    printf("%s, %p\n", stringa, stringa);

    return (0);
};