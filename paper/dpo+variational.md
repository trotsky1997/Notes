我们尝试从${y_l,y_w,x}$的三元组中去掉$y_w$的依赖，

$$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x,y_w,y_l) \sim D} \left[ \log \sigma\left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]

$$

定义距离$\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}$,$p^*(y_1 \succ y_2 | x) = \sigma (d)$

$d = \beta \log \frac{\pi_\theta(y_w|x)\pi_{ref}(y_l|x)}{\pi_\theta(y_l|x)\pi_{ref}(y_w|x)}$

 $\min \mathcal{L}_{DPO}(\pi_\theta; \pi_{ref})$ 等价于 $\max \mathbb{E}_{(x,y_w,y_l) \sim D}[d]$。



审视此式,先处理$\pi_\theta(y_l|y_w,x)$，我们已知

 $\min \mathcal{L}_{DPO}(\pi_\theta; \pi_{ref})$ 等价于 $\max \mathbb{E}_{(x,y_w,y_l) \sim D}[\pi_\theta(y_l|y_w,x)\pi_{ref}(y_l|y_w,x) \pi_\theta(y_l|x)\pi_{ref}(y_l|x)\}]$。

令$Q(y_l)$ 作为 $\pi_\theta(y_l|y_w,x)$的近似，即$\pi_\theta(y_l)$的后验近似，令$Q_{ref}(y_l)$ 作为$\pi_{ref}(y_l|y_w,x)$的后验近似，

$$

\begin{aligned}



-\log\pi_\theta(y_l|y_w,x)

&= - \log \frac{\pi_\theta(y_w,y_l,x)}{\mathbb{E}_q[\frac{\pi_\theta(y_w,y_l,x)}{Q(y_l)}]} \\

& \geq -\log\pi_\theta(y_w,y_l,x) +ELBO(q)\\

& = -\log\pi_\theta(y_w,y_l,x) + \mathbb{E}_q[\log\pi_\theta(y_w,y_l,x) - \log{Q(y_l)}] \\

&= -log{\pi_\theta(y_w,y_l,x)} + \mathbb{E}_q[\log{\pi_\theta(y_w|y_l,x)}] - KL[Q(y_l)||\pi_\theta(y_l)] \\

& = -\log{\pi_\theta(y_l,x)} - KL[Q(y_l)||\pi_\theta(y_l)] \\

\end{aligned}$$

同样处理$\pi_{ref}(y_l|y_w,x)$，可得

$$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) \geq -\mathbb{E}_{(x,y_w,y_l) \sim D} [\log \sigma \{-2\log{\pi_\theta(y_l,x)} - KL[Q(y_l)||\pi_\theta(y_l)]-2\log{\pi_{ref}(y_l,x)} - KL[Q_{ref}(y_l)||\pi_{ref}(y_l)] \}]$$

指出这个推导过程的错误之处