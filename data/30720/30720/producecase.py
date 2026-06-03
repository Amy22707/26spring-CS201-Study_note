import random
import time
import os
from collections import deque

# 确保 data 目录存在
os.makedirs("data", exist_ok=True)

class Node:
    __slots__ = ['val', 'win', 'left', 'right', 'parent']
    def __init__(self, v=0):
        self.val = v      # 内部节点存储：败者 (Loser)
        self.win = v      # 内部节点存储：该场胜者 (Winner)
        self.left = None
        self.right = None
        self.parent = None

def solve_logic(n, m, vals, updates):
    """ac.py 的逻辑实现，用于生成 .out 文件"""
    leaves = [Node(v) for v in vals]
    queue = deque(leaves)
    
    # 1. 初始构建树
    while len(queue) > 1:
        l = queue.popleft()
        r = queue.popleft()
        match = Node()
        match.val, match.win = max(l.win, r.win), min(l.win, r.win)
        match.left, match.right = l, r
        l.parent = r.parent = match
        queue.append(match)
    
    battle_root = queue.popleft()
    root = Node(battle_root.win)
    root.left, battle_root.parent = battle_root, root

    # 确定内部节点顺序
    internal_nodes = []
    bfs_q = deque([root])
    while bfs_q and len(internal_nodes) < n:
        curr = bfs_q.popleft()
        internal_nodes.append(curr)
        if curr.left: bfs_q.append(curr.left)
        if curr.right: bfs_q.append(curr.right)

    result_lines = []
    result_lines.append(" ".join(str(node.val) for node in internal_nodes))

    # 2. 修改逻辑
    for idx, new_val in updates:
        curr_leaf = leaves[idx]
        curr_leaf.win = new_val
        p = curr_leaf.parent
        while p:
            if p.right: # 普通比赛节点
                p.val = max(p.left.win, p.right.win)
                p.win = min(p.left.win, p.right.win)
            else:       # 顶层冠军节点
                p.val = p.win = p.left.win
            p = p.parent
        result_lines.append(" ".join(str(node.val) for node in internal_nodes))
    
    return result_lines

# --- 数据生成核心循环 ---
for epoch in range(30):
    # 题目指出 n 通常为 2 的幂次
    # 我们生成一些 2的幂次，也生成一些普通的数进行鲁棒性测试
    if epoch < 20:
        n = 2 ** random.randint(1, 10) # 2 到 1024
    else:
        n = random.randint(2, 1000)
    
    # 控制 m 的大小，防止 n*m 过大导致文件过巨
    # 限制总输出量在 2*10^6 个整数左右
    max_m = 2000000 // n
    m = random.randint(0, min(max_m, 1000))
    
    # 初始数组元素
    vals = [random.randint(0, 10000) for _ in range(n)]
    
    # 生成 m 个修改操作 (idx, val)
    updates = []
    for _ in range(m):
        u_idx = random.randint(0, n - 1)
        u_val = random.randint(0, 10000)
        updates.append((u_idx, u_val))

    # 写入输入文件 (.in)
    with open(f"data/{epoch}.in", "w") as f:
        f.write(f"{n} {m}\n")
        f.write(" ".join(map(str, vals)) + "\n")
        for u in updates:
            f.write(f"{u[0]} {u[1]}\n")

    start_time = time.time()

    # 调用逻辑生成输出内容
    result = solve_logic(n, m, vals, updates)

    elapsed = time.time() - start_time
    print(f"[{epoch}] {elapsed:.3f}s | n={n}, m={m}")

    # 写入输出文件 (.out)
    with open(f"data/{epoch}.out", "w") as f:
        f.write("\n".join(result) + "\n")

print("\n数据生成完毕，存放在 data/ 目录下。")
