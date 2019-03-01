#include <stdio.h>
#include <stdlib.h>
#ifdef __unix__
#include <unistd.h>
#endif
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


int main(int argc, char* argv[]) {
	char hOrT, res;
	bool found = false;
	printf("\n\n");
	printf("Predict Head(h) or Tail(t) :");
	scanf("%c",&hOrT);
	printf("\n\n");
	if(hOrT != 'h'&& hOrT != 'H' && hOrT != 't' && hOrT != 'T') {
		printf("Not Valid Input\n\n");
	} else {
		printf("Shuffling..\n");
		#ifdef __unix__
			sleep(1);
		#endif
		if (i_rnd(2) == 1) 
			found= true;
		else
			found = false;
		if(found) {
			if(hOrT == 't' || hOrT == 'T') {
				printf("You have Predicted right . It's Tail.\n");
			} else {
				printf("You have Predicted right . It's Head.\n");
			}
		} else {
			if(hOrT == 't' || hOrT == 'T') {
				printf("You have Predicted false . It's Head.\n");
			} else {
				printf("You have Predicted false . It's Tail.\n");
			}
		}
	}
	printf("\n\n");
	return EXIT_SUCCESS;
}