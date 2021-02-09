#include <stdio.h>

int main()
{
int wd;
double bal;
scanf("%d",&wd);
scanf("%f",&bal);
if (wd%5==0 && wd<=bal-0.50)
{
	    bal=bal-wd-0.5;
	    printf("%f",bal);
	}
	else{
	    printf("%f",bal);
	}

	return 0;

}
