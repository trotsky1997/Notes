# Denoising Diffusion Probabilistic Models
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|preprint|
> |标题|Denoising Diffusion Probabilistic Models|
> |短标题||
> |作者|[[Jonathan Ho]]、 [[Ajay Jain]]、 [[Pieter Abbeel]]|
> |期刊名称||
> |DOI||
> |存档位置||
> |馆藏目录|arXiv.org|
> |索书号||
> |版权||
> |分类||
> |条目链接|[My Library](zotero://select/library/items/HIEWLPRH)|
> |PDF 附件|<ul><li><a href="zotero://open-pdf/library/items/RZEREA2F">全文</a></li><li><a href="zotero://open-pdf/library/items/S3SYFGSM">Full Text PDF</a></li></ul>|
> |关联文献||
> ^Metadata

> [!example]- <center>本文标签</center>
> 
> `$=dv.current().file.tags`

> [!quote]- <center>Abstract</center>
> 
> We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

> [!tldr]- <center>隐藏信息</center>
> 
> itemType:: preprint
> title:: Denoising Diffusion Probabilistic Models
> shortTitle:: 
> creators:: [[Jonathan Ho]]、 [[Ajay Jain]]、 [[Pieter Abbeel]]
> publicationTitle:: 
> journalAbbreviation:: 
> volume:: 
> issue:: 
> pages:: 
> language:: 
> DOI:: 
> ISSN:: 
> url:: [http://arxiv.org/abs/2006.11239](http://arxiv.org/abs/2006.11239)
> archive:: 2023-07-12
> archiveLocation:: 
> libraryCatalog:: arXiv.org
> callNumber:: 
> rights:: 
> extra:: 🏷️ 📒、Computer Science - Machine Learning、Statistics - Machine Learning
> collection:: 
> tags:: #Done #Computer_Science_-_Machine_Learning #Statistics_-_Machine_Learning
> related:: 
> itemLink:: [My Library](zotero://select/library/items/HIEWLPRH)
> pdfLink:: <ul><li><a href="zotero://open-pdf/library/items/RZEREA2F">全文</a></li><li><a href="zotero://open-pdf/library/items/S3SYFGSM">Full Text PDF</a></li></ul>
> qnkey:: 2020_Ho_Denoising Diffusion _KEY-HIEWLPRH
> date:: 2020-12-16
> dateY:: 2020
> dateAdded:: 2023-07-09
> dateModified:: 2023-07-13
> 
> abstract:: We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https：//github.com/hojonathanho/diffusion


%--------------ω--------------%

## ✏️ 笔记区

> [!WARNING]+ <center>🐣 总结</center>  
>
>🎯 研究问题::  
🔎 研究背景::  
🚀 研究方法::  
🐔 研究思路::  
📺 主要内容::  
🎉 研究结论::  
🗝️ 创新点::  
💩 研究局限::  
🐾 研究展望::  
✏️ 备注::  

> [!inbox]- <center>📫 导入时间</center>
>
> ⏰ importDate:: 2023-07-10

%--------------ω--------------%

## 📝 注释笔记 RZEREA2F

> <span style="font-size: 15px;color: gray">📍 2020-Ho-Denoising Diffusion Probabilistic Models</span>

^KEYrefTitle

> <span class="highlight" style="background-color: #aaaaaa">This paper presents progress in diffusion probabilistic models [53]. A diffusion probabilistic model (which we will call a “diffusion model” for brevity) is a parameterized Markov chain trained using variational inference to produce samples matching the data after finite time. Transitions of this chain are learned to reverse a diffusion process, which is a Markov chain that gradually adds noise to the data in the opposite direction of sampling until signal is destroyed. When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for a particularly simple neural network parameterization.</span>  
> 🔤本文介绍了扩散概率模型的进展[53]。扩散概率模型（为简洁起见，我们将其称为“扩散模型”）是使用变分推理训练的参数化马尔可夫链，以在有限时间后生成与数据匹配的样本。该链的转换被学习以逆转扩散过程，这是一个马尔可夫链，在采样的相反方向上逐渐向数据添加噪声，直到信号被破坏。当扩散包含少量高斯噪声时，将采样链转换设置为条件高斯就足够了，从而允许特别简单的神经网络参数化。🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=DCFW8JM5))

^KEYDCFW8JM5

> <span class="highlight" style="background-color: #aaaaaa">Diffusion models are straightforward to define and efficient to train, but to the best of our knowledge, there has been no demonstration that they are capable of generating high quality samples. We show that diffusion models actually are capable of generating high quality samples, sometimes better than the published results on other types of generative models (Section 4). In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics during sampling (Section 3.2) [55, 61]. We obtained our best sample quality results using this parameterization (Section 4.2), so we consider this equivalence to be one of our primary contributions.</span>  
> 🔤扩散模型定义简单且训练高效，但据我们所知，尚无证据表明它们能够生成高质量样本。我们证明扩散模型实际上能够生成高质量的样本，有时比其他类型的生成模型已发布的结果更好（第 4 节）。此外，我们表明，扩散模型的某些参数化揭示了训练期间多个噪声水平上的去噪分数匹配以及采样期间退火的 Langevin 动力学的等价性（第 3.2 节）[55, 61]。我们使用此参数化（第 4.2 节）获得了最佳样本质量结果，因此我们认为这种等价性是我们的主要贡献之一。🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=QNWVV22F))

