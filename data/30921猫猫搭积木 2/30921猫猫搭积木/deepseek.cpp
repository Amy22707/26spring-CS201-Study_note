#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 500005;

int parent[MAXN];   // 并查集父节点
int sz[MAXN];       // 仅对根有效，表示集合大小
int nxt[MAXN];      // 循环链表下一个节点
int prv[MAXN];      // 循环链表上一个节点
int total;          // 当前总堆数
int n, q, s;        // 积木数，操作次数，崩塌上限

// 并查集查找，带路径压缩（迭代版）
int find(int x) {
    int root = x;
    while (parent[root] != root) root = parent[root];
    // 路径压缩
    while (x != root) {
        int nxt_parent = parent[x];
        parent[x] = root;
        x = nxt_parent;
    }
    return root;
}

// 重置一个集合的所有元素为单块堆
void reset_set(int r) {
    int cur = r;
    do {
        int nxt_node = nxt[cur];
        parent[cur] = cur;
        sz[cur] = 1;
        nxt[cur] = cur;
        prv[cur] = cur;
        cur = nxt_node;
    } while (cur != r);
}

int main() {
    scanf("%d %d %d", &n, &q, &s);
    total = n;
    // 初始化：每块积木自成一堆，循环链表只包含自己
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
        sz[i] = 1;
        nxt[i] = i;
        prv[i] = i;
    }

    while (q--) {
        int x, y;
        scanf("%d %d", &x, &y);
        int rx = find(x);
        int ry = find(y);

        // 已在同一堆，操作无效
        if (rx == ry) {
            printf("%d\n", total);
            continue;
        }

        // 按大小合并，保证 rx 为较大集合
        if (sz[rx] < sz[ry]) {
            swap(rx, ry);
        }

        total -= 1;                 // 两堆合为一堆
        int new_sz = sz[rx] + sz[ry];

        if (new_sz >= s) {          // 触发崩塌
            total += new_sz - 1;    // 1 堆崩塌为 new_sz 堆
            reset_set(rx);
            reset_set(ry);
        } else {                    // 正常合并
            // 将 ry 的循环链表插入 rx 的链表中
            int rx_next = nxt[rx];
            int ry_last = prv[ry];
            nxt[rx] = ry;
            prv[ry] = rx;
            nxt[ry_last] = rx_next;
            prv[rx_next] = ry_last;

            // 并查集合并
            parent[ry] = rx;
            sz[rx] = new_sz;
        }

        printf("%d\n", total);
    }
    return 0;
}