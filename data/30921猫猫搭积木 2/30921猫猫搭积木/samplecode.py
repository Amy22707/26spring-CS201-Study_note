import sys

def solve():
    # 快速读取所有输入
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = next(iterator)
    q = next(iterator)
    s = next(iterator)
    
    # 初始化并查集
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    elements = [[i] for i in range(n + 1)]
    
    piles = n
    out = []
    
    for _ in range(q):
        u = next(iterator)
        v = next(iterator)
        
        r_u = parent[u]
        r_v = parent[v]
        
        if r_u != r_v:
            sz_u = size[r_u]
            sz_v = size[r_v]
            
            # 判断是否崩塌
            if sz_u + sz_v >= s:
                piles += sz_u + sz_v - 2
                # 拆散堆 r_u 里的积木
                for x in elements[r_u]:
                    parent[x] = x
                    size[x] = 1
                    elements[x] = [x]
                # 拆散堆 r_v 里的积木
                for x in elements[r_v]:
                    parent[x] = x
                    size[x] = 1
                    elements[x] = [x]
            else:
                piles -= 1
                # 启发式合并：将小的堆合并到大的堆中
                if sz_u < sz_v:
                    for x in elements[r_u]:
                        parent[x] = r_v
                    elements[r_v].extend(elements[r_u])
                    size[r_v] += sz_u
                    elements[r_u] = []
                else:
                    for x in elements[r_v]:
                        parent[x] = r_u
                    elements[r_u].extend(elements[r_v])
                    size[r_u] += sz_v
                    elements[r_v] = []
        
        out.append(str(piles))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
