#include <stdio.h>
#include <math.h>

int main (){
    
    int a;

    printf("Input : ");
    scanf("%d", &a);

    switch (a)
    {
    case 1:
        printf("red");
        break;
    case 2:
        printf("green");
        break;
    case 3:
        printf("blue");
        break;        
    default:
        printf("white");
        break;
    }


    return(0);
};