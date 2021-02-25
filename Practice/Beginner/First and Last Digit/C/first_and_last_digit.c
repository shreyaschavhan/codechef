#include <stdio.h>

int main(void) {
	// your code goes here
	int N;
	scanf("%d",&N);
	char a[10];
    while(N--)
    	{
    		scanf("%s",a);
    		printf("%ld\n",(a[0]-'0' + a[strlen(a)-1] - '0'));
	  	}
	return 0;
}
