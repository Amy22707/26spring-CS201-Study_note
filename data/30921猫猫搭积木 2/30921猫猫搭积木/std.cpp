#include<cstdio>
#include<algorithm>
#include<vector>
struct dsu
{
	int n,k,s,fa[100005],sz[100005];
	std::vector<int> p[100005];
	int find(int x){return x==fa[x]?x:find(fa[x]);}
	void split(int x)
	{
		--s;
		for (int i=0;i<(int)p[x].size();i++)
		{
			int k=p[x][i];
			fa[k]=k,sz[k]=1;
			if (k!=x) p[k].push_back(k);
			++s;
		}
		p[x].clear();p[x].push_back(x);
	}
	void merge(int x,int y)
	{
		x=find(x),y=find(y);
		if (x==y) return;
		if (sz[x]<sz[y]) std::swap(x,y);
		for (int i=0;i<(int)p[y].size();i++) p[x].push_back(p[y][i]);
		p[y].clear();
		fa[y]=x,sz[x]=sz[x]+sz[y];
		sz[y]=0;
		--s;
		if (sz[x]>=k) split(x);
	}
	void pre(int n,int k)
	{
		s=this->n=n,this->k=k;
		for (int i=1;i<=n;i++) fa[i]=i,sz[i]=1,p[i].push_back(i);
	}
};
dsu t;
int n,q,k;
int main()
{
	scanf("%d%d%d",&n,&q,&k);
	t.pre(n,k);
	while (q--)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		t.merge(x,y);
		printf("%d\n",t.s);
	}
	return 0;
}