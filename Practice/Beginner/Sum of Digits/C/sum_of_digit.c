 #include <stdio.h>

int main(void) //codechef
{
	int t,rem,sum=0,i;
	scanf("%d",&t);
	int a[t];
	for(i=0;i<t;i++)
	{
	    scanf("%d",&a[i]);
	 }
	 for(i=0;i<t;i++)
	 {
	     sum=0;
	     while(a[i]>0)
	      {
	          rem=a[i]%10;
	          sum=sum+rem;
	          a[i]/=10;
	      }
	     printf("%d\n",sum);

	 }
	return 0;
}
