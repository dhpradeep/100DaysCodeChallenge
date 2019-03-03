#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
	int day, month, year;
	int hour, minute, second;
	int daylight;
	printf("Enter your birthdate (DD.MM.YYYY) : ");
	scanf("%2d.%2d.%4d", &day, &month, &year);
	printf("\nEnter birth time (HH:MM:SS) : ");
	scanf("%2d:%2d:%2d", &hour, &minute, &second);
	int a[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
	if(year % 4 == 0) a[1] = 29;
	int daysInYears = 0;
	for (int i = 1; i < month; ++i)
	{
		daysInYears += a[i-1];
	}
	daysInYears += day;
	struct tm times = {
		second,minute,hour,day,month-1,year-1900,0,daysInYears,0
	};
	struct tm *birth = &times;
	time_t birthtime;   
	time_t curtime;
	birthtime = mktime(birth);
   	time(&curtime);
   	double ageInSec = difftime(curtime, birthtime);
   	printf("\n Age in seconds is : %.2f", ageInSec);
   	return EXIT_SUCCESS;
}