^KEYQNWVV22F

> <span class="highlight" style="background-color: #ffd400">pθ(x0) := ∫ pθ(x0:T ) dx1:T</span>  
> The equation you provided is a definition of the marginal probability density function, denoted as p_θ(x_0), for a specific variable x_0 in a continuous-time dynamic model. Let's break down the components of the equation:  
> - p_θ(x_0:T): This represents the joint probability density function of the variables x_0 through x_T, conditioned on the parameter values θ. It describes the probability distribution of the entire sequence of variables from x_0 to x_T.  
> - d𝐱_1:T: This represents an integration measure, indicating that we are integrating over the variables x_1 through x_T. It implies that we are integrating out these variables to obtain the marginal probability density function of x_0 alone.  
> - ∫ p_θ(x_0:T) d𝐱_1:T: This is the integration of the joint probability density function over the variables x_1 through x_T. By integrating, we obtain the probability of observing x_0 in isolation.  
> - p_θ(x_0): This represents the marginal probability density function of x_0 alone, which is obtained by integrating out the other variables.  
> In essence, the equation is defining how to obtain the probability distribution of x_0 alone by integrating the joint probability distribution over all the other variables. This is useful for understanding the probability distribution of individual variables in a dynamic system.  
> 🔤🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=MQAPEUMD))

^KEYMQAPEUMD

> <span class="highlight" style="background-color: #ffd400">variational bound</span>  
> 🔤变分界🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=2Q877BNK))

^KEY2Q877BNK

> <span class="highlight" style="background-color: #ffd400">negative log likelihood</span>  
> Negative log likelihood (NLL) is a mathematical measurement in statistics that is commonly used in maximum likelihood estimation (MLE). It is the negation of the logarithm of the likelihood function, which measures the probability of observing a set of data given a statistical model and its parameter values.  
> Formally, the negative log likelihood can be defined as:  
> NLL(θ) = -log(L(θ))  
> Where NLL is the negative log likelihood, θ represents the parameters of the statistical model, and L(θ) is the likelihood function. The likelihood function provides the probability of observing the given data under a specific set of parameter values.  
> The NLL is often used as a loss function to optimize the parameters of a model during the training process. The goal is to minimize the NLL, which indirectly maximizes the likelihood and improves the model's fit to the data.  
> In summary, the negative log likelihood is a measure of the discrepancy between the observed data and the predictions of a statistical model, and it is commonly used in maximum likelihood estimation and model training.  
> 🔤负对数似然🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=9HAXZ52Q))

^KEY9HAXZ52Q

> <span class="highlight" style="background-color: #ffd400">q(xt|x0) = N (xt; √ ̄ αtx0, (1 − ̄ αt)I)</span>  
> 这一步是通过对于正向过程进行条件概率的建模得出的。根据上下文信息中的方程（4），我们可以得到：  
> $$q(\mathbf{x}_{t}|\mathbf{x}_{0})=\mathcal{N}(\mathbf{x}_{t};\sqrt{\bar{\alpha}_{t}}\mathbf{x}_{0},(1-\bar{\alpha}_{t})\mathbf{I})  $$
> 其中，α_t和̄α_t分别定义为：  
> α_t=1-β_t  
> ̄α_t =\prod_{t}^{s=1} α_s  
> 这个建模是为了确保正向过程和反向过程在β_t较小时具有相同的函数形式[53]。因此，我们可以在任意时间步骤t中以闭合形式对x_t进行采样。 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=KVTXC65K))

