from chaos_encrypt import chaos_encrypt
import numpy as np
import random

# 环境：20x20 网格
size = 20
goal = (18, 18)
actions = [(1,0), (-1,0), (0,1), (0,-1)]  # 右 左 下 上

Q = np.zeros((size, size, 4))
alpha, gamma, eps = 0.1, 0.9, 0.1

def train(episodes=5000):
    for _ in range(episodes):
        x, y = 1, 1
        while (x, y) != goal:
            if random.random() < eps:
                a = random.randint(0,3)
            else:
                a = np.argmax(Q[x,y])

            dx, dy = actions[a]
            nx, ny = np.clip(x+dx, 0, size-1), np.clip(y+dy, 0, size-1)

            reward = 10 if (nx, ny) == goal else -1

            Q[x,y,a] += alpha*(reward + gamma*np.max(Q[nx,ny]) - Q[x,y,a])
            x, y = nx, ny

train()
print("AI 训练完成！你现在有一个会找目标的无人机导航模型")
def test():
    print("测试AI导航路径：")
    x, y = 1, 1
    steps = 0
    path = [(x,y)]

    while (x,y) != goal and steps < 200:
        a = np.argmax(Q[x,y])  # 选择最佳动作
        dx, dy = actions[a]
        x, y = np.clip(x+dx, 0, size-1), np.clip(y+dy, 0, size-1)
        path.append((x,y))
        steps += 1

    print(path)
    print("步数:", steps)

test()
import numpy as np
import random
import matplotlib.pyplot as plt

# --- 无人机 Q-learning 环境 ---
size = 20               # 20x20 网格
goal = (18, 18)         # 终点
start = (1, 1)          # 起点

actions = [(1,0), (-1,0), (0,1), (0,-1)]   # 右 左 下 上
Q = np.zeros((size, size, 4))

alpha = 0.1    # 学习率
gamma = 0.9    # 折扣因子
eps = 0.1      # 探索概率

# --- 训练过程 ---
def train(episodes=5000):
    for _ in range(episodes):
        x, y = start
        while (x, y) != goal:
            # 选择动作（探索或利用）
            if random.random() < eps:
                a = random.randint(0,3)
            else:
                a = np.argmax(Q[x,y])

            dx, dy = actions[a]
            nx, ny = np.clip(x+dx, 0, size-1), np.clip(y+dy, 0, size-1)

            # 奖励
            reward = 10 if (nx, ny) == goal else -1

            # Q-learning 更新
            Q[x,y,a] += alpha * (reward + gamma*np.max(Q[nx,ny]) - Q[x,y,a])

            x, y = nx, ny

# --- 测试 & 可视化路径 ---
def test_and_visualize():
    x, y = start
    path = [(x,y)]
    steps = 0

    # 使用 Q 表导航
    while (x,y) != goal and steps < 300:
        a = np.argmax(Q[x,y])
        dx, dy = actions[a]
        x, y = np.clip(x+dx, 0, size-1), np.clip(y+dy, 0, size-1)
        path.append((x,y))
        steps += 1

    print("AI 导航完成！步数：", steps)

    # --- 将路径转换为一维整数序列 ---
    flat_path = []
    for (px, py) in path:
        flat_path.extend([px, py])  # 展开成 [x1,y1,x2,y2,...]

    # --- 加密路径 ---
    encrypted_path = chaos_encrypt(flat_path)

    # 保存加密路径
    with open("encrypted_ai_path.csv", "w") as f:
        for val in encrypted_path:
            f.write(str(val) + ",")

    print("🔐 AI 路径已成功加密并保存到 encrypted_ai_path.csv")

    # --- 可视化绘图 ---
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    plt.figure(figsize=(6,6))
    plt.plot(xs, ys, '-o', markersize=3, label="AI Path")
    plt.scatter(start[0], start[1], c='green', s=100, label="Start")
    plt.scatter(goal[0], goal[1], c='red', s=100, label="Goal")

    plt.title("Q-learning UAV Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- 主流程 ---
train()
print("AI 训练完成！")
test_and_visualize()