#include <stdio.h>
#include <stdlib.h>

float ctof(float value) { return (value * 9 / 5) + 32; } 
float ftoc(float value) { return (value - 32) * 5 / 9; }
float ktoc(float value) { return (value - 273); }
float ctok(float value) { return (value + 273); }
float ktof(float value) { return ctof(ktoc(value)); }
float ftok(float value) { return ctok(ftoc(value)); }




int main(int argc, char* argv[]) {
	printf("\n");
	printf("\tChoose from the options:\n");
	printf("\t1. C to F\n");
	printf("\t2. F to C\n");
	printf("\t3. Kel to C\n");
	printf("\t4. C to Kel\n");
	printf("\t5. Kel to F\n");
	printf("\t6. F to Kel\n");

	printf("\n\tSelect 1 - 6 : ");
	
	int num;
	float value, result;

	scanf("%d", &num);
	if(num > 6 || num < 1) {
		return EXIT_FAILURE;
	}

	printf("\n\tPlease give the value : ");
	scanf("%f", &value);

	float (*caller[])(float) = {ctof,ftoc,ktoc,ctok,ktof,ftok};
	result = (*caller[num-1])(value);

	printf("\n\tConverted value is: %.2f\n", result);

	return EXIT_SUCCESS;
}