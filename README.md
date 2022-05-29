# fast-map-dpp

Fast Greedy MAP Inference for DPP
字节算法课第四次作业，加上了beemsearch
进行10000次模拟实验，每次随机生成100个向量和得分
因为暴力枚举是$C_{100}^8$可能最优解不好找，准确度不好得到
因为打散要求是对所选视频的得分越高和相似度小，根据论文所得，等价于$L_y$矩阵行列式，就对所得结果求一个行列式的值作为得分，越大越好
进行了greedy search和beemsize为2-8的beemsearch平均时间与得分的测试

# 实验结果:

algorithm running avg time:    8.9605e-05
algorithm running avg score:   2.8749e+01
beem2 algorithm running avg time:  1.0404e-03
beem2 algorithm running avg score:     2.8791e+01
beem3 algorithm running avg time:  1.4780e-03
beem3 algorithm running avg score:     2.8816e+01
beem4 algorithm running avg time:  1.9442e-03
beem4 algorithm running avg score:     2.8822e+01
beem5 algorithm running avg time:  2.3832e-03
beem5 algorithm running avg score:     2.8832e+01
beem6 algorithm running avg time:  2.8122e-03
beem6 algorithm running avg score:     2.8835e+01
beem7 algorithm running avg time:  3.2898e-03
beem7 algorithm running avg score:     2.8841e+01
beem8 algorithm running avg time:  3.7506e-03
beem8 algorithm running avg score:     2.8846e+01

# 结论

发现beemsearch2时间复杂度比greedy高10倍，可能我写的代码常数太大了
理论上greedy时间复杂度是$O(n^2m)$
beem是他乘一个常数beem的个数
发现每多一个束时间多接近0.5e-3秒,得分也在不断增高，实验结果可以接受

[Paper Link](http://papers.nips.cc/paper/7805-fast-greedy-map-inference-for-determinantal-point-process-to-improve-recommendation-diversity)
