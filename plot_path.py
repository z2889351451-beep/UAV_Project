import pandas as pd
import matplotlib.pyplot as plt

# 读取无人机飞行数据
data = pd.read_csv("drone_data.csv")

# x 是横坐标，y 是纵坐标
x = data["x"]
y = data["y"]

# 绘制路径图
plt.figure(figsize=(6,5))
plt.plot(x, y, "-b", linewidth=1)
plt.title("UAV Flight Path")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.grid(True)
plt.show()
