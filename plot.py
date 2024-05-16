#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 定义距离误差范围
dist_err_soft = np.linspace(-0.1, 0.1, 1000)

# 定义软障碍物的参数
r = 0.15
rsqr = r * r

# 计算平滑函数的值
term = np.sqrt(((1 + dist_err_soft**2 / rsqr) -1)* rsqr)

# 绘制图像
plt.plot(dist_err_soft, term, label='Smooth Function')
plt.xlabel('Distance Error')
plt.ylabel('Term Value')
plt.title('Smooth Function vs. Distance Error')
plt.grid(True)
plt.legend()
plt.show()