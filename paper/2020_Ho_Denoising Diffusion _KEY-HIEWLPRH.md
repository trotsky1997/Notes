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
> dateModified:: 2023-07-16
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

> <span class="highlight" style="background-color: #aaaaaa">q(xt|xt−1) := N (xt; √1 − βtxt−1, βtI)</span>  
> 🔤q(xt|xt−1) := N (xt; √1 − βtxt−1, βtI)🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=PRBM9838))

^KEYPRBM9838

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

> <span class="note" style="background-color: #ffd400">note</span>  
> 根据提供的上下文信息,我们可以推导出所给表达式的详细过程。首先,我们给出以下的均值方差的表示形式:  
> $$  
> \mu_\theta(x_t,t) = x_t - \sqrt{(1-\alpha_t)}\phi_\theta(x_t)$$  
> $$  
> \Sigma_\theta(x_t,t) = \beta_t\phi^2_\theta(x_t)$$  
> 其中$\phi_\theta$代表一个可学习的非线性函数[2]。根据上一步骤的结果,我们可以写出条件概率分布:  
> $$  
> p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)) = \mathcal{N}(x_{t-1};x_t - \sqrt{(1-\alpha_t)}\phi_\theta(x_t),\beta_t\phi^2_\theta(x_t)) = p(x_{t-1}|x_t)$$  
> 接下来,我们可以使用递归 Substitution 方法推导出 $q(x_t|x_0)$ 的表达式[5]。我们从 $q(x_1|x_0)$ 开始,将其表示为:  
> $$  
> q(x_1|x_0) = \int p(x_1,x_0)\mathrm{d}x_0 = \int p(x_1|x_0)p(x_0)\mathrm{d}x_0$$  
> 根据上一步的条件概率分布的结果:  
> $$  
> p(x_1|x_0) = \mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0+\sqrt{\alpha_1}\xi_1,\beta_1\xi_1(x_0)) = \mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0,\beta_1 I)$$  
> 其中$\xi_1$是在$\mathcal{N}(0,I)$上采样的噪声[3]。进一步推导,对于任意的$t>1$,我们有:  
> $$  
> q(x_t|x_0) = \int p(x_t,x_{t-1}\dots x_1,x_0)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1} = \int \prod^{t-1}_{i=1} p(x_i|x_{i+1})p(x_1)p(x_0)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$  
> 根据之前的给定条件概率分布结果,我们可以得到:  
> $$  
> q(x_t|x_0) = \int \prod^{t-1}_{i=1} \mathcal{N}(x_i|x_{i+1},\beta_i I)\mathcal{N}(x_1;\sqrt{(1-\alpha_1)}x_0,\beta_1 I)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$  
> 使用 Gaussian 概率密度函数的性质,我们可以进一步进行计算化简:  
> $$  
> q(x_t|x_0) = \int \mathcal{N}(x_t|\sqrt{(1-\alpha_1)}x_0,\beta_i I)\prod^{t-2}_{i=1} \mathcal{N}(x_i|x_{i+1},\beta_i I)\mathrm{d}x_1\mathrm{d}x_2\dots\mathrm{d}x_{t-1}$$  
> 继续简化上述表达式,我们可以得到所给的 $q(x_t|x_0)$ 的表达式:  
> $$  
> q(x_t|x_0) = \mathcal{N}(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I)$$  
> 这就是所求的结果。请注意,上述计算过程中的符号含义  
> 其中，递归替代方法（Recursive Substitution Method）是一种解决递归方程的方法。递归方程是一种定义一个数列或函数的方程，它包含了该数列或函数的前一项或前几项。递归替代方法通过反复使用递归方程来逐步计算出数列或函数的值。  
> 递归替代方法的步骤如下：  
> 1. 根据递归方程，确定初始条件（初始项）。  
> 2. 利用递归方程，将前一项的值替代为后一项的表达式。  
> 3. 重复步骤2，直到计算出所需的项。  
> 递归替代方法常用于解决递归方程的数学问题，例如计算斐波那契数列、阶乘等。通过递归替代方法，可以逐步计算出数列或函数的各项的值，从而得到解决问题的结果。 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=35AZAYI2))

^KEY35AZAYI2

