策略梯度(Policy Gradient, PG)算法

对各种强化学习任务来说，策略梯度算法是另一种选择。策略梯度方法直接对策略进行建模,优化取决于此策略的回报（目标）函数值，然后可以应用各种算法来优化θ以获得最佳奖励。策略通常用参数为$\theta$的参数方程$\pi_\theta(a|s)​$来表示。

策略梯度网络的中心思想就是通过$\nabla_\theta J(\theta)$的方向直接调整策略的参数$\theta$来最大化目标函数$J(\theta)=\mathbb{E}_{s \sim \rho,a \sim \pi_\theta}[R]$,使用前面定义的Q函数，策略的梯度可以表示为

$$\nabla_\theta J(\theta)=\mathbb{E}_{s \sim \rho,a \sim \pi_\theta}[\nabla_\theta log\pi_\theta(a|s)Q^\pi (s,a)]​$$

策略梯度的几种实用算法的不同之中在于对$Q^\pi$的估计方法上，行动者-评价家（Actor Critic)算法，引入了状态-价值模型，其中包含两个模型，一个是策略模型，一个是价值模型，其中Actor表示策略模型，Critic表示价值模型用来学习真实的动作价值函数$Q^\pi(s,a) ​$。

然而PG算法存在以下缺陷：

1. 即使通过PG学习得到了随机策略之后，在每一步行为时，我们还需要对得到的最优策略概率分布进行采样，才能获得action的具体值；而action通常是高维的向量，比如25维、50维，在高维的action空间的频繁采样，无疑是很耗费计算能力的；

2. 在PG的学习过程中，每一步计算policy gradient都需要在整个action space进行积分: 

$$
\nabla \theta=\int_S \int_A \rho(s)\pi_\theta(a|s)Q^\pi(s,a)dads
$$

   这个积分我们一般通过Monte Carlo 采样来进行估算，需要在高维的action空间进行采样，耗费计算能力。

决定策略梯度(Deterministic Policy Gradient, DPG) 算法
决定策略梯度算法将将策略梯度算法拓展到决定策略$\mu_\theta:S \rightarrow A​$. 这个函数$\mu_\theta​$即最优行为策略，不再是一个需要采样的随机策略。



在确定情况下我们可以将目标函数$J(\theta)=\mathbb{E}_{s \sim \rho^\mu}[R(s,a)]$的梯度写为

$$
\nabla_{\theta} J(\theta)=E_{s \sim \beta}\left[\nabla_{\theta} \mu_{\theta}(s) \nabla_{a} Q^{\mu}\left.(s, a)\right|_{a=\mu_{\theta}(s)}\right]
$$
DPG是使用AC的方法来估计一个Q函数，并结合Q-learning或者Gradient Q-learning这些传统的Q函数学习方法，经过训练得到一个确定性的最优行为策略函数。

深度决定策略梯度算法（Deep Deterministic Policy Gradient, DDPG)是DPG算法的变种，其中策略$\mu$和critic的$Q^\mu$是用深度神经网络来近似的，借鉴了DQN经验回放与目标网络的技巧。

多智能体决定策略梯度(Multi-Agent Deep Deterministic Policy Gradient, MADDPG)

通过将其他智能体看做环境的一部分，直接将单智能体强化学习方法应用到多智能体强化学习上是存在问题的。因为在每个每个智能体看来环境都是非平稳的，也就是破坏了马尔可夫模型假设的收敛性。 而在DDPG这种使用深度神经网络来近似策略函数和动作价值函数的方法面临更严重的收敛性问题。

MADDPG算法的核心思想是学习为每个智能体在全局信息下学习一个中心化的Q函数来缓解非平稳问题和训练的稳定性。

