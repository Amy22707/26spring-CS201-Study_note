#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<queue>
using namespace std;
const int INF=0x3f3f3f3f;
int a[101][101];
int dp[1<<10][101];//j为根，将i中的关键点全部联通的最短距离
int n,m,k;
void dijkstra(int x){
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;
    for(int i=1;i<=n;i++){
        if(dp[x][i]<INF){
            q.push({dp[x][i],i});
        }
    }
    while(!q.empty()){
        auto [dist,u]=q.top();
        q.pop();
        if(dist>dp[x][u]){
            continue;
        }
        for(int v=1;v<=n;v++){
            int w=a[u][v];
            if(dp[x][v]>dp[x][u]+w){
                dp[x][v]=dp[x][u]+w;
                q.push({dp[x][v],v});
            }
        }
    }
}
int main(){
    scanf("%d %d %d",&n,&m,&k);
    memset(a,INF,sizeof(a));
    for(int i=0;i<m;i++){
        int u,v,w;
        scanf("%d %d %d",&u,&v,&w);
        if(a[u][v]>w){
            a[u][v]=w;
            a[v][u]=w;
        }
    }
    int s[k];
    for(int i=0;i<k;i++){
        scanf("%d",&s[i]);
    }
    for(int p=1;p<=n;p++){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                a[i][j]=min(a[i][j],a[i][p]+a[p][j]);
            }
        }
    }
    memset(dp,INF,sizeof(dp));
    for(int i=1;i<(1<<k);i++){
        if(!(i&(i-1))){//i只有1个1
            for(int j=0;j<k;j++){
                if(i&(1<<j)){
                    dp[i][s[j]]=0;
                    break;
                }
            }
        }
        for(int j=i;j>0;j=(j-1)&i){//枚举i的子集
            for(int p=1;p<=n;p++){
                dp[i][p]=min(dp[i][p],dp[j][p]+dp[i^j][p]);
            }
        }
        dijkstra(i);
    }
    int ans=INF;
    for(int i=1;i<=n;i++){
        ans=min(ans,dp[(1<<k)-1][i]);
    }
    printf("%d\n",ans);
}