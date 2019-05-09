# Selling Multiple Items via Social Networks

## Abstract 

我们考虑卖方销售**多个商品单位**的市场在社交网络中。社交网络中的**每个节点/买家只能直接与她的邻居**，即卖家**沟通**如果她找不到，只能将商品卖给她的邻居一种通知其他买家的方法。在本文中，我们设计了一个新颖的促销
激励所有知情的买家的机制出售，**邀请所有邻居加入销售，即使无法保证他们的努力将得到支付**。虽然传统
促销活动，如赞助搜索拍卖不能保证广告客户（卖方）的正面回报，我们的机制保证卖方的收入优于不使用广告。更重要的是，卖方不需要付款如果广告不利于她。

## Introduction

Our advertising mechanism does not rely on any third party such as newspapers or search engines to do the advertisements. The mechanism is owned by the seller. The seller just needs to invite all her neighbors to join the sale, then her neighbors will further invite their neighbors and so on. In the end, all buyers in the
social network will be invited to participate in the sale. Moreover, all buyers are not paid in advance for their invitations and they may not get paid if their invitations are not beneficial to the seller. Although some buyers may never get paid for their efforts in the advertising, they are still incentivised to do so, which is one of the key features of our advertising mechanism. This significantly differs from existing advertising mechanisms used on the Internet.

我们的广告机制不依赖报纸或搜索引擎等任何第三方来做广告。该机制由卖方拥有。卖家只需要邀请所有邻居参加促销活动，然后她的邻居就会进一步邀请他们的邻居等等。最终，所有买家都在社交网络将被邀请参与销售。此外，所有买家都不会提前收到他们的邀请，如果他们的邀请对卖家不利，他们可能无法获得报酬。**虽然一些买家可能永远不会因为他们在广告中的努力而获得报酬，但他们仍然鼓励他们这样做**，这是我们广告机制的关键特征之一。这与因特网上使用的现有广告机制显着不同。

More importantly, our advertising mechanism not only incentivizes all buyers to do the advertising, but also guarantees that the seller’s revenue increases. That is, her revenue is never worse than the revenue she can get if she only sells the items to her neighbours.

更重要的是，我们的广告机制**不仅激励所有买家做广告，还保证卖家的收入增加。**也就是说，如果她只向邻居出售这些物品，她的收入绝不会低于她可以获得的收入。

Li et al. [8]  considered the setting when the seller sells only one item and proposed IDM(Information Diffusion Mechanism, 信息传递机制)， which guarantees that all buyers will truthfully report their willing payments (i.e. valuations) and also invite all their neighbors to join the sale.

对比baseline IDM, 本文提出GIDM which generalizes to settings where the seller sells multiple items.



主要分为两方面工作：

1.最大化卖家的收入

traditional market mechanisms， like VCG  assumed that the buyers are all known to the seller and the aim is to maximize the revenue among the fixed number of buyers.（所以卖家应该只知道部分目标客户，引入部分观测性 partial observation, 此时Myerson提出的改进的VCG其中的buyers' valuations将无法计算)

2.激励买家去分享信息（how information is propagated in a social network or how to design reward mechanisms to incentivize people to invite more people to accomplish a challenge together.）

basline DARPA Network Challenges的解决方案

## Model

在社交网络里 一个seller s sells K >= 1件商品，除了seller,社交网络里还有n个节点，$N=\{1, \cdots, n\}$，每个节点$i \in N \cup\{s\}$有一组邻居（即近邻节点）$r_{i} \subseteq N \cup\{s\}$。简单起见，我们假设seller的售卖的K个物品互不相同，每个买家至少需要一件商品，商品的价值非负。

在没有广告的情况下，卖家s只能卖给自己的neighbors, 因为这时其他非近邻节点对seller不可见，反之亦然。

Therefore, our goal here is to design a a kind of cost free advertising mechanism such that all buyers, who are aware of the sale, are incentivized to invite all their neighbors to join the sale with no guarantee that their efforts will be paid. IDM已经证明了这种机制在K=1时可行的，我们将其推广到K>=1上

那么我们怎么定义这个模型呢，首先我们定义每个buyer的type，对每个buyer $i \in N,\theta_{i}=\left(v_{i}, r_{i}\right)$，那么$ \theta=\left(\theta_{1}, \cdots, \theta_{n}\right)$就是buyer的类型集合。这里的v应该是value的意思，r上文有。

广告机制包含分配策略$\pi$和报酬策略x， The mechanism requires each buyer, who is aware of the sale, to report her valuation to the mechanism and invite/inform all her neighbours about the sale.

感觉后面这段话就是$\theta$就是这个博弈局面的表示

$x_{i}\left(\theta^{\prime}\right)$是估值函数

$\pi_{i}\left(\theta^{\prime}\right) \in\{0,1\}$是策略函数

Definition2.1 Given an action profile $\theta^{\prime}$ of all buyers, an invitation chain from the seller s to a buyer i is a buyer sequence of $\left(s, j_{1}, \cdots, j_{l}, j_{l+1}, \cdots, j_{m}, i\right)$ such that  $j_{1} \in r_{s}$, for all $1<l \leq m$ $j_{l} \in r_{j_{l-1}}^{\prime}, i \in r_{j_{m}}^{\prime}$and no buyer appears twice in the sequence, i.e. it is acyclic.

定义了invitation chain

Definition 2.2 Given the buyer's type profile $\theta$ ,an action profile $\theta^{\prime}$ is feasible if for all $i \in N$

