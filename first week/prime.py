import math

# --- 配置部分 ---
n = 100  # 这里设置你想筛选的上限，例如 100

# --- 核心算法 ---
# 1. 初始化一个布尔列表，假设所有数字都是素数
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False  # 0 和 1 不是素数<websource>source_group_web_1</websource>

# 2. 开始筛选，只需检查到 sqrt(n)
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:  # 如果 i 是素数
        # 将 i 的所有倍数（从 i*i 开始）标记为非素数
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# 3. 收集所有仍被标记为 True 的数字
primes = [i for i in range(2, n + 1) if is_prime[i]]

# --- 输出结果 ---
print(f"{n} 以内的素数有：")
print(primes)