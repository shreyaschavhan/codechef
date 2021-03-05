#include <stdio.h>

int main(void) {
    int t,i,A,B;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d %d",&A, &B);
        if(A>B)
        {
            printf(">\n");
        }
        else if(A<B)
        {
            printf("<\n");
        }
        else if(A==B)
        {
            printf("=\n");
        }
    }
      
}