- $\theta_{i}^{\prime} \neq n i l$ if and only if there exists an invitation chain from the seller s to i following the action profile $| \theta_{-i}^{\prime}$ (意思就是之后s到i之间有invitation chain，才不会有$\theta_{i}^{\prime} \neq n i l$)

- if $\theta_{i}^{\prime} \neq n i l$, then $r_{i}^{\prime} \subseteq r_{i}$

Let $\mathcal{F}(\theta)$be the set of all feasible action profiles of all buyers under type profile θ.

Definition 2.3 An allocation $\pi$ is feasible if for all $\theta \in \Theta$, for all $\theta^{\prime} \in \mathcal{F}(\theta)$,
• for all $i \in N$,  if $\theta_{i}^{\prime}=n i l,$ then $\pi_{i}\left(\theta^{\prime}\right)=0$
• $\sum_{i \in N} \pi_{i}\left(\theta^{\prime}\right) \leq \mathcal{K}$.

定义策略$\pi$何时为0

Definition 2.4. An allocation π is efficient  if for all $\theta \in \Theta$, for all $\theta^{\prime} \in \mathcal{F}(\theta)$,
$$
\pi \in \arg \max _{\pi^{\prime} \in \Pi} \sum_{i \in N, \theta_{i}^{\prime} \neq n i l} \pi_{i}^{\prime}\left(\theta^{\prime}\right) v_{i}^{\prime}
$$
即长期收益最大时，为本次博弈的最终目标

Definition 2.5. A mechanism $(\pi,x)$ is individually rational (IR) if $u_{i}\left(\theta_{i}, \theta^{\prime}\right) \geq 0$ for all $\theta \in \Theta$, for all $i \in N$, for all  $\theta^{\prime} \in \mathcal{F}(\theta)$ such that $\theta_{i}^{\prime}=\left(v_{i}, r_{i}^{\prime}\right)$

根据上文的$u_{i}\left(\theta_{i}, \theta^{\prime},(\pi, x)\right)=\pi_{i}\left(\theta^{\prime}\right) v_{i}-x_{i}\left(\theta^{\prime}\right)$ 公式，就是我这一步的动作不会使我本身已经获的收益减少，然后定义为IR系数

Definition 2.6. A mechanism (π,x) is incentive compatible (IC) if $u_{i}\left(\theta_{i}, \theta^{\prime}\right) \geq u_{i}\left(\theta_{i}, \theta^{\prime \prime}\right)$ for all $\theta \in \Theta$, for all $i \in N$, for all $\theta^{\prime},\theta^{\prime \prime} \in \mathcal{F}(\theta)$ such that $\theta_{i}^{\prime}=\theta_{i}$ and for all $j \neq i, \theta_{j}^{\prime \prime}=\theta_{j}^{\prime}$if there exists an invitation chain from the seller s to j following the action profile of $\left(\theta_{i}^{\prime \prime}, \theta_{-i}^{\prime}\right)$

同上

Definition 2.7. A mechanism (π,x) is weakly budget balanced if for all $\theta \in \Theta$, for all $\theta^{\prime} \in \mathcal{F}(\theta)$,$R^{(\pi, x)}\left(\theta^{\prime}\right) \geq 0$

## The Information Diffusion Mechanism $\mathcal{K}=1$

The essence of their approach is that a buyer is only rewarded for advertising if her invitations increase social welfare and the reward guarantees that inviting all neighbours is a dominant strategy for all buyers.

**Information Diffusion Mechanism (IDM)**
(1) Given a feasible action profile $\theta^{\prime}$, identify the buyer with the highest valuation, denoted by $i^∗$.
(2) Find all diffusion critical buyers of $i^∗$, denoted by $C_{i^∗},j \in C_{i^∗}$ if and only if without j’s action $\theta^{\prime}_j$ , there is no invitation chain from the seller s to $i^∗$ following $\theta^{\prime}_{-j}$, i.e. $i^∗$ is not able to join the sale without j.
(3) For any two buyers $i, j \in C_{i^{*}} \cup\left\{i^{*}\right\}$, define an order ≻i∗ such that i ≻i∗ j if and only if all invitation chains from s to j contain i.
(4) For each $i \in C_{i^{*}} \cup\left\{i^{*}\right\}$, if i receives the item, the payment of i is the highest valuation report without i’s participation. Formally, let N−i be the set of buyers each of whom has an invitation chain from s following $\theta^{\prime}_{-i}$, i’s payment to receive the item is $p_{i}=\max _{j \in N_{-i} \wedge \theta_{j}^{\prime} \neq n i l} v_{j}^{\prime}$
(5) The seller initially gives the item to the buyer i ranked first in $C_{i^{*}} \cup\left\{i^{*}\right\}$, let l = 1 and repeat the following
until the item is allocated.
• if i is the last ranked buyer in $C_{i^{*}} \cup\left\{i^{*}\right\}$, then i receives the item and her payment is $x_{i}\left(\theta^{\prime}\right)=p_{i}$;
• else if $v_{i}^{\prime}=p_{j}$ , where j is the (l + 1)-th ranked buyer in $C_{i^{*}} \cup\left\{i^{*}\right\}$, then i receives the item and her payment is $x_{i}\left(\theta^{\prime}\right)=p_{i}$;
• otherwise, i passes the item to buyer j and i’s payment is $x_{i}\left(\theta^{\prime}\right)=p_{i}-p_{j}$, where j is the (l + 1)-th ranked buyer in$C_{i^{*}} \cup\left\{i^{*}\right\}$. Set i = j and l = l + 1.
(6) The payments of all the rest buyers are zero.