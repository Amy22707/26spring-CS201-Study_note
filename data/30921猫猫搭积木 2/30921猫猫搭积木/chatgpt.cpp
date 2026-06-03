#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q, k;
    cin >> n >> q >> k;

    vector<int> fa(n + 1), sz(n + 1);
    vector<vector<int>> mem(n + 1);

    for (int i = 1; i <= n; i++) {
        fa[i] = i;
        sz[i] = 1;
        mem[i].push_back(i);
    }

    int comp = n;

    function<int(int)> find = [&](int x) {
        return fa[x] == x ? x : fa[x] = find(fa[x]);
    };

    auto collapse = [&](int root) {
        for (int u : mem[root]) {
            fa[u] = u;
            sz[u] = 1;
            mem[u].clear();
            mem[u].push_back(u);
        }
    };

    while (q--) {
        int x, y;
        cin >> x >> y;

        int fx = find(x), fy = find(y);

        if (fx != fy) {
            // union
            if (sz[fx] < sz[fy]) swap(fx, fy);

            // merge fy into fx
            for (int u : mem[fy]) {
                mem[fx].push_back(u);
            }
            mem[fy].clear();

            fa[fy] = fx;
            sz[fx] += sz[fy];

            if (sz[fx] > k) {
                collapse(fx);
                comp += (int)mem[fx].size() - 1; // 其实直接重算也行
            } else {
                comp--;
            }
        }

        cout << comp << "\n";
    }

    return 0;
}