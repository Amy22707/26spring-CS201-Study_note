#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
const int MAXN=200005;
const double alpha=0.75;//替罪羊树平衡因子
struct Node{
    int x,y;
    int v,sum;
    int x1,y1,x2,y2;
    int l,r;
    int size;
} t[MAXN];
int root,tot;
int cur_nodes[MAXN],node_cnt;
bool cmpx(int a,int b){
    return t[a].x<t[b].x;
}
bool cmpy(int a,int b){
    return t[a].y<t[b].y;
}
void push_up(int u){
    int l=t[u].l,r=t[u].r;
    t[u].size=t[l].size+t[r].size+1;
    t[u].sum=t[l].sum+t[r].sum+t[u].v;
    t[u].x1=min({t[u].x,t[l].x1,t[r].x1});
    t[u].y1=min({t[u].y,t[l].y1,t[r].y1});
    t[u].x2=max({t[u].x,t[l].x2,t[r].x2});
    t[u].y2=max({t[u].y,t[l].y2,t[r].y2});
}
void flatten(int u){//替罪羊树思想：不平衡时拍平子树重构
    if(!u) return;
    cur_nodes[node_cnt++]=u;
    flatten(t[u].l);
    flatten(t[u].r);
}
int build(int l,int r,int dim){
    if(l>r) return 0;
    int mid=(l+r)>>1;
    if(dim==0){
        nth_element(cur_nodes+l,cur_nodes+mid,cur_nodes+r+1,cmpx);
    }
    else{
        nth_element(cur_nodes+l,cur_nodes+mid,cur_nodes+r+1,cmpy);
    }
    int u=cur_nodes[mid];
    t[u].l=build(l,mid-1,dim^1);
    t[u].r=build(mid+1,r,dim^1);
    push_up(u);
    return u;
}
void insert(int &u,int p,int dim){
    if(!u){
        u=p;
        push_up(u);
        return;
    }
    if(dim==0){
        if(t[p].x<t[u].x){
            insert(t[u].l,p,dim^1);
        }
        else{
            insert(t[u].r,p,dim^1);
        }
    }
    else{
        if(t[p].y<t[u].y){
            insert(t[u].l,p,dim^1);
        }
        else{
            insert(t[u].r,p,dim^1);
        }
    }
    push_up(u);
    if(t[u].size*alpha<max(t[t[u].l].size,t[t[u].r].size)){
        node_cnt=0;
        flatten(u);
        u=build(0,node_cnt-1,dim);
    }
}
int query(int u,int x1,int y1,int x2,int y2){
    if(!u) return 0;
    if(t[u].x1>=x1 && t[u].y1>=y1 && t[u].x2<=x2 && t[u].y2<=y2){
        return t[u].sum;
    }
    if(t[u].x2<x1 || t[u].y2<y1 || t[u].x1>x2 || t[u].y1>y2){
        return 0;
    }
    int res=0;
    if(t[u].x>=x1 && t[u].x<=x2 && t[u].y>=y1 && t[u].y<=y2){
        res+=t[u].v;
    }
    res+=query(t[u].l,x1,y1,x2,y2);
    res+=query(t[u].r,x1,y1,x2,y2);
    return res;
}
int main(){
    t[0].x1=t[0].y1=2e9;
    t[0].x2=t[0].y2=-2e9;
    t[0].sum=t[0].size=0;
    int n;
    scanf("%d",&n);
    int op;
    int last_ans=0;
    while(scanf("%d",&op) && op!=3){
        if(op==1){
            int x,y,A;
            scanf("%d %d %d",&x,&y,&A);
            x^=last_ans;
            y^=last_ans;
            A^=last_ans;
            tot++;
            t[tot].x=x;
            t[tot].y=y;
            t[tot].v=t[tot].sum=A;
            insert(root,tot,0);
        }
        else if(op==2){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            x1^=last_ans;
            y1^=last_ans;
            x2^=last_ans;
            y2^=last_ans;
            last_ans=query(root,x1,y1,x2,y2);
            printf("%d\n",last_ans);
        }
    }
}