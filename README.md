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
- 更多的easy例子参考：https://blog.csdn.net/haronchou/article/details/123335750
  - python源代码，以及主要的参数的改变会带来哪些影响？

# 2. 实际的一些问题

## 2.1 在低帧率low-fps中如何确保收敛性的？以及需要多少帧可以收敛？

## 2.2 在未收敛时，不可靠的检测(如目标交错时)会带来哪些影响？

## 2.3 如何进一步踢出明显的错误匹配

- **什么是错误匹配？**
  - 就是虽然ID和检测匹配了，但是由于距离计算的metric不鲁棒，他俩的距离计算出来很小。
  - 或者是，metric计算的距离也不小，但是匈牙利由于别的误差太大，显得这俩的距离小，又想尽量匹配，就强行匹配了。
  - **现象：就是折线的轨迹很多，明显不合理**
  - **远离：就是匈牙利的阈值取的太大！！！**

## 2.4 yolo如何与kalman结合起来，效果怎样？

## 2.5 粒子滤波的例子如何？与kalman比较优劣？





