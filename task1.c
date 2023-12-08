#include <stdio.h>
#include <stdlib.h>

//to compile on cmd, gcc -o task1 task1.c
//matteo gristina
int main(int argc, char *argv[]) {
	
// define threshold and RGB values
	int thresh = 170;
	int zero = 0;
	int max = 255;


// dynamically allocate memory to array called matrix
	int *matrix = (int *) malloc((argc - 1) * sizeof(int));

// Read elements from command line and convert to integers
	for (int i = 0; i < argc - 1; i++) {
		matrix[i] = atoi (argv[i + 1]);	//atio changes argument input (string) to int
		
		if (matrix[i] > thresh) {
			printf ("%d ", max);
		} else {
			printf ("%d ", zero);
		}
			
	}
// Free dynamically allocated memory

	free(matrix);


return 0;
}