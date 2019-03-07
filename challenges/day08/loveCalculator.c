#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void lowerCaseName(char* name) {

	for (char* i = name; *i != '\0'; i++)
	{
		if(*i >= 65 && *i <= 90) {
			*i = *i + 32;
		}
	}
}

int chInString(char* code, char ch) {
	if(strchr(code, ch) != NULL)
	 {
	 	code = strchr(code, ch) + 1;
		return chInString(code, ch) + 1;
	} else {
		return 0;
	}
}

void stringPush(char* str, char ch) {
	str[strlen(str)] = ch;
	str[strlen(str)+1] = '\0';
}

void integerPush(int* arr, int num, int index) {
	arr[index] = num;
}

int intlen(int* arr) {
	int i;
	for (i = 0; arr[i] != 0; ++i);
	return i;
}

void printArray(int* arr, int len) {
	for (int i = 0; i < len; ++i)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}

void toStr(char* str, int* arr, int len) {
	int ind = 0;
	for (int i = 0; i < len; ++i)
	{
		if(arr[i] < 10) {
			str[ind++] = (char) 48 + arr[i];
		} else {
			int mod = arr[i] % 10;
			int whole = arr[i] / 10;
			str[ind++] = (char) 48 + whole;
			str[ind++] = (char) 48 + mod;
		}
	}
	str[ind] = '\0';
}

void toInt(char* str, int* arr) {
	int i;
	for (i = 0; i < strlen(str); ++i)
	{
		integerPush(arr, (int) str[i]- 48, i);
	}
	integerPush(arr, 0, i);
}

void calculate(char* str, int* arr){
	toInt(str, arr);
	int len = strlen(str);
	int i, j;
	if(len % 2 == 0) {
		for (i = 0, j = len-1; i < len/2; ++i, j--)
		{
			integerPush(arr, arr[i] + arr[j], i);
		}
		integerPush(arr, 0, i);
	} else {
		for (i = 0, j = len-1; i < (len-1)/2; ++i, j--)
		{
			integerPush(arr, arr[i] + arr[j], i);
		}
		integerPush(arr, arr[i], i);
		integerPush(arr, 0, i+1);
	}
	toStr(str,arr,intlen(arr));

}

int main(int argc, char* argv[]) {

	char bname[40], gname[40], code[100], counted[100];
	int arr[100] = {0};
	printf("\nEnter your first name : ");
	do{scanf("%s", bname);} while (getchar() != '\n');
	printf("\nEnter his/her first name : ");
	do{scanf("%s", gname);} while (getchar() != '\n');

	sprintf(code, "%s loves %s", bname, gname);
	lowerCaseName(code);
	memset(counted, '\0', 100);
	int len = strlen(code);
	int count = 0;
	for (int i = 0; i < len; ++i)
	{
		if(code[i] != ' ' && strchr(counted, code[i]) == NULL)
			 {
			 	integerPush(arr, chInString(code, code[i]), count++); 
			 	stringPush(counted, code[i]);
			 }
	}
	toStr(code,arr,intlen(arr));
	while(strlen(code) > 2) {
		calculate(code, arr);
	}
	if(strlen(code) == 1){
		code[1] = '0';
		code[2] = '\0';
	}	
	printf("\nLove Percentage : %s \% \n\n",code);
	return EXIT_SUCCESS;
}