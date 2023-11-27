#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - while loop
 * Return: void
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: int
 */

int main(void)
{
	int child;
	pid_t pid;

	child = 5;
	while (child > 0)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
		else if (pid < 0)
			perror("fork");
		child--;
	}
	infinite_while();
	return (0);
}
