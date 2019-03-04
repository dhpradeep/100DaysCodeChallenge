#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

bool srand_called = false;

int i_rnd(int i) {
    if (!srand_called) {
        srand(time(NULL) << 10);
        srand_called = true;
    }
    return rand() % i;
}

void encrypt(char* code) {
	int hash = strlen(code);
	char* encrypt = malloc((hash *3) +3);
	char* toHash = encrypt;
	for (char ch = *code; ch != '\0'; ch = *(++code))
	{
		int hashNum = encrypt - toHash; 
		*(encrypt++) = (char) 126 - i_rnd(66);
		*(encrypt++) = (char) 126 - i_rnd(66);
		*(encrypt++) = ch + hash - hashNum ;
	}

	*(encrypt++) = (char) 126 - i_rnd(66);
	*(encrypt++) = (char) 126 - i_rnd(66);
	*encrypt = '\0';
	printf("\nEncrypted Code : %s\n\n", toHash);
	free(toHash);
}

void decrypt(char* code) {
	int hash = ((strlen(code) - 3) / 3) + 2;
	char* decrypt = malloc(hash);
	char* toFree = decrypt;
	char* word = code;
	printf("%d\n", hash);
	for (int ch = *code; ch != '\0'; ch = *(++code))
	{
		if((code - word + 2) % 3  == 1){
			*(decrypt++) = ch - (word - code + 1) - hash;
			printf("%c\n", ch);
			printf("%d\n", code - word);
		}
	}
	*decrypt = '\0';
	printf("\nDecrypted Code : %s\n\n", toFree);
	free(toFree);
}

int main(int argc, char* argv[]) {
	if(argc != 3 || (strcmp(argv[1],"-e") != 0 && strcmp(argv[1],"-d") != 0)) {
		printf("\n\t Error in syntax.");
		printf("\n\n\t Syntax : ./encryptDecrypt -flag code \
			\n\t Flags:\
			\n\t -e : Encrypt\
			\n\t -d : Decrypt\n\n");
		return EXIT_FAILURE;
	}
	if(strcmp(argv[1], "-e") == 0) {
		encrypt(argv[2]);
	} else {
		decrypt(argv[2]);
	}	
	return EXIT_SUCCESS;
}