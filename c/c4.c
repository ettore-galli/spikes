#include <stdio.h>
#include <math.h>
#include <string.h>

// char getInputString(char *str){

//}

void acquireInputString(char *prompt, char *strIn){
    printf("%s", prompt);
    fgets(strIn, 50, stdin);
}

void concatStrings(char *s1, char *s2, char *outBuf){
    strcpy(outBuf, s1);
    strcat(outBuf, s2);
}

int main (){
    
    char str1[50];
    char str2[50];
    char full[100];

    acquireInputString("Inserisci il testo 1: ", str1);
    acquireInputString("Inserisci il testo 2: ", str2);

    concatStrings(str1, str2, full);

    printf("-----\n%s-----\n", full);

    return(0);
};