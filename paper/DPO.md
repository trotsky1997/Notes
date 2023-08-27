# DPO

- **任务**：本文研究了三个开放式文本生成任务，分别是情感调节、摘要和对话。对于所有的任务，算法都需要从一个包含人类偏好的数据集中学习一个策略，即给定一个前缀x，生成一个符合人类偏好的后缀y。
    
- **评估**：本文使用两种不同的方法来评估算法的性能。一种是在受控的情感调节任务中，使用真实的奖励函数（一个情感分类器）来计算每个算法在奖励和KL散度方面的表现。另一种是在摘要和对话任务中，使用GPT-4作为人类评价的代理，计算每个算法与基准策略之间的胜率。本文还通过人类评价来验证GPT-4判断的可靠性。
    
- **方法**：除了DPO算法之外，本文还评估了一些现有的方法，包括零样本或二样本提示、有监督微调、Unlikelihood、PPO以及基于学习奖励函数返回最佳样本的方法。所有的方法都使用相同或相似的预训练语言模型作为基础。
    ## RLHF
我们回顾了Ziegler等人在后续工作中采用的RLHF管道 [35, l 23]。它通常由3个阶段组成:
1)有监督的微调(SFT);2)偏好采样和奖励学习; SFT阶段:RLHF通常从一个通用的预训练语言模型开始，该模型在高质量数据集上对感兴趣的下游任务(如对话、指令遵循、摘要等)进行监督学习(最大似然)进行微调，以获得一个模型$\pi^{\mathrm{SFT}}$ 奖励建模阶段:在第二阶段，用提示提示SFT模型生成部分答案$(y_{1},y_{2})\sim\pi^{\mathrm{SFT}}(y|x)$.。然后将这些呈现给人类标记者，他们表示对一个答案的偏好，表示为$y_{w}\succ y_{l}$ a，其中$\boldsymbol{y}_{\boldsymbol{w}}$和gi分别表示(y1,9/2)中首选和不首选的完成。假设偏好是由一些我们无法访问的潜在奖励模型$r^{*}(y,x),$生成的。有许多方法用于对偏好进行建模，Bradley-Terry (BT)[5]模型是一种流行的选择(尽管更通用的Plackett-Luce排名模型也与框架兼容，如果我们可以获得多个排名答案)。BT模型规定人类的偏好分布$p^{*}$可以写成: $$ p^*(y_1\succ y_2\mid x)=\frac{\exp\left(r^*(x,y_1)\right)}{\exp\left(r^*(x,y_1)\right)+\exp\left(r^*(x,y_2)\right)}. $$ 假设我们从一个偏好函数分布$p^{*}$中采样出静态比较数据集三元组 $\mathcal{D}=\left\{x^{(i)},y_w^{(i)},y_l^{(i)}\right\}_{i=1}^N$，我们就可以将奖励模型参数化$r_{\phi}(x,y)$并通过最大似然估计参数。假设问题为二分类问题，我们得到负对数似然损失: $$ \mathcal{L}_R(r_\phi,\mathcal{D})=-\mathbb{E}_{(x,y_w,y_l)\sim\mathcal{D}}\left[\operatorname{log}\sigma(r_\phi(x,y_w)-r_\phi(x,y_l))\right] $$ (2) 其中$\color{red}{\sigma}$为logistic函数。在LMs的背景下，网络$r_{\phi}(x,y)$通常由SFT模型$\pi^{\mathrm{SFT}}(y\mid x)$初始化，并在最终的transformer层之上添加了一个线性层，该层为奖励值产生单个标量预测。为了确保具有较低方差的奖励函数，前作常惩罚奖励，对所有$x$，$\mathbb{E}_{x,y\sim\mathcal{D}}\left[r_\phi(x,y)\right]=0.$。强化学习微调阶段:在强化学习阶段，我们使用学习到的奖励函数为语言模型提供反馈。特别地，我们表述了以下优化问题 
$$ \max_{\pi_{\theta}}\mathbb{E}_{x\sim\mathcal{D},y\sim\pi_{\theta}(y|x)}\big[r_{\phi}(x,y)\big]-\beta\mathbb{D}_{\mathbf{KL}}\big[\pi_{\theta}(y\mid x)\:||\:\pi_{\mathbf{ref}}(y\mid x)\big] $$
其中$\text{β}$是一个参数，控制与基本参考策略$\pi_{\mathrm{ref}},$的偏差，即初始SFT模型$\pi^{\mathrm{SFT}}$。在实践中是由$\pi^{\mathrm{SFT}}$提出的语言模型策略$\pi_{\theta}$。添加的约束是重要的，因为它防止模型偏离奖励模型准确的分布太远，以及保持生成多样性和防止模式崩溃到单一的高奖励答案。由于语言生成的离散性质，该目标是不可微的，通常用强化学习进行优化。构建奖励函数的标准实践是 $r(x,y)=r_{\phi}(x,y)-\beta(\log\pi_{\theta}(y\mid x)-\log\pi_{\mathrm{ref}}(y\mid x))$，并使用PPO算法最大化。
  

DPO算法的推导过程

  

1. 从与现有方法相同的RL目标出发，即在KL散度约束下最大化奖励。
    

$$

\max_{\pi_\theta} \mathbb{E}_{x \sim D, y \sim \pi_\theta(y|x)} r_\phi(x, y) - \beta D_{KL}(\pi_\theta(y|x) || \pi_{ref}(y|x))

$$

2. 推导出最优解的形式，并用策略、参考策略和未知的配分函数来重新表示奖励函数。
    

$$

\pi_r(y|x) = \frac{1}{Z(x)} \pi_{ref}(y|x) \exp \left( \frac{1}{\beta} r(x, y) \right)

