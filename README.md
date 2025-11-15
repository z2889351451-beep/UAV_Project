AI-Driven UAV Bionic Patrol System with Reinforcement Learning, Chaos Encryption, and Thermal Sensing

Fei Tianle · 2025


---

Abstract

This project presents an integrated AI-driven UAV bionic patrol system combining:

Reinforcement Learning (Q-learning) for autonomous navigation

Chaos-based lightweight encryption for secure telemetry

Thermal sensing simulation for environmental perception

Real-time UAV simulation using Python and Pygame


The design aligns closely with the research directions of Prof. Kim Gi-Il (김기일), including chaotic cryptography, lightweight IoT security, secure messaging protocols, and intelligent autonomous systems.
This project can serve as a strong foundation for graduate-level research in UAV intelligence and lightweight cryptography.


---

1. Introduction

Unmanned Aerial Vehicles (UAVs) are widely used in surveillance, patrolling, and remote monitoring.
However, three core challenges remain:

1. Autonomous decision-making


2. Lightweight real-time security for telemetry


3. Environmental sensing (e.g., thermal information)



This project develops a modular prototype addressing these challenges via:

AI-based navigation

Chaos-encrypted communication

Thermal sensing

Real-time UAV simulation



---

2. Relevance to Prof. Kim Gi-Il’s Research

Project Component	Related Research Topic	Connection

Chaos Encryption	Tent–Sine S-box chaotic design	Logistic-map XOR encryption is a lightweight chaotic cipher aligned in concept
IoT/MQTT Messaging	Secure SMS / IoT delivery	UAV telemetry uses encrypted lightweight messaging similar to IoT protocols
Reinforcement Learning	UAV path optimization	Directly related to autonomous aviation and control systems
Thermal Sensing	IoT sensing & anomaly detection	Matches intelligent sensor processing topics
UAV Simulation	Applied Sciences UAV modeling	Strong overlap with UAV decision & patrol systems



---

3. System Architecture

┌──────────────────────────────────────────────┐
│ Cloud / Research Layer                        │
│  • Reinforcement Learning Policy              │
│  • Data Analysis & Visualization              │
│  • Model Training                             │
└──────────────────────────────────────────────┘
                ▲
                │ Encrypted Telemetry (Chaos XOR)
                ▼
┌──────────────────────────────────────────────┐
│ Secure Transmission Layer                     │
│  • MQTT Publish                               │
│  • Chaos-based Lightweight Encryption         │
└──────────────────────────────────────────────┘
                ▲
                │ Raw + Thermal Data
                ▼
┌──────────────────────────────────────────────┐
│ UAV Simulation Layer                          │
│  • Pygame-based Real-time Motion              │
│  • Thermal Sensing Module                     │
│  • Bionic Flight Behavior                     │
└──────────────────────────────────────────────┘


---
4. Methodology

4.1 Autonomous Navigation (Q-Learning)

A 20×20 grid-world is used for learning an optimal patrol path.

Learning rate (α) = 0.1

Discount factor (γ) = 0.9

Exploration rate (ε) = 0.1


Reward Function

State	Reward

Goal	+10
Each Step	–1


The UAV successfully learns the optimal path from (1,1) → (18,18).


---

4.2 Chaos Encryption (Logistic Map XOR)

The chaotic sequence is generated:

x = 3.99 * x * (1 - x)
byte = int((x * 10000) % 256)
encrypted[i] = data[i] XOR byte

Advantages

Extremely lightweight

Hardware-friendly

Strong unpredictability

Compatible with UAV/IoT real-time bandwidth

Conceptually parallels Tent–Sine chaotic S-box models



---

4.3 Real-Time UAV Simulation

Features:

Bionic movement with random drift

Real-time 30 FPS visualization

Logging XY coordinates + temperature

Logging encrypted telemetry

Compatible with MQTT publishing



---

4.4 Thermal Sensing Module

A simple model:

temp = 20 + random.random() * 5

Future extensions include:

Infrared thermal imaging

Anomaly detection

Heat map estimation

CNN-based thermal classification



---

5. Experiments

5.1 Learned Path Visualization

A matplotlib-generated flight path confirms Q-learning convergence.

5.2 Encrypted Telemetry Example

x	y	temp	enc_x	enc_y	enc_temp

550	312	23	141	92	201


The encryption successfully transforms each telemetry value.


---

6. Results

The system achieves:

✔ Autonomous UAV navigation via Q-learning

✔ Chaos-encrypted telemetry

✔ Thermal sensing integration

✔ Real-time simulation

✔ Full architectural match with Prof. Kim’s research topics



---

7. Future Work

Recommended graduate-level extensions:

Deep Reinforcement Learning (DQN, PPO)

Tent–Sine chaotic S-box implementation

UAV swarm algorithms (PSO, BA)

GPS spoofing & cyberattack simulation

Thermal anomaly segmentation with CNNs



---

8. How to Run

Install Dependencies

pip install pygame numpy matplotlib paho-mqtt

Run UAV Simulation

python drone_sim.py

Run AI Navigation

python drone_ai.py

View Encrypted Data

encrypted_drone_data.csv


---

9. Contact

Fei Tianle
Email: 2889351451@qq.com
Applying for: Master’s Program, Chungnam National University (CNU)
Intended Advisor: Prof. Kim Gi-Il (김기일)
