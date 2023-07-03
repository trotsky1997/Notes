ROS:

#ROS简介

![image-20200721170111377](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721170111377.png)

![image-20200721161107152](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161107152.png)



ROS 资 源 是 如 何 分
布 式 管 理 的 

程 序 文 件 是 如 何 组
织 和 构 建 的 

描 述 程 序 是 如 何
运 行 的


![image-20200721161258780](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161258780.png)

## 计算图

通过计算图的消息同步完成通信

![image-20200721161324544](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161324544.png)(1) 节 点 (Node) 一 一 软 件 模 块

(2) 节 点 管 理 器 (ROS Master) 一 一 控 制 中 心 , 提 供 参 数 管 理
(3) 话 题 (Topic) 一 一 异 步 通 信 机 制 , 传 输 消 息 (Message)
(4) 服 务 (Service) 一 一 同 步 通 信 机 制 , 传 输 请 求 / 应 答 数 据


![image-20200721161403386](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161403386.png)

![image-20200721161414813](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161414813.png)

服务模型:双向同步的C/S模型

## 通信机制

1.  话题

![image-20200721161540811](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161540811.png)

![image-20200721161553677](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161553677.png)

2.  服务通信

    ![image-20200721161709013](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161709013.png)

![image-20200721161720143](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161720143.png)

3.参数通信

![image-20200721161756619](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161756619.png)

![image-20200721161809067](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161809067.png)

![image-20200721161832628](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721161832628.png)

4.文件系统:

![image-20200721162304040](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721162304040.png)

![image-20200721162333357](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721162333357.png)

1. 功 能 包 清 单 (Package manifest) : 记 录 功 能 包 的 基 本
信 息 , 包 含 作 者 信 息 、 许 可 信 息 、 依 赖 选 项 、 编 译 标 志 等 。

2. 元 功 能 包 (Meta Packages) ; 组 织 多 个 用 于 同 一 目 的
功 能 包 。

3. 元 功 能 包 清 单 (Meta Packages) : 类 似 于 功 能 包 清 单 ,
不 同 之 处 在 于 元 功 能 包 清 单 中 可 能 会 包 含 运 行 时 需 要 依 赖 的
功 能 包 或 者 声 明 一 些 引 用 的 标 签 。

4. 消 息 类 型 (Message) : 消 息 是 ROS 节 点 之 间 发 布 / 订 阅
的 通 信 信 息 , 可 以 使 用 ROS 系 统 提 供 的 消 息 类 型 , 也 可 以 使
用 .msg 文 件 在 功 能 包 的 msg 文 件 夹 下 自 定 义 需 要 的 消 息 类 型 。

5. 服 务 类 型 (Service) : 服 务 类 型 定 义 了 ROS 服 务 器 / 客户 端 通 信 模 型 下 的 请 求 与 应 答 数 据 类 型 , 可 以 使 用 ROS 系 统提供的服务类型, 也 可 以 使 用 .srv 文 件 在 功 能 包 的 srv 文 件 夹
    进 行 定 义 。

6. 代 码 (Code) : 放 置 功 能 包 节 点 源 代 码 的 文 件 夹 。

![image-20200721162456200](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721162456200.png)

![image-20200721164307738](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721164307738.png)

##小海龟

![image-20200721165826921](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721165826921.png)

应用框架

![image-20200721165926612](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721165926612.png)

![image-20200721170456517](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721170456517.png)

# ROS简介

![image-20200721183922196](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721183922196.png)

![image-20200721195120364](C:\Users\admintrato\AppData\Roaming\Typora\typora-user-images\image-20200721195120364.png)





































$\begin{aligned}
\mathrm{S}_{2}(\mathrm{X}) &=\|\mathrm{X}-\mathrm{A} \mathrm{X}\|_{F}^{2} \stackrel{(a)}{=}\left\|(\mathrm{I}-\mathrm{A}) \mathrm{U} \Sigma \mathrm{Q}^{*}\right\|_{F}^{2} \\
&=\operatorname{Tr}\left(\mathrm{Q} \Sigma \mathrm{U}^{*}(\mathrm{I}-\mathrm{A})^{*}(\mathrm{I}-\mathrm{A}) \mathrm{U} \Sigma \mathrm{Q}^{*}\right) \\
& \stackrel{(b)}{=} \operatorname{Tr}\left(\Sigma \mathrm{U}^{*}(\mathrm{I}-\mathrm{A})^{*}(\mathrm{I}-\mathrm{A}) \mathrm{U} \Sigma \mathrm{Q}^{*} \mathrm{Q}\right) \\
&=\|(\mathrm{I}-\mathrm{A}) \mathrm{U} \Sigma\|_{F}^{2} \stackrel{(c)}{=} \sum_{i=1}^{r} \sigma_{i}^{2}\left\|(\mathrm{I}-\mathrm{A}) \mathbf{u}_{i}\right\|_{2}^{2}
\end{aligned}$











