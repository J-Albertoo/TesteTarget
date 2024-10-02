#include <stdio.h>
#include <string.h>

int main() {
    // resolvi fazer em C porque já havia feito uma vez em uma prova na faculdade.
    
    char str[100], inverted[100];
    int length;

    // solicita a entrada da string ao usuário
    printf("Digite uma string: ");
    fgets(str, sizeof(str), stdin);
    
    // remove o caractere de nova linha se estiver presente
    length = strlen(str);
    if (str[length - 1] == '\n') {
        str[length - 1] = '\0'; // Substitui o newline por um terminador nulo
        length--; // Atualiza o comprimento da string
    }

    // usa ponteiros para inverter a string
    char *ptrStr = str; // ponteiro para a string original
    char *ptrInverted = inverted; // ponteiro para a string invertida

    for (int i = length - 1; i >= 0; i--) {
        *(ptrInverted++) = *(ptrStr + i); // copia o caractere para a string invertida
    }
    *ptrInverted = '\0'; // adiciona o caractere nulo ao final da string invertida

    // exibe a string invertida
    printf("String invertida: %s\n", inverted);

    return 0;
}
