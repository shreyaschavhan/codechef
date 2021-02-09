#include <stdio.h>

#include <stdlib.h>

int main()

{

    int t,i; long a,b,c;

    scanf("%d",&t);

    for(i=1;i<=t;i++)

    {

        scanf("%ld %ld %ld",&a,&b,&c);

        if(a<b&&a>c||a>b&&a<c)

            printf("%ld\n",a);

        else if(b>a&&b<c||b<a&&b>c)

            printf("%ld\n",b);

        else if(c>a&&c<b||c<a&&c>b)

            printf("%ld\n",c);

    }
}
