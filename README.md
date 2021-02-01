# MultiTracker
VIBE+Kalman+KM

主要框架参考： https://github.com/Smorodov/Multitarget-tracker
其中差异的地方：距离计算部分
- 使用的是马氏距离，用errCovPre来作为协方差（而不是errCovPost）。
- 同时输入匈牙利算法的部分也是不一样的。
- 然后距离阈值用了8，而不是20；
- 还加入了visibility的部分
- 再加入工程代码中还额外统一了接口
