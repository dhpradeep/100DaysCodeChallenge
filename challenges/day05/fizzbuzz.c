#include <stdio.h>
#include <stdlib.h>

int main() {
	for (int i = 1; i <= 100; ++i)
	{
		if(i % 15 == 0) printf("%d Fizzbuzz\n",i);
		else if( i % 3 == 0 ) printf("%d Fizz\n",i);
		else if( i % 5 == 0 ) printf("%d Buzz\n",i);
		else printf("%d\n",i);
	}
	return EXIT_SUCCESS;
}