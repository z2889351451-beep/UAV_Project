import paho.mqtt.client as mqtt
import pygame, random, csv
import numpy as np
from chaos_encrypt import chaos_encrypt   # 引入混沌加密模块

# ---------------------------
# MQTT 初始化
# ---------------------------
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "uav/encrypted"
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

# ---------------------------
# 窗口参数
# ---------------------------
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UAV Simulation")

# ---------------------------
# 无人机类
# ---------------------------
class Drone:
    def __init__(self):
        self.x, self.y = WIDTH//2, HEIGHT//2
        self.speed = 3

    def move(self):
        dx, dy = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.x = np.clip(self.x + dx*self.speed, 0, WIDTH)
        self.y = np.clip(self.y + dy*self.speed, 0, HEIGHT)
        temp = 20 + random.random()*5
        return int(self.x), int(self.y), int(temp)

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), 5)

drone = Drone()
running = True
clock = pygame.time.Clock()

# 打开加密版 CSV（实时写入）
enc_file = open("encrypted_drone_data.csv", "w", newline="")
enc_writer = csv.writer(enc_file)

# ---------------------------
# 主循环
# ---------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    x, y, temp = drone.move()
    drone.draw()

    # 原始数据
    raw = [x, y, temp]

    # 混沌加密
    enc = chaos_encrypt(raw)

    # 写入加密数据到本地
    enc_writer.writerow(enc)

    # 🔥 每一帧发送加密数据到 MQTT 服务器
    msg = ",".join([str(a) for a in enc])
    client.publish(MQTT_TOPIC, msg)

    pygame.display.flip()
    clock.tick(30)

# ---------------------------
# 收尾
# ---------------------------
enc_file.close()
pygame.quit()
print("✅ 加密飞行数据已保存到 encrypted_drone_data.csv")