> <span class="highlight" style="background-color: #ffd400">q(xt|x0) = N (xt; √ ̄ αtx0, (1 − ̄ αt)I)</span>  
> 这一步是通过对于正向过程进行条件概率的建模得出的。根据上下文信息中的方程（4），我们可以得到：  
> q(\mathbf{x}_{t}|\mathbf{x}_{0})=\mathcal{N}(\mathbf{x}_{t};\sqrt{\bar{\alpha}_{t}}\mathbf{x}_{0},(1-\bar{\alpha}_{t})\mathbf{I})  
> 其中，α_t和̄α_t分别定义为：  
> α_t=1-β_t  
> ̄α_t =\prod_{t}^{s=1} α_s  
> 这个建模是为了确保正向过程和反向过程在β_t较小时具有相同的函数形式[53]。因此，我们可以在任意时间步骤t中以闭合形式对x_t进行采样。  
> 🔤🔤 ([p2](zotero://open-pdf/library/items/RZEREA2F?page=2&annotation=KVTXC65K))

^KEYKVTXC65K

> <span class="highlight" style="background-color: #ffd400">Rao-Blackwellized fashion</span>  
> Rao-Blackwellization is a statistical technique that aims to improve the efficiency of an estimator by using conditional expectations. It is named after C. Radhakrishna Rao and David Blackwell, who initially developed and popularized the approach.  
> In the context of fashion, Rao-Blackwellization could refer to the application of this statistical technique to improve the accuracy of trend analysis, forecasting, or personalization within the fashion industry.  
> For example, in trend analysis, Rao-Blackwellization could be used to refine the prediction of future fashion trends by incorporating additional relevant variables or adjusting estimators based on conditional expectations. This would result in a more efficient and accurate forecast compared to traditional methods.  
> Similarly, in personalization, Rao-Blackwellization could help in providing more accurate fashion recommendations to individual customers. By utilizing conditional expectations, the system can make more informed predictions about a customer's preferences based on their previous behavior or the behavior of similar customers.  
> Overall, "Rao-Blackwellized fashion" refers to the application of this statistical technique to enhance the efficiency and accuracy of various fashion-related analyses and recommendations.  
> 🔤黑化时装🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=ZKS2LAWY))

^KEYZKS2LAWY

> <span class="highlight" style="background-color: #ffd400">denoising score matching</span>  
> 🔤去噪分数匹配🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=SIWXBLA8))

^KEYSIWXBLA8

> <span class="highlight" style="background-color: #ff6666">Reverse process and L1:T −1</span>  
> 在3.2节中，作者讨论了逆过程和L1:T −1的问题。逆过程是从高噪声图像逐渐还原为清晰图像的过程。L1:T −1是在训练过程中对逆过程中的一系列损失函数进行加权和处理。  
> 首先，作者提出了一种简化的目标函数（式14），将损失在时间步骤t较小的部分进行降权处理。这样做的目的是使网络能够更好地处理更困难的去噪任务，而不是过于依赖于去噪轻微噪声的能力。通过降低对小t值的损失函数的权重，网络可以更好地学习处理更大t值的去噪任务，从而提高样本质量。  
> 其次，作者还研究了逆过程的参数化问题。具体地，作者使用了一些参数来表示逆过程的方差和均值。作者提到，他们尝试了不同的参数化方法，并与其他方法进行了比较。结果显示，作者提出的参数化方法在训练过程中表现出良好的性能，并且在样本质量方面比其他方法更好。特别是，作者提到他们的参数化方法在使用简化目标函数进行训练时表现得更好。  
> 综上所述，在3.2节中，作者介绍了逆过程和L1:T −1的概念，并通过一系列实验结果证明了其在改善样本质量方面的有效性。这些研究结果为网络的逆过程和损失权重提供了有益的见解。  
> 🔤🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=T946KEZS))

^KEYT946KEZS

> <span class="highlight" style="background-color: #ff6666">These are the two extreme choices corresponding to upper and lower bounds on reverse process entropy for data with coordinatewise unit variance [53].</span>  
> 🔤这是与坐标单位方差数据的逆向过程熵的上限和下限相对应的两个极端选择[53]。🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=Z6BGA56J))

^KEYZ6BGA56J

