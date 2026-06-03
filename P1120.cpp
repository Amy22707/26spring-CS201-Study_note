#include<bits/stdc++.h>
using namespace std;
bool cmp(int a,int b){
    return a>b;
}
int a[70],vis[70],n;
bool dfs(int cnt,int rest,int last,int len){
    if(cnt==1) return true;
    if(rest==0) return dfs(cnt-1,len,0,len);
    int i=last,pre=-1;
    while(i<n){
        if(a[i]>rest){
            i=lower_bound(a,a+n,rest,cmp)-a;
            continue;
        }
        if(vis[i]){
            i++;
            continue;
        }
        if(a[i]==pre){
            i++;
            continue;
        }
        vis[i]=1;
        if(dfs(cnt,rest-a[i],i+1,len)) return true;
        vis[i]=0;
        pre=a[i];
        if(rest==len||rest==a[i]) return false;
        i++;
    }
    return false;
}
int main(){
    int sum=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        sum+=a[i];
    }
    sort(a,a+n,cmp);
    memset(vis,0,sizeof(vis));
    for(int i=a[0];i<=sum;i++){
        if(sum%i!=0) continue;
        if(dfs(sum/i,i,0,i)){
            printf("%d\n",i);
            break;
        }
    }
}