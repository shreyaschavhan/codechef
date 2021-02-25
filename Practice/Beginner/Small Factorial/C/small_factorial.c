#include <stdio.h>

int main(void) 
{
    int T,i;
    scanf("%d",&T);
    for (i=T;i>0;i--)
    {
        int n,m=1,j;
        scanf("%d",&n);
        for (j=n;j>0;j--)
        {
            m=m*j;
        }
        printf("%d\n",m);
    }
	
	return 0;
}