^KEYKVTXC65K

> <span class="highlight" style="background-color: #ffd400">Rao-Blackwellized fashion</span>  
> Rao-Blackwellization is a statistical technique that aims to improve the efficiency of an estimator by using conditional expectations. It is named after C. Radhakrishna Rao and David Blackwell, who initially developed and popularized the approach.  
> In the context of fashion, Rao-Blackwellization could refer to the application of this statistical technique to improve the accuracy of trend analysis, forecasting, or personalization within the fashion industry.  
> For example, in trend analysis, Rao-Blackwellization could be used to refine the prediction of future fashion trends by incorporating additional relevant variables or adjusting estimators based on conditional expectations. This would result in a more efficient and accurate forecast compared to traditional methods.  
> Similarly, in personalization, Rao-Blackwellization could help in providing more accurate fashion recommendations to individual customers. By utilizing conditional expectations, the system can make more informed predictions about a customer's preferences based on their previous behavior or the behavior of similar customers.  
> Overall, "Rao-Blackwellized fashion" refers to the application of this statistical technique to enhance the efficiency and accuracy of various fashion-related analyses and recommendations.  
> 🔤黑化时装🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=ZKS2LAWY))

^KEYZKS2LAWY

根据提供的上下文信息,我们可以推导出所给表达式的详细过程。首先,我们给出以下的均值方差的表示形式:

$$
\mu_\theta(x_t,t) = x_t - \sqrt{(1-\alpha_t)}\phi_\theta(x_t)$$

$$
\Sigma_\theta(x_t,t) = \beta_t\phi^2_\theta(x_t)$$

其中$\phi_\theta$代表一个可学习的非线性函数[2]。根据上一步骤的结果,我们可以写出条件概率分布:

$$
p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)) = \mathcal{N}(x_{t-1};x_t - \sqrt{(1-\alpha_t)}\phi_\theta(x_t),\beta_t\phi^2_\theta(x_t)) = p(x_{t-1}|x_t)$$

接下来,我们可以使用递归 Substitution 方法推导出 $q(x_t|x_0)$ 的表达式[5]。我们从 $q(x_1|x_0)$ 开始,将其表示为:

$$
q(x_1|x_0) = \int p(x_1,x_0)\mathrm{d}x_0 = \int p(x_1|x_0)p(x_0)\mathrm{d}x_0$$

根据上一步的条件概率分布的结果:

$$
p(x_1|x_0) = \mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0+\sqrt{\alpha_1}\xi_1,\beta_1\xi_1(x_0)) = \mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0,\beta_1 I)$$
其中$\xi_1$是在$\mathcal{N}(0,I)$上采样的噪声[3]。进一步推导,对于任意的$t>1$,我们有:

$$
q(x_t|x_0) = \int p(x_t,x_{t-1}\dots x_1,x_0)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1} = \int \prod^{t-1}_{i=1} p(x_i|x_{i+1})p(x_1)p(x_0)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$

根据之前的给定条件概率分布结果,我们可以得到:

$$
q(x_t|x_0) = \int \prod^{t-1}_{i=1} \mathcal{N}(x_i|x_{i+1},\beta_i I)\mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0,\beta_1 I)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$

使用 Gaussian 概率密度函数的性质,我们可以进一步进行计算化简:

$$
q(x_t|x_0) = \int \mathcal{N}(x_t|\sqrt{(1-\alpha_1)}x_0,\beta_i I)\prod^{t-2}_{i=1} \mathcal{N}(x_i|x_{i+1},\beta_i I)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$

继续简化上述表达式,我们可以得到所给的 $q(x_t|x_0)$ 的表达式:

$$
q(x_t|x_0) = \mathcal{N}(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I)$$

这就是所求的结果。请注意,上述计算过程中的符号含义

其中，递归替代方法（Recursive Substitution Method）是一种解决递归方程的方法。递归方程是一种定义一个数列或函数的方程，它包含了该数列或函数的前一项或前几项。递归替代方法通过反复使用递归方程来逐步计算出数列或函数的值。

递归替代方法的步骤如下：

1. 根据递归方程，确定初始条件（初始项）。
2. 利用递归方程，将前一项的值替代为后一项的表达式。
3. 重复步骤2，直到计算出所需的项。

递归替代方法常用于解决递归方程的数学问题，例如计算斐波那契数列、阶乘等。通过递归替代方法，可以逐步计算出数列或函数的各项的值，从而得到解决问题的结果。