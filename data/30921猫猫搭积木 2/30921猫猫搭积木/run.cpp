#include<cstdio>
#include<cstdlib>
int main() {
    int l,r;
    scanf("%d%d",&l,&r);
    char cmd[256];
    for (int x=l;x<=r;x++)
    {
//        sprintf(cmd,"data.exe>test%02d.in", x);
//        system(cmd);
	    sprintf(cmd,"deepseek.exe<test%02d.in>test%02d.ans",x,x);
	    system(cmd);
        sprintf(cmd,"fc test%02d.out test%02d.ans",x,x);
        system(cmd);
    }
    return 0;
}
//0 example
//1-9 n 2-10 q 10 s 2-(n+1)
//10-19 n 2-100 q 5000 s 2-(n+1)
//20-29 n 500 q 500000 s 2-(n+1)
//30-34 n 100000 q 500000 s 2-10
//35-39 n 100000 q 500000 s 11-9999
//40-44 n 100000 q 500000 s 10000-(n+1)
//45 n 100000 q 499995 s 5 a link
//46 n 100000 q 499995 s 1000 a link
//47 n 100000 q 499995 s 10000 a link
//48 n 100000 q 499500 s 1000 links of 1000 points(merge in same time)
//49 n 100000 q 495000 s 10000 links of 10000 points(merge in same time)