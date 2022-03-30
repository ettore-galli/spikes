#include <stdio.h>
#include <math.h>

int main (){
    
    float a, b;
    float results[7];

    printf("Input a: ");
    scanf("%f", &a);
    printf("Input b: ");
    scanf("%f", &b);

    results[0] = a + b;
    results[1] = a - b;
    results[2] = a * b;
    results[3] = b !=0 ? a / b : 0.0;
    results[4] = pow(a, b);
    results[5] = sqrt(a);
    results[6] = sqrt(b);




    printf("Risultati");

    for (int i=0; i < sizeof(results)/sizeof(results[0]); i++){
        printf("# %f\n", results[i]);
    }


    return(0);
};