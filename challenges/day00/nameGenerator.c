#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define BUFSIZE 100

void lowerCaseName(char* name) {

	for (char* i = name; *i != '\0'; i++)
	{
		if(*i >= 65 && *i <= 90) {
			*i = *i + 32;
		}
	}
}

bool compareStrings(char* name1, char* name2) {
	lowerCaseName(name1);
	lowerCaseName(name2);
	char* c = name1;
	char* c1 = name2;
	for (;*c != '\0' && *c1 != '\0'; c++,c1++)
	{
		if(*c != *c1) return false;
	}
	return true;
}



int main(int argc, char* argv[]) {
	char names[10][40] = {"Saroj", "Pradeep", "Arjun", "Suman", "Pravhu", "Oscar", "Jay","Nischal","Manish","Raju"};
	char name[BUFSIZE];

	printf("Please enter the part to search : \n");
	scanf("%s", name);

	for (int i = 0; i < 10; ++i)
	{
		char nameToComp[BUFSIZE];
		memcpy(nameToComp, names[i], BUFSIZE);
		if(compareStrings(name, nameToComp)) {
			printf("Name found : %s\n", names[i]);
			return EXIT_SUCCESS;
		}
	}

	printf("No name found!\n");
	return EXIT_FAILURE;
}