> <span class="highlight" style="background-color: #ff6666">Second</span>  
> 为了表示均值$\boldsymbol{\mu}_\theta(\mathbf{x}_t,t)$，我们提出了一个特定的参数化方法，其受到了$L_{\boldsymbol{t}}$的分析的启发。对于$\text{ı }p_{\theta}(\mathbf{x}_{t-1}|\mathbf{x}_{t})=\mathcal{N}(\mathbf{x}_{t-1};\boldsymbol{\mu}_{\theta}(\mathbf{x}_{t},t),\sigma_{t}^{2}\mathbf{I})$，我们可以写成(8)，其中$\text{C}$是一个与$t$无关的常数。因此，我们可以看出，pp的最简单的参数化方法是预测$\tilde{\mu}_{t}$，即前向过程的后验均值。然而，我们可以通过将方程(4)重新参数化为$x_t = \sqrt{\alpha_t}\mathbf{x}_0 + \sqrt{1-\alpha_t}\epsilon$，其中$\epsilon \sim \mathcal{N}(\mathbf{0},\mathbf{I})$，并应用前向过程的后验公式(9)，进一步展开方程(8):  
> \[ L_{t-1}-C=\mathbb{E}_{\mathbf{x}_0,\boldsymbol{\epsilon}}\left[\frac1{2\sigma_t^2}\left\|\tilde{\boldsymbol{\mu}}_t\left(\mathbf{x}_t(\mathbf{x}_0,\boldsymbol{\epsilon}),\frac1{\sqrt{\bar{\alpha}_t}}(\mathbf{x}_t(\mathbf{x}_0,\boldsymbol{\epsilon})-\sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon})\right)-\boldsymbol{\mu}_\theta(\mathbf{x}_t(\mathbf{x}_0,\boldsymbol{\epsilon}),t)\right\|^2\right] \quad (9) \]  
> \[ =\mathbb{E}_{\mathbf{x}_0,\boldsymbol{\epsilon}}\left[\frac{1}{2\sigma_t^2}\left\|\frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t(\mathbf{x}_0,\boldsymbol{\epsilon})-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\boldsymbol{\epsilon}\right)-\boldsymbol{\mu}_\theta(\mathbf{x}_t(\mathbf{x}_0,\boldsymbol{\epsilon}),t)\right\|^2\right] \quad (10)\]  
> 根据实验结果 [5]，我们发现，当使用真实的变分界限而不是未加权的均方误差进行训练时，预测$\tilde{\mu}$的基准选项效果良好。我们还发现，相对于固定的方差，学习反向过程的方差（通过将参数化的对角线$\Sigma_{\theta}(\mathbf{x}_t)$纳入变分界限中）会导致训练不稳定和样本质量较差。而我们提出的预测$\epsilon$的方法，当使用我们简化的目标进行训练时，与预测$\tilde{\mu}$的方法表现相当，但在使用简化的目标进行训练时表现更好。  
> 🔤adv. 其次；第二（的）；（重要性、规模、质量等）居第二位的；另外的； n. 瞬间；片刻；秒（时间单位）；秒（角度单位）； v. 附议；临时调派； adj. 别的；次(的)；副(的)；从属的； 网络释义： 第二的；第二次；秒钟🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=VY7CN2AY))

^KEYVY7CN2AY

