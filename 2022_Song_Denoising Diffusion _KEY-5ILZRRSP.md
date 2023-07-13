# Denoising Diffusion Implicit Models
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|preprint|
> |标题|Denoising Diffusion Implicit Models|
> |短标题||
> |作者|[[Jiaming Song]]、 [[Chenlin Meng]]、 [[Stefano Ermon]]|
> |期刊名称||
> |DOI||
> |存档位置||
> |馆藏目录|arXiv.org|
> |索书号||
> |版权||
> |分类||
> |条目链接|[My Library](zotero://select/library/items/5ILZRRSP)|
> |PDF 附件|[Song et al. - 2022 - Denoising Diffusion Implicit Models.pdf](zotero://open-pdf/library/items/CHRBA486)|
> |关联文献||
> ^Metadata

> [!example]- <center>本文标签</center>
> 
> `$=dv.current().file.tags`

> [!quote]- <center>Abstract</center>
> 
> Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a Markovian diffusion process. We construct a class of non-Markovian diffusion processes that lead to the same training objective, but whose reverse process can be much faster to sample from. We empirically demonstrate that DDIMs can produce high quality samples $10 \times$ to $50 \times$ faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, and can perform semantically meaningful image interpolation directly in the latent space.

> [!tldr]- <center>隐藏信息</center>
> 
> itemType:: preprint
> title:: Denoising Diffusion Implicit Models
> shortTitle:: 
> creators:: [[Jiaming Song]]、 [[Chenlin Meng]]、 [[Stefano Ermon]]
> publicationTitle:: 
> journalAbbreviation:: 
> volume:: 
> issue:: 
> pages:: 
> language:: 
> DOI:: 
> ISSN:: 
> url:: [http://arxiv.org/abs/2010.02502](http://arxiv.org/abs/2010.02502)
> archive:: 
> archiveLocation:: 
> libraryCatalog:: arXiv.org
> callNumber:: 
> rights:: 
> extra:: 132 citations (Semantic Scholar/arXiv) [2022-06-21] arXiv：2010.02502 [cs]; https：//web.archive.org/web/20220621150925/https：//arxiv.org/abs/2010.02502
> collection:: 
> tags:: #reading #Computer_Science_-_Computer_Vision_and_Pattern_Recognition #Computer_Science_-_Machine_Learning
> related:: 
> itemLink:: [My Library](zotero://select/library/items/5ILZRRSP)
> pdfLink:: [Song et al. - 2022 - Denoising Diffusion Implicit Models.pdf](zotero://open-pdf/library/items/CHRBA486)
> qnkey:: 2022_Song_Denoising Diffusion _KEY-5ILZRRSP
> date:: 2022-06-09
> dateY:: 2022
> dateAdded:: 2022-06-20
> dateModified:: 2023-07-07
> 
> abstract:: Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a Markovian diffusion process. We construct a class of non-Markovian diffusion processes that lead to the same training objective, but whose reverse process can be much faster to sample from. We empirically demonstrate that DDIMs can produce high quality samples $10 \times$ to $50 \times$ faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, and can perform semantically meaningful image interpolation directly in the latent space.


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
> ⏰ importDate:: 2023-07-07

%--------------ω--------------%

## 📝 注释笔记 CHRBA486

> <span style="font-size: 15px;color: gray">📍 2022-Song-Denoising Diffusion Implicit Models</span>

^KEYrefTitle

> <span class="highlight" style="background-color: #ffd400">Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps in order to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a particular Markovian diffusion process. We generalize DDPMs via a class of non-Markovian diffusion processes that lead to the same training objective. These non-Markovian processes can correspond to generative processes that are deterministic, giving rise to implicit models that produce high quality samples much faster. We empirically demonstrate that DDIMs can produce high quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, perform semantically meaningful image interpolation directly in the latent space, and reconstruct observations with very low error.</span>  
> 🔤去噪扩散概率模型(DDPMs)取得了高质量图像生成没有对抗的训练,但他们需要模拟一个马尔可夫链对许多步骤,以产生一个样本。加速抽样,我们现在去噪扩散隐式模型(DDIMs),更有效的迭代隐含概率模型与DDPMs一样的训练过程。DDPMs,生成过程的定义是反向的马尔可夫链的扩散过程。我们通过一类non-Markovian概括DDPMs扩散过程,导致同样的训练目标。这些non-Markovian过程可以对应于确定的生成过程,引起隐式模型,生产高质量的样品快得多。我们经验证明DDIMs可以产生高质量的样品快10×50×所DDPMs相比,允许我们权衡计算样本质量,直接执行语义上有意义的图像插值的潜在空间,和重构观测误差很低。🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=QSPCMC9A))

^KEYQSPCMC9A

> <span class="highlight" style="background-color: #ffd400">Recent works on iterative generative models</span>  
> 🔤近期作品在迭代生成模型🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=4824L42L))

^KEY4824L42L

> <span class="highlight" style="background-color: #ffd400">such as denoising diffusion probabilistic models</span>  
> 🔤如去噪扩散概率模型🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=5P365IAT))

^KEY5P365IAT

> <span class="highlight" style="background-color: #ffd400">have demonstrated the ability to produce samples comparable to that of GANs, without having to perform adversarial training.</span>  
> 🔤已经证明能够生产样品与甘斯,无需进行对抗训练。🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=ZL2MX7I4))

^KEYZL2MX7I4

> <span class="highlight" style="background-color: #ffd400">To achieve this, many denoising autoencoding models are trained to denoise samples corrupted by various levels of Gaussian noise. Samples are then produced by a Markov chain which, starting from white noise, progressively denoises it into an image.</span>  
> 🔤为了实现这一目标，许多去噪自动编码模型经过训练，可以对被不同级别的高斯噪声破坏的样本进行去噪。然后，马尔可夫链生成样本，该链从白噪声开始，逐渐将其去噪为图像。🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=RFSVQUUL))

^KEYRFSVQUUL

> <span class="highlight" style="background-color: #ffd400">A critical drawback of these models is that they require many iterations to produce a high quality sample. For DDPMs, this is because that the generative process (from noise to data) approximates the reverse of the forward diffusion process (from data to noise), which could have thousands of steps; iterating over all the steps is required to produce a single sample, which is much slower compared to GANs, which only needs one pass through a network.</span>  
> 🔤这些模型的一个关键缺点是它们需要多次迭代才能产生高质量的样本。对于 DDPM，这是因为生成过程（从噪声到数据）近似于前向扩散过程（从数据到噪声）的逆过程，后者可能有数千个步骤；生成单个样本需要迭代所有步骤，这比只需要通过网络一次的 GAN 慢得多。🔤 ([p1](zotero://open-pdf/library/items/CHRBA486?page=1&annotation=CU6LAMJE))

^KEYCU6LAMJE

> <span class="highlight" style="background-color: #ffd400">his can massively increase sample efficiency only at a minor cost in sample quality.</span>  
> 🔤只需要以很小的样品质量成本为代价，就能大幅提高样品效率。🔤 ([p2](zotero://open-pdf/library/items/CHRBA486?page=2&annotation=TCATK9DG))

^KEYTCATK9DG