$$
$$Z(x)=\sum_{y}\pi_{\mathrm{ref}}(y\mid x)\exp\left(\frac{1}{\beta}r(x,y)\right)$$

$$

r(x, y) = \beta \log \frac{\pi_r(y|x)}{\pi_{ref}(y|x)} + \beta \log Z(x)

$$

3. 将这种重新表示应用于真实的奖励函数$r^*$和最优策略$\pi^*$后，发现配分函数会抵消，从而可以用最优策略和参考策略来表示人类偏好概率。
   $$ r^*(x,y)=\beta\log\frac{\pi^*(y|x)}{\pi_{\mathrm{ref}}(y|x)}+\beta\log Z(x)$$
$$p^*(y_1\succ y_2|x)=\frac{\exp\left(r^*(x,y_1)\right)}{\exp\left(r^*(x,y_1)\right)+\exp\left(r^*(x,y_2)\right)}$$

$$
p^*(y_1\succ y_2|x)=\frac{\exp\left(\beta\log\frac{\pi^*(y_1|x)}{\pi_{\mathrm{erf}}(y_1|x)}+\beta\log Z(x)\right)}{\exp\left(\beta\log\frac{\pi^*(y_1|x)}{\pi_{\mathrm{erf}}(y_1|x)}+\beta\log Z(x)\right)+\exp\left(\beta\log\frac{\pi^*(y_2|x)}{\pi_{\mathrm{erf}}(y_2|x)}+\beta\log Z(x)\right)}
$$
$$p^*(y_1 \succ y_2 | x) = \frac{1}{1 + \exp \left( \beta \log \frac{\pi^*(y_2|x)}{\pi_{ref}(y_2|x)} - \beta \log \frac{\pi^*(y_1|x)}{\pi_{ref}(y_1|x)}\right)}

$$

4. 因此，可以用一个最大似然目标来优化一个参数化的策略。
    

$$

\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x,y_w,y_l) \sim D} \left[ \log \sigma\left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]

$$
这个优化目标对应的是一个损失函数，即$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref})$。它是通过计算样本的负对数似然来衡量模型的性能。其中，$\pi_\theta(y_w|x)$和$\pi_\theta(y_l|x)$分别表示在给定输入$x$的条件下，模型$\pi_\theta$生成的答案$y_w$和$y_l$的概率。$\pi_{ref}(y_w|x)$和$\pi_{ref}(y_l|x)$分别表示给定输入$x$的条件下，参考策略$\pi_{ref}$生成的答案$y_w$和$y_l$的概率。

优化目标$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref})$的含义是，通过最小化样本的负对数似然来使得模型的生成答案更接近人类偏好的答案。其中，$\beta$是一个超参数，用于控制偏差与参考策略之间的权衡。使用负对数似然作为损失函数的目的是使得模型在生成答案时更接近参考策略，并且能够学习到如何根据人类偏好进行生成。
```
        metrics = {}

        (
            policy_chosen_logps,
            policy_rejected_logps,
            policy_chosen_logits,
            policy_rejected_logits,
        ) = self.concatenated_forward(model, batch)
        with torch.no_grad():
            (
                reference_chosen_logps,
                reference_rejected_logps,
                _,
                _,
            ) = self.concatenated_forward(self.ref_model, batch)

        losses, chosen_rewards, rejected_rewards = self.dpo_loss(
            policy_chosen_logps,
            policy_rejected_logps,
            reference_chosen_logps,
            reference_rejected_logps,
        )
```

```
        all_logps = self._get_batch_logps(
            all_logits,
            concatenated_batch["concatenated_labels"],
            average_log_prob=False,
        )
		chosen_logps = all_logps[: batch["chosen_input_ids"].shape[0]]
        rejected_logps = all_logps[batch["chosen_input_ids"].shape[0] :]

        chosen_logits = all_logits[: batch["chosen_input_ids"].shape[0]]
        rejected_logits = all_logits[batch["chosen_input_ids"].shape[0] :]
```

```
    def _get_batch_logps(
        self,
        logits: torch.FloatTensor,
        labels: torch.LongTensor,
        average_log_prob: bool = False,
    ) -> torch.FloatTensor:
        """Compute the log probabilities of the given labels under the given logits.

        Args:
            logits: Logits of the model (unnormalized). Shape: (batch_size, sequence_length, vocab_size)
            labels: Labels for which to compute the log probabilities. Label tokens with a value of label_pad_token_id are ignored. Shape: (batch_size, sequence_length)
            average_log_prob: If True, return the average log probability per (non-masked) token. Otherwise, return the sum of the log probabilities of the (non-masked) tokens.

        Returns:
            A tensor of shape (batch_size,) containing the average/sum log probabilities of the given labels under the given logits.
        """
        if logits.shape[:-1] != labels.shape:
            raise ValueError("Logits (batch and sequence length dim) and labels must have the same shape.")

        labels = labels[:, 1:].clone()
        logits = logits[:, :-1, :]
        loss_mask = labels != self.label_pad_token_id

        # dummy token; we'll ignore the losses on these tokens later
        labels[labels == self.label_pad_token_id] = 0

        per_token_logps = torch.gather(logits.log_softmax(-1), dim=2, index=labels.unsqueeze(2)).squeeze(2)

        if average_log_prob:
            return (per_token_logps * loss_mask).sum(-1) / loss_mask.sum(-1)
        else:
            return (per_token_logps * loss_mask).sum(-1)
```

比如生成结果是”吃“，吃的index 是135 ,对应输出头向量是\[batch,length,..y..\]，135 = argmax{y},$\pi\{...吃...|Prompt\} = log\_softmax(logit[135])$

迈向自评估
假设我们有两个策略网络，分别代表输出头和自评估头，