> <span class="highlight" style="background-color: #5fb236">(8) 这一步是由两个闭式解的差值求解出来的</span>  
> 根据提供的上下文信息，我们来解释一下L_{t-1}=\mathbb{E}_q\bigg[\frac{1}{2\sigma_t^2}\|\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t,\mathbf{x}_0)-\boldsymbol{\mu}_\theta(\mathbf{x}_t,t)\|^2\bigg]+C这一步的推导过程。  
> 首先，我们回顾一下上下文提到的一些关键信息。在公式（3）中，我们有L_{t-1}=\mathbb{E}_q\bigg[\|\mathbf{x}_{t-1}-\boldsymbol{\mu}_{\theta}(\mathbf{x}_t,t)\|^2\bigg]，表示在给定前一个时间步t-1的条件下，通过概率分布q生成的样本与使用反向过程通过解码器得到的样本之间的误差。  
> 在简化的目标函数公式（14）中，我们丢弃了公式（12）中的权重，从而得到了一个加重的变分边界。这个简化的目标函数会降低相对较小的t值对应的损失项的权重。因为这些损失项是用非常少的噪声来训练网络去去噪，所以将它们的权重降低，可以使网络更加关注在更困难的去噪任务上。实验结果表明，这种重新加权可以提高样本质量。  
> 接下来，我们看一下公式（4）：q(\mathbf{x}_t | \mathbf{x}_0) = N(\mathbf{x}_t; \sqrt{\bar{\alpha}_t}\mathbf{x}_0, (1-\bar{\alpha}_t)I)，表示在任意时间步t处，我们可以闭式地从概率分布q中采样。  
> 综上所述，结合公式（3）和（4），我们可以得到公式（8）的推导过程：  
> 首先，我们根据公式（4）的结论得到q(\mathbf{x}_t | \mathbf{x}_0) = N(\mathbf{x}_t; \sqrt{\bar{\alpha}_t}\mathbf{x}_0, (1-\bar{\alpha}_t)I)。  
> 接着，我们计算\|\mathbf{x}_t - \boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)\|^2，这表示样本\mathbf{x}_t与使用反向过程通过解码器得到的样本\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)之间的欧式距离的平方。  
> 然后将\sqrt{\bar{\alpha}_t}作为比例因子，对样本\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)进行缩放。  
> 然后，我们将缩放后的样本\frac{\sqrt{1-\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)与样本\mathbf{x}_0相减，得到\frac{\sqrt{1-\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)-\mathbf{x}_0。  
> 为了计算期望值，我们将其平方，得到\left(\frac{\sqrt{1-\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)-\mathbf{x}_0\right)^2。  
> 最后，我们乘以系数\frac{1}{2\sigma_t^2}，得到\frac{1}{2\sigma_t^2}\left(\frac{\sqrt{1-\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)-\mathbf{x}_0\right)^2。  
> 因此，我们得到L_{t-1}=\mathbb{E}_q\bigg[\frac{1}{2\sigma_t^2}\left(\frac{\sqrt{1-\bar{\alpha}_t}}{\sqrt{\bar{\alpha}_t}}\boldsymbol{\mu}_{\theta}(\mathbf{x}_t, t)-\mathbf{x}_0\right)^2\bigg]。  
> 🔤🔤 ([p3](zotero://open-pdf/library/items/RZEREA2F?page=3&annotation=TE9A2PRQ))

^KEYTE9A2PRQ

> <span class="highlight" style="background-color: #ff6666">To summarize, we can train the reverse process mean function approximator μθ to predict ̃ μt, or by modifying its parameterization, we can train it to predict .</span>  
> 🔤总而言之，我们可以训练逆向过程均值函数逼近器 μθ 来预测 ̃ μt，或者通过修改其参数化，我们可以训练它来预测 。🔤 ([p4](zotero://open-pdf/library/items/RZEREA2F?page=4&annotation=7A2M92UG))

^KEY7A2M92UG

> <span class="highlight" style="background-color: #5fb236">Related Work</span>  
> 传统的难点是在训练过程中如何有效地学习到一个概率分布模型，以使得生成的样本与真实数据分布尽可能接近。而扩散模型（diffusion model）通过将噪声逐渐添加到数据中，从噪声数据中逆向恢复得到原始数据的过程，简化了训练过程。在这种情况下，预测噪声（即高斯噪声）变得更容易进行优化。  
> 具体来说，扩散模型采用了一个参数化的马尔可夫链，在变分推断的指导下进行训练，使得最终得到的样本在有限时间内逼近真实数据。这个马尔可夫链的转移通过学习一个逆向的扩散过程来实现，这个扩散过程逐渐向数据中添加噪声，与采样过程的方向相反。当扩散过程由一小部分高斯噪声组成时，采样链的转移也可以设置为条件高斯分布，从而简化了神经网络的参数化过程。  
> 与其他基于概率似然的模型相比，扩散模型的定义和训练过程都非常直观和高效。但据我们所知，迄今为止没有证明扩散模型能够生成高质量的样本。然而，我们的研究表明，扩散模型实际上是能够生成高质量样本的，有时甚至比其他类型的生成模型的效果更好。  
> 此外，我们还发现扩散模型的一个特定参数化揭示了它与多个噪声水平下的去噪分数匹配（denoising score matching）以及退火兰德金动力学（annealed Langevin dynamics）之间的等价性。我们的最佳样本质量结果是使用这种参数化得到的。所以我们认为这种等价性是我们的主要贡献之一。  
> 需要注意的是，尽管扩散模型的样本质量很高，但与其他基于似然的模型相比，我们的模型的对数似然性能并不具备竞争力。我们发现，我们模型的绝大部分无损编码长度都用于描述人眼几乎察觉不到的图像细节。我们还使用了无损压缩的方法对这种现象进行了更精细的分析，并发现扩散模型的采样过程类似于具有远远超越传统自回归模型的位序编码的渐进解码过程。  
> 综上所述，通过预测高斯噪声而不是数据本身的优化目标，扩散模型在训练过程中能够更容易地实现高质量样本的生成。同时，扩散模型的简单参数化使得其在定义和训练过程中都非常有效。  
> 🔤🔤 ([p8](zotero://open-pdf/library/items/RZEREA2F?page=8&annotation=VVKHS2X2))

^KEYVVKHS2X2

