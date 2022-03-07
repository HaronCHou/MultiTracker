"""
Author: Zhou Chen
Date: 2020/3/27
Desc: 使用卡尔曼滤波进行状态预测
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# 创建位置观测矩阵，表示0-99的位移
z_observed = np.arange(100)
# 创建高斯噪声矩阵
z_noise = np.random.normal(0, 1, 100)
z = z_observed + z_noise
# 创建初始状态矩阵X
x = np.array([[0, ], [0, ]])
# 创建初始状态协方差矩阵P，这里的1也可以是一个较为合适的较大数字
p = np.array([[1, 0], [0, 1]])
# 创建状态转移矩阵，采样频率为1秒，所以△t为1
f = np.array([[1, 1], [0, 1]])
# 创建状态转移协方差矩阵，协方差较小
q = np.array([[1e-6, 0], [0, 1e-6]])
# 创建观测矩阵
h = np.mat([1, 0])
# 创建观测噪声的协方差矩阵
r = np.mat([1])

for i in range(100):
    # 迭代，计算5大步骤
    x_predict = f * x
    p_predict = f * p * f.T + q
    kalman = (p_predict * h.T) / (h * p_predict * h.T + r)
    x = x_predict + kalman * (z[i] - h * x_predict)
    p = (np.eye(2) - kalman * h) * p_predict
    plt.plot(x[0, 0], x[1, 0], 'bo')

plt.xlabel("location")
plt.ylabel("speed")
plt.savefig("rst.png")
plt.show()
