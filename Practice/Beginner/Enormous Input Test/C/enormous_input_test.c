#include<stdio.h>
int main()
{
int t,n,k;
scanf("%d",&t);
scanf("%d",&n);
scanf("%d",&k);
int ans=0;
int i=0;
for ( i = 0; i < n; i++)
{
  if (t%k==0)
  {
     ans++;

  }
}
printf("%d\n",ans);
return 0;
}
