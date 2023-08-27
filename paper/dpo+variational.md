$$

\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x,y_w,y_l) \sim D} \left[ \log \sigma\left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]

$$
定义距离$d = \beta \log \frac{\pi^*(y_2|x)}{\pi_{ref}(y_2|x)} - \beta \log \frac{\pi^*(y_1|x)}{\pi_{ref}(y_1|x)}$,$p^*(y_1 \succ y_2 | x) = \sigma (d)$
$d = \beta \log\{\pi_\theta(y_w|y_l,x) \cdot \pi_{ref}(y_w|y_l,x)\}$
$\max \mathcal{L}_{DPO}(\pi_\theta; \pi_{ref})$  等价于 $\min d$
$$ \mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x,y_w,y_l) \sim D} [\log \sigma \{  \beta \log\{\pi_\theta(y_w|y_l,x) \cdot \pi_{ref}(y_w|y_l,x)\} \}]$$
审视$d$,当$\pi_{ref}$不可优化时,我们仅优化$\pi_\theta(y_w|y_l,x)$
$\mathcal{L}$ 可等价于  $\max -\log\pi_\theta(y_w|y_l,x)$
$$ 
\begin{aligned}
\mathcal{L} &=
-\log\pi_\theta(y_w|y_l,x) \\ 
&= - \log \frac{\pi_\theta(y_w,y_l,x)}{\mathbb{E}_q[\frac{\pi_\theta(y_w,y_l,x)}{Q(y_w)}]} \\
& \ge -\log\pi_\theta(y_w,y_l,x) +ELBO(q)\\
& =  -\log\pi_\theta(y_w,y_l,x) + \mathbb{E}_q[\log\pi_\theta(y_w,y_l,x) - \log{Q(y_w)}] \\
&= -log{\pi_\theta(y_w,y_l,x)} + \mathbb{E}_q[\log{\pi_\theta(y_l|y_w,x)}] - KL[Q(y_w)||\pi_\theta(y_w)] \\
& = -\log{\pi_\theta(y_w,x)} - KL[Q(y_w)||\pi_\theta(y_w)] \\

\end{aligned}$$

因为$$-\log\pi_\theta(y_w|y_l,x) = \log\pi_\theta(y_l|y_w,x) $$
$$ 
\begin{aligned}
\mathcal{L} &=
-\log\pi_\theta(y_w|y_l,x)  \\
&=\log{\pi_\theta(y_l,x)} + KL[Q(y_l)||\pi_\theta(y_l)]
\end{aligned}$$