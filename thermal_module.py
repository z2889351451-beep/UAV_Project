# thermal_module.py
import numpy as np

def generate_thermal_grid(drone_x, drone_y, width, height, grid_size=16):
    """
    生成一个模拟的 16x16 热成像矩阵
    - drone_x, drone_y: 无人机当前在屏幕上的坐标
    - width, height: 窗口大小（和 pygame 一致）
    - grid_size: 热成像分辨率（默认 16x16）
    """

    # 基础温度（比如环境温度）
    base_temp = 25.0

    # 创建网格
    grid = np.zeros((grid_size, grid_size), dtype=float)

    # 无人机在网格中的位置（大概映射一下）
    gx = int(drone_x / width * (grid_size - 1))
    gy = int(drone_y / height * (grid_size - 1))

    for i in range(grid_size):
        for j in range(grid_size):
            # 距离无人机越近温度越高，简单用距离反比模拟
            dist = np.sqrt((i - gx) ** 2 + (j - gy) ** 2)
            # 距离小 → 温度高，给一个衰减
            temp = base_temp + 30 * np.exp(- (dist ** 2) / 10)
            grid[i, j] = temp

    return grid


if __name__ == "__main__":
    # 简单测试
    g = generate_thermal_grid(drone_x=100, drone_y=150, width=800, height=600)
    print("热成像矩阵形状:", g.shape)
    print(g)