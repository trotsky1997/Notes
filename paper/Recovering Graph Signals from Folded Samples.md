[toc]

|     Name | stage 1    |   stage2   |stage3|
| ---- | ---- | ---- |---- |
| Recovering Graph Signals from Folded Samples |  |      ||
|      |      |      ||
|      |      |      ||

# Recovering Graph Signals from Folded Samples



# neural tangent kernel

初始化时，人工神经网络（ANN）等效于高斯
无限宽度限制（16; 4; 7; 13; 6）中的进程，因此将它们连接到
内核方法。我们证明了训练过程中神经网络的发展也可以
用内核来描述：在ANN参数的梯度下降过程中，
网络函数f（将输入向量映射到输出向量）遵循
功能成本的核梯度（与参数相反，是凸的）
成本）一个新的内核：神经正切内核（NTK）。这个内核是核心
描述人工神经网络的一般化特征。而NTK在
初始化并在训练过程中变化，在无穷大限制内收敛
到一个明确的极限内核，并且在训练过程中保持不变。这使它
有可能在功能空间而不是参数空间中研究ANN的训练。
然后，训练的收敛性可以与训练的正定性相关。
限制NTK。我们证明了极限NTK的正定性
球体上支持数据，并且非线性是非多项式的。
然后，我们将重点放在最小二乘回归的设置上，并证明它在无限宽
极限时，网络函数f遵循线性微分方程
训练。沿着最大的内核主要组件，收敛最快
关于NTK的输入数据，因此暗示了理论动机
尽早停止。
最后，我们对NTK进行数值研究，观察其在宽网络中的行为，
并将其与无限宽度限制进行比较。

#图上的信号恢复：变化最小化

我们考虑信号恢复的问题
图。图形化具有复杂结构的模型数据作为信号
图。图形信号恢复可恢复一个或多个平滑
从嘈杂，损坏或不完整的测量结果中绘制图形信号。
我们将图形信号恢复公式化为优化问题，
为此，我们通过交替提供了一个通用的解决方案
==乘数的方向方法==。我们展示了信号修复
矩阵完成，强大的主成分分析和
异常检测均与图形信号恢复有关，并提供
相应的具体解决方案和理论分析。我们
验证有关实际恢复问题的建议方法，
包括在线博客分类，桥梁条件识别，
温度估算，笑话推荐系统，以及
在线博客分类的专家意见组合。

图形上的信号处理，信号恢复，
矩阵完成，半监督学习





#Mish: A Self Regularized Non-Monotonic Neural Activation Function

Mish takes inspiration from Swish by using a property called Self Gating, where the scalar input is provided to the gate. The property of Self-gating is advantageous for replacing activation functions like ReLU (point-wise functions) which take in a single scalar input without requiring to change the network parameters.