更具体地来说，考虑一个N个智能体的博弈，我们用 $\theta=\left[\theta_{1}, \cdots, \theta_{n}\right]$ 表示n个智能体策略的参数，  $\pi=\left[\pi_{1}, \cdot, \pi_{n}\right]$表示n个智能体的策略。针对第i个智能体的累积期望奖励  $J\left(\theta_{i}\right)=E_{s \sim \rho^{\pi}, a_{i} \sim \pi_{\theta_{i}}}\left[\sum_{t=0}^{\infty} \gamma^{t} r_{i, t}\right]$，针对随机策略，求策略梯度为：

$$
\nabla_{\theta_{i}} J\left(\theta_{i}\right)=E_{s \sim \rho^{\pi}, a_{i} \sim \pi_{i}}\left[\nabla_{\theta_{i}} \log \pi_{i}\left(a_{i} | o_{i}\right) Q_{i}^{\pi}\left(x, a_{1}, \cdots, a_{n}\right)\right]
$$
其中 $o_{1}$ 表示第i个智能体的观测，   $x=\left[o_{1}, \cdots, o_{n}\right]$表示观测向量，即状态。 $Q_{i}^{\pi}\left(x, a_{1}, \cdots, a_{n}\right)$ 表示第i个智能体集中式的状态-动作函数。由于是每个智能体独立学习自己的 $Q_{i}^{\pi}$ 函数，因此每个智能体可以有不同的奖励函数（reward function），因此可以完成合作或竞争任务。

集中式的critic的更新方法借鉴了DQN中TD与目标网络思想
$$

L\left(\theta_{i}\right)=E_{x, a, r, x^{\prime}}\left[\left(Q_{i}^{\mu}\left(x, a_{1}, \cdots, a_{n}\right)-y\right)^{2}\right]
$$

其中，
$$
\mathrm{y}=\mathrm{r}_{\mathrm{i}}+\gamma \overline{\mathrm{Q}}_{\mathrm{i}}^{\mu^{\prime}}\left.\left(\mathrm{x}^{\prime}, \mathrm{a}_{1}^{\prime}, \cdots, \mathrm{a}_{\mathrm{n}}^{\prime}\right)\right|_{\mathrm{a}_{\mathrm{j}}^{\prime}=\mu_{\mathrm{j}}^{\prime}\left(\mathrm{o}_{\mathrm{j}}\right)}
$$
$\overline{Q}_{i}^{\mu^{\prime}}$ 表示目标网络， $$\mu'=[\mu_1',\cdots,\mu_n']$$ 为目标策略具有滞后更新的参数 $\theta_{j}^{\prime}$ 。其他智能体的策略可以采用拟合逼近的方式得到，而不需要通信交互。需要注意的是集中训练的Q函数仅仅在训练时使用，在分布式的执行过程中，每个智能体的策略函数$\mu_{\theta_i}$仅仅需要本地观察信息$o_i$来产生动作





极小化极大优化(Minimax Optimization)算法

在多智能体强化学习中，智能体的策略对对手的策略十分敏感。特别是在竞争环境中，当竞争对手改变策略后，智能体已经学习的策略可能十分脆弱。极小化极大优化算法，是一种找出失败的最大可能性中的最小值的算法。Minimax算法常用于棋类等对抗博弈问题的求解。该算法是一种零总和算法，即一方要在可选的选项中选择将其优势最大化的选择，而另一方则选择令对手优势最小化的方法。这里我们引入Minimax算法意图训练得到更为鲁棒的策略。

1. Minimax是一种悲观算法，即假设对手每一步都会将我方引入从当前看理论上价值最小的格局方向，即对手具有完美决策能力。因此我方的策略应该是选择那些对方所能达到的让我方最差情况中最好的，也就是让对方在完美决策下所对我造成的损失最小。

2. Minimax不找理论最优解，因为理论最优解往往依赖于对手是否足够愚蠢，Minimax中我方完全掌握主动，如果对方每一步决策都是完美的，则我方可以达到预计的最小损失格局，如果对方没有走出完美决策，则我方可能达到比预计的最悲观情况更好的结局。总之我方就是要在最坏情况中选择最好的

