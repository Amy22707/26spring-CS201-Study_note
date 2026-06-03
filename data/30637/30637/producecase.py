import random
import time
import os

# 确保 data 目录存在
os.makedirs("data", exist_ok=True)

def is_valid_pop_sequence(origin, output):
    """AC代码中的逻辑，用于生成.out文件"""
    if len(origin) != len(output):
        return False
    stack = []
    bank = list(origin)
    for char in output:
        while (not stack or stack[-1] != char) and bank:
            stack.append(bank.pop(0))
        if not stack or stack[-1] != char:
            return False
        stack.pop()
    return True

def generate_valid_sequence(origin):
    """通过模拟栈操作 100% 生成一个合法的出栈序列"""
    stack = []
    bank = list(origin)
    result = []
    while bank or stack:
        # 随机决定是入栈还是出栈
        # 0: 入栈 (如果bank不为空), 1: 出栈 (如果stack不为空)
        choices = []
        if bank: choices.append(0)
        if stack: choices.append(1)
        
        op = random.choice(choices)
        if op == 0:
            stack.append(bank.pop(0))
        else:
            result.append(stack.pop())
    return "".join(result)

# 可选字符集
chars_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for epoch in range(30):
    # 1. 随机生成原始字符串 x (长度 1-62, 无重复)
    x_len = random.randint(1, 62)
    x_list = random.sample(chars_pool, x_len)
    origin_str = "".join(x_list)

    # 2. 随机生成若干待测试字符串 (不超过50行)
    test_cases = []
    num_tests = random.randint(5, 50)
    
    for _ in range(num_tests):
        rand_val = random.random()
        if rand_val < 0.4:
            # 40% 概率生成绝对正确的序列
            test_cases.append(generate_valid_sequence(origin_str))
        elif rand_val < 0.7:
            # 30% 概率生成长度相同但乱序的序列 (大概率为 NO)
            temp = list(origin_str)
            random.shuffle(temp)
            test_cases.append("".join(temp))
        elif rand_val < 0.9:
            # 20% 概率生成长度随机、字符随机的序列
            other_len = random.randint(1, min(100, x_len + 10))
            test_cases.append("".join(random.choices(chars_pool, k=other_len)))
        else:
            # 10% 边界情况：空串或极短串
            test_cases.append("".join(random.choices(origin_str, k=random.randint(0, 2))))

    # 写入输入文件 (.in)
    with open(f"data/{epoch}.in", "w") as f:
        f.write(origin_str + "\n")
        for line in test_cases:
            f.write(line + "\n")

    start = time.time()

    # 计算结果并写入输出文件 (.out)
    results = []
    for case in test_cases:
        if is_valid_pop_sequence(origin_str, case):
            results.append("YES")
        else:
            results.append("NO")

    end = time.time() - start
    print(f"[{epoch}] {end:.3f}s | origin_len={x_len}, queries={num_tests}")

    with open(f"data/{epoch}.out", "w") as f:
        if results:
            f.write("\n".join(results) + "\n")
