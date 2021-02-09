#include <stdio.h>

int main() 
{
	int T;
	scanf("%d",&T);
	while(T--)
	{
		int A,B,C;
		scanf("%d%d%d",&A,&B,&C);
		if(A+B+C==180)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}
