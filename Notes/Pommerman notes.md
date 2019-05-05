Pommerman notes

Envirment Github : [Pommerman](<https://github.com/MultiAgentLearning/playground/tree/master/pommerman>)

Competition MainPage : [Build an AI to Compete against the World.](<https://www.pommerman.com/>)

Blogs about the Skynet team : [The Pommerman team competition or: How we learned to stop worrying and love the battle](<https://www.borealisai.com/en/blog/pommerman-team-competition-or-how-we-learned-stop-worrying-and-love-battle/>)

Pommerman 环境基于经典的Nintendo主机游戏Bomberman， 是NeurIPS2018会议期间举行的团队比赛

The Borealis AI team, 

consisting of Edmonton researchers Chao Gao, Pablo Hernandez-Leal, Bilal Kartal and research director, Matt Taylor, 

won 2nd place in the learning agents category,  在学习智能体类别中名列第二

and 5th place in the global ranking including (non-learning) heuristic agents. 在全球排名中名列第5

Pommerman团队比赛包括了4个炸弹人智能体放置在一个11*11的对称棋盘中，有两个队伍，每个队伍包含两个智能体

竞赛规则如下

- 在每个时间步，每个智能体都有能力执行六个动作中的一个：它们可以在四个基本方向中的任何一个方向上移动，保持原位，或放置炸弹。
- 棋盘上的每个单元都可以作为通道（智能体可以在它上面行走），刚性墙（不能被破坏），或木板（可以用炸弹摧毁）。

- 作为单独级别的游戏地图是随机生成的;但是，任何智能体之间始终保证存在路径，以便保证程序生成地图的可玩性。
- 每当一个特工放置炸弹时，它会在10个步骤后爆炸，产生寿命为两倍的火焰。火焰摧毁木材并杀死其爆炸半径范围内的任何物质。当木材被摧毁时，沉降物会显示通道或通电（见下文）。
- 在比赛期间影响运动员能力的物品的加电可以有三种类型：i）它们增加炸弹的爆炸半径; ii）他们增加了智能体可以放置的炸弹数量;或iii）他们有能力踢炸弹。
- 每个游戏剧集最多持续800次。结束游戏有两种方法：如果一支球队在达到这个上限之前获胜，那么游戏就结束了。如果没有，则以800次步长调用平局，游戏结束。

Challenges:

The Pommerman team competition is a very challenging benchmark for reinforcement learning methods. Here’s why:

- Sparse, delayed reward : 在游戏结束之前，智能体不会获得奖励，这可能需要800次步骤。 这种单一奖励是+1或-1。 当两个智能体在相同的时间步长死亡时，它们将被分配-1，这使得时间信用分配问题temporal credit-assignment problem[2]具有挑战性。 信用分配问题temporal credit-assignment problem试图解决从稀疏延迟奖励中奖励原子动作的问题。
- **Noisy rewards**: 在Pommerman游戏中，由于潜在的自杀，观察到的奖励可能会很嘈杂。 例如，考虑只使用两个智能体的简单场景 - 在这种情况下，我们的智能体和对手。 当我们的经纪人获得+1的奖励因为对手自杀（不是由于我们的经纪人的战斗技能）时，我们认为情节是假阳性false negative， 假阴性事件是学习合理行为的主要瓶颈，在无模型RL中进行纯粹的探索。 此外，假阳性事件也可以奖励代理人任意（被动）政策，如露营，而不是积极地与对手交往。
- **Partial observability**: 智能体只能观察他们周围的区域。 这会产生一些问题。 例如，如果一个炸弹的爆炸半径大于智能体的观察区域，则它甚至不会看到炸弹就会死亡。 当炸弹被一个智能体踢出后移动时会出现另一个问题。 炸弹变成射弹，与爆炸链一起使环境非常随机。
- **Vast search space**: 鉴于四个代理中的每一个都有六个可用的动作并同时提供游戏，联合搜索空间中的可能动作的数量为1296.由于一个完整的Pommerman游戏可以持续高达800个步骤，我们可以估计搜索 空间复杂度为$(1296)^{800}≈10^{2400}$; 即比Go大得多。
- **Lack of a fast-forward simulator**: The competition requires near real-time decision-making, i.e., within 100ms per move. However, the built-in game forward model is rather slow. This renders vanilla search algorithms ineffective.
- **Difficulty of learning to place a bomb : **

- **Multi-agent challenges** : 1.两个智能体（同伙一方）不被允许共享集中控制器 2.环境的竞争性，团队并不能事先了解其竞争对手的情况 3.多智能体信用分配multiagent credit assignment， 对同一团队的两个成员给予相同的情节奖励。没有关于每个智能体的明确贡献的信息。
- **Opponent generalization challenge** 逼迫对手自杀或者利用游戏漏洞而不是学习到泛化性强的游戏策略

The Skynet Resolution

A Skynet team is composed of a single neural network and is based on five building blocks:

1. parameter sharing

允许智能体分享单个网络的参数。也就是说网络的训练数据来源于两个agent的经验。但是，两个智能体因为观察到的环境不同所以即使是同一个网络，他们的行为也并不相同

2. **reward shaping**

为帮助智能体提高学习表现，我们增加了密集回报，从difference reward mechanism获得的灵感，即为智能体的行为提供更多的有意义的回报，而不只是使用单一的全局回报

3. an Action Filter module

为智能体增加先验知识，告诉他什么能做，什么不能做再让agent去do by trial-and-error.
好处：
1)简化学习问题
2)简单技巧的学习

4. opponent curriculum learning
5. an efficient RL algorithm

神经网络用PPO进行训练，目标函数
$$
o(\theta ; \mathcal{D})=\sum_{\left(s_{t}, a_{t}, R_{t}\right) \in \mathcal{D}}\left[-\operatorname{clip}\left(\frac{\pi_{\theta}\left(a_{t} | s_{t}\right)}{\pi_{\theta}^{o l d}\left(a_{t} | s_{t}\right)}, 1-\epsilon, 1+\epsilon\right) A\left(s_{t}, a_{t}\right)+\frac{\alpha}{2} \max \left[\left(v_{\theta}\left(s_{t}\right)-R_{t}\right)^{2},\left(v_{\theta}^{o l d}\left(s_{t}\right)+\operatorname{clip}\left(v_{\theta}\left(s_{t}\right)-v_{\theta}^{o l d}\left(s_{t}\right),-\epsilon, \epsilon\right)-R_{t}\right)^{2}\right]\right].
$$
$\theta$是神经网络

$D$是$\pi^{old}_\theta​$的状态空间的采样

$\epsilon$是调节参数

专门设置两种对手来提升训练：

- **Static opponent teams**: opponents do not move, nor place bomb.  

- **SmartRandomNoBomb** : players that do not place bombs; however, they are “smart random”, i.e., they have the action filter as described above. The reason we allowed the opponent to *not* place a bomb is that we realized the neural net can focus on learning true “blasting” skills, and not a skill that solely relies the opponent's mistakenly suicidal actions. Also, this strategy avoids training on “false positive” reward signal caused by an opponent's involuntary suicide.



Network architecture ： 

As shown in the figure below, the architecture first repeats four convolution layers, followed by two policy and value heads, respectively.



![](https://www.borealisai.com/media/filer_public_thumbnails/filer_public/27/d7/27d7feda-e62b-466f-8a62-c69f07621c26/blog-pommerman-img3.png__1042x2000_q85_subsampling-2.png)

Instead of using an LSTM to track the observational history, we used a “retrospective board” to keep track of the most recent value of each cell on the board. For cells outside an agent's purview, the “retrospective board” filled the unobserved elements of the board with the elements that were observed most recently. The input feature counts 14 planes in total, where the first 10 planes are extracted from the agent's current observation, while the remaining four come from the “retrospective board”. 

*Lessons learned and future work*

- Combine search and learning agents in an imitation-learning framework. For example, planning algorithms can continuously provide expert trajectories that RL agents could mimic to speed up learning.

- use of Bayesian inference for opponent detection
- from the competition that effective cooperation in Pommerman is still an open problem.