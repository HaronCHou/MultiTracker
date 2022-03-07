# MultiTracker
[TOC]

VIBE+Kalman+KM

主要框架参考： https://github.com/Smorodov/Multitarget-tracker
其中差异的地方：距离计算部分

- 使用的是马氏距离，用errCovPre来作为协方差（而不是errCovPost）。
  距离计算公式参考：[『3.距离计算公式』](https://blog.csdn.net/haronchou/article/details/112649684)
- 同时输入匈牙利算法的部分也是不一样的。
- 然后距离阈值用了8，而不是20；
- 还加入了visibility的部分
- 再加入工程代码中还额外统一了接口

# 1. 简单demo运行

代码来源：https://www.cnblogs.com/tornadomeet/archive/2012/08/19/2646412.html

KalmanEasyDemo中的demo代码来源：

- 代码来源于：https://blog.csdn.net/onezeros/article/details/6318944 复制粘贴得到





