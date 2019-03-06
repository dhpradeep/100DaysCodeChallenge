#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define GAME 3

bool srand_called = false;

int i_rnd(int i) {
    if (!srand_called) {
        srand(time(NULL) << 10);
        srand_called = true;
    }
    return rand() % i;
}

int main(int argc, char* argv[]) {

	char games[GAME][30] = {"rock","paper","scissor"};
	int id = -1;

	if(argc == 2) {
		for (int i = 0; i < GAME; ++i)
		{
			if(strcmp(argv[1], games[i]) == 0)
				id = i;
		}
	}	

	if(id == -1) {
		printf("\n\t Error in syntax.");
		printf("\n\n\t Syntax : ./rockPaperScissor rock|paper|scissor\n\n");
		return EXIT_FAILURE;
	}

	int computer = i_rnd(GAME);

	int winComp = (id == GAME-1) ? 0 : id + 1;
	if(winComp == computer) {
		printf("Computer wins! Computer has %s\n", games[computer]);
		return EXIT_SUCCESS;
	}

	int winUser = (computer == GAME-1) ? 0 : computer + 1;
	if(id == winUser) {
		printf("You win! Computer has %s\n", games[computer]);
		return EXIT_SUCCESS;
	}

	printf("Its a draw. Computer has %s\n", games[computer]);
	return EXIT_SUCCESS;	
}