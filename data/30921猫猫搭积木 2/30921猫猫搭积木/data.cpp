#include<cstdio>
#include<random>
#include<algorithm>
#include<set>
std::random_device realseed;
std::mt19937 seed(realseed());
long long rd(long long l,long long r){std::uniform_int_distribution<long long> rnd(l,r);return rnd(seed);}
int f[100005];
std::set<int> s;
int main()
{
	int n=100000,q=499500,s=10000;
	printf("%d %d %d\n",n,q,s);
	for (int i=1;i<=n;i++) f[i]=i;
	std::shuffle(f+1,f+n+1,seed);
	for (int i=1;i<=5;i++)
		for (int k=1;k<=9999;k++)
			for (int t=0;t<=9;t++)
				printf("%d %d\n",f[t*10000+k],f[t*10000+k+1]);
//	for (int i=1;i<=q;i++)
//	{
//		int x,y;
//		x=rd(1,n),y=rd(1,n);
//		if (x==y) {--i;continue;}
//		printf("%d %d\n",f[x],f[y]);
//	}
	return 0;
}
/*
#include<cstdio>
#include<random>
#include<algorithm>
#include<set>
std::random_device realseed;
std::mt19937 seed(realseed());
long long rd(long long l,long long r){std::uniform_int_distribution<long long> rnd(l,r);return rnd(seed);}
int f[100005];
std::set<int> s;
int main()
{
	int n=100000,q=500000,s=rd(10000,n+1);
	printf("%d %d %d\n",n,q,s);
	for (int i=1;i<=n;i++) f[i]=i;
	std::shuffle(f+1,f+n+1,seed);
	for (int i=1;i<=q;i++)
	{
		int x,y;
		x=rd(1,n),y=rd(1,n);
		if (x==y) {--i;continue;}
		printf("%d %d\n",f[x],f[y]);
	}
	return 0;
}
*/