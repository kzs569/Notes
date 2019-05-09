# Speech Separation

## Introduction

语音分离是指将目标语音从背景干扰中分离出来的任务。传统上，语音分离被当作一个信号处理问题。最近出现一种新方法把语音分离作为监督学习问题处理，从训练数据中学习语音、说话人和背景噪声的判别模式(discriminative pattern)。

- 语音增强（语音-非语音分离）

- 说话人分离（多人谈话分离）

- 语音混响削减

- 麦克风阵列技术

语音分离的目标是把目标语音从背景干扰中分离出来。在信号处理中，语音分离属于很基本的任务类型，应用范围很广泛，包括听力假体、移动通信、鲁棒的自动语音以及说话人识别。人类听觉系统能轻易地将一个人的声音和另一个人的分离开来。即使在鸡尾酒会那样的声音环境中，我们似乎也能毫不费力地在其他人的说话声和环境噪声的包围中听到一个人的说话内容。因此语音分离问题通常也被叫做「鸡尾酒会问题」（cocktail party problem），该术语由 Cherry 在他 1953 年那篇著名论文中提出 [22]。



## 语音分离的问题描述（数学描述、文字描述）、问题分类

鸡尾酒会问题(cocktail party problem)

- n个人，n个麦克风。从n个麦克风得到一组数据：

  $$
  \left\{\mathrm{x}^{(i)}\left(x_{1}^{(i)}, x_{2}^{(i)}, \ldots, x_{n}^{(i)}\right) ; i=1, \dots, m\right\}
  $$
  其中，i表示采样的时间顺序，也就说共得到了m组采样，每一组采样都是n维的。
  
- 我们的目标是单单从这m组采样数据中分别出每个人说话的信号s。有n个信号源
  $$
s\left(s_{1}, s_{2}, \dots, s_{n}\right)^{T}, \quad \mathrm{s} \in \mathbb{R}^{n}
  $$
s相互独立
  
- A是一个未知的混合矩阵(mixing matrix),用来组合叠加信号s。


根据传感器或麦克风的数量，分离方法可以分为

- 单声道方法
  - 传统方法：CASA、NMF
- 阵列方法
  由两个或更多的麦克风组成的阵列使用不同的语音分离方法。波束成形，或者说空间滤波器，通过恰当的阵列结构增强从特定的方向到达的信号，进而削减来自其它方向的干扰 。最简单的波束成形是一种延迟-叠加技术，能将来自目标方向的多个麦克风的信号以相同的相位相加，并根据相差削减来自其它方向的信号。噪声的削减量取决于阵列的间隔、尺寸和结构，通常随着麦克风数量和阵列长度的增加，削减量也会增加。显然，当目标源和干扰源被共置，或者很靠近的时候，空间滤波器是无法应用的。此外，在回声场景中，波束成形的效用大幅降低，对声源方向的判定变得模糊不清。

## 语音分离的历史发展流程（几种经典方法和派系，基于深度学习方法的派系）





一种最近提出的方法将语音分离当作一个监督学习问题。监督语音分离的最初形成受CASA中时频掩模(time-frequency(T-F)masking)概念的启发。CASA的主要目标是理想二值掩模(ideal binary mask, IBM),表示信号是否控制混合信号时频表示中的一个T-F单元。听力研究显示，理想二值掩模能够显著提高正常听力者和听力受损者在嘈杂环境中的语音理解能力。以IBM作为计算目标，则语音分离变成了二值分类问题，这正是监督学习的一种基本形式。在这种情况下，IBM被当作训练中的目标信号或目标函数。在测试中，学习机器的目的就是估计 IBM，这也是监督语音分离的第一训练目标（参见 Sect. III）。

## 单通道监督学习语音分离的系统架构

**基于时频域的单通道监督学习语音分离的系统架构**

![1557294649386](C:\Users\kzs56\AppData\Roaming\Typora\typora-user-images\1557294649386.png)

#### 1.Time-Frequency representation时频分解

**short-time Fourier transform(STFT,短时傅里叶变换)**

STFT用于决定随时间变化的信号局部部分的正弦频率和相位。实际上，计算STFT的过程是将长时间信号分成数个较短的等长信号，然后再分别计算每个较短段的傅里叶变换。通常拿来描绘频域和时域上的变化。

我们这里指的均为连续短时傅里叶变换，简单来说，在连续时间上，一个函数可以先乘上仅在一段时间不为零的窗函数再进行一维的傅里叶变换。再将这个窗函数沿着时间轴挪移，所得到一系列的傅里叶变换结果排开则成为二维表象。

其数学表达为：
$$
X(t, f)=\int_{-\infty}^{\infty} w(t-\tau) x(\tau) e^{-j 2 \pi f \tau} d \tau
$$
其中$w(t)$是窗函数，$x(t)$是待变换信号。$X(t,f)$是$w(t-\tau) x(\tau)$的傅里叶变换。随着t的改变，窗函数在时间轴上会有位移。经过$w(t-\tau) x(\tau)$后，信号只留下了窗函数截取的部分做最后的傅里叶变换，所得到的结果为一复数函数，代表着信号随时间与频率改变的大小与相位。

对应的傅里叶能量幅度谱$p_x(t,f)$为
$$
p_{x}(t, f)=|X(t, f)|
$$
其中$|\cdot|$表示复数域的取模操作。为了简化符号表示，用向量$p \in \mathbf{R}_{+}^{F \times 1}$ 表示时间帧为t的幅度谱，这里F是傅里叶变换的频带数。

#### 2.Feature Extraction 特征提取

***Mel-domain***

**Mel-frequency cepstral coefficient(MFCC,梅尔倒谱系数)**

为了计算MFCC, 输入信号进行20 ms 帧长和10 ms 帧移的分帧操作, 然后使用一个汉明窗进行加窗处理, 利用STFT 计算能量谱, 再将能量谱转化到梅尔域, 最后, 经过对数操作和离散余弦变换(Discrete cosine transform, DCT) 并联
合一阶和二阶差分特征得到39 维的MFCC.

**Delta-spectral cepstral coefficient(DSCC)**

which is similar to MFCC except that a delta operation is applied to mel-spectrum.



***Linear Prediction***

**Perceptual linear prediction(PLP)**

 PLP能够尽可能消除说话人的差异而保留重要的共振峰结构, 一般认为是与语音内容相关的特征, 被广泛应用到语音识别中. 和语音识别一样, 我们使用12 阶的线性预测模型, 得到13 维的PLP 特征.

**Relative spectral trans-form PLP(RASTA-PLP)**

 RASTA-PLP 引入了RASTA 滤波到PLP, 相对于PLP 特征, RASTA-PLP 对噪音更加鲁棒, 常用于鲁棒性语音识别. 和PLP 一样, 我们计算13 维的RASTA-PLP 特征.



***Gammatone Features***

**Gammatone feature(GF) **

GF 特征的提取方法和GFCC 类似, 只是不需要DCT 步骤. 一般提取64 维的GF 特征.

**Gammatone frequency cepstral coeffcient(GFCC)**

 GFCC 特征是通过Gammatone 听觉滤波得到的. 我们对每一个Gammatone 滤波输出按照100 Hz 的采样频率进行采样. 得到的采样通过立方根操作进行幅度压制. 最后, 通过DCT 得到GFCC.  一般提取31 维的GFCC 特征.

**Gammatone frequency modulation coefficient(GFMC)**



***zero-crossing features***

**Zero-Crossings with Peak-Amplitudes(ZCPA)**

computes zero-crossing intervals and corresponding peak amplitudes from subband signals derived using a gammatone filterbank.



***Autocorrelation features***

**Relative Autocorrelation Sequence MFCC(RAS-MFCC)**

**Autocorrelation Sequence MFCC(AC-MFCC)**

**Phase Autocorrelation MFCC(PAC-MFCC)**

all of which apply the MFCC procedure in the autocorrelation domain



***medium-time filtering features***

**power normalized cepstral coefficients (PNCC)**

**suppression of slowly-varying components and the falling edge of the power envelope (SSF)**



***modulation domain features***

**Gabor filterbank (GFB)**

**Amplitude modulation spectro-gram(AMS)**

为了计算AMS 特征, 输入信号进行半波整流, 然后进行四分之一抽样, 抽样后的信号按照32 ms 帧长和10 ms 帧移进行分帧, 通过汉明窗加窗处理, 利用STFT 得到信号的二维表示, 并计算STFT 幅度谱, 最后利用15 个中心频率均匀分布在15.6»400 Hz 的三角窗, 得到15 维的AMS 特征.



**基于基音的特征(Pitch-based feature)**

基于基音的特征是时频单元级别的特征, 需要对每一个时频单元计算基音特征. 这些特征包含时频单元被目标语音主导的可能性. 我们计算输入信号的Cochleagram, 然后对每一个时频单元计算6 维的基音特征.



**Multi-resolution cochleagram(MRCG)**

MRCG 的提取是基于语音信号的Cochleagram 表示的. 通过Gammatone 滤波和加窗分帧处理, 我们能得到语音信号的Cochleagram 表示, 然后通过以下步骤可以计算MRCG.
步骤1. 给定输入信号, 计算64 通道的Cochle-agram, CG1, 对每一个时频单元取对数操作.
步骤2. 同样地, 用200 ms 的帧长和10 ms 的帧移计算CG2.
步骤3. 使用一个长为11 时间帧和宽为11 频带的方形窗对CG1 进行平滑, 得到CG3.
步骤4. 和CG3 的计算类似, 使用23 £ 23 的方形窗对CG1 进行平滑, 得到CG4.

步骤5. 串联CG1, CG2, CG3 和CG4 得到一个64 £ 4 的向量, 即为MRCG.
MRCG 是一种多分辨率的特征, 既有关注细节的高分辨率特征, 又有把握全局性的低分辨率特征.

**傅里叶幅度谱(FFT-magnitude)**

输入的时域信号进行分帧处理, 然后对每帧信号进行STFT,得到STFT 系数, 然后对STFT 进行取模操作即得到STFT 幅度谱.

**傅里叶对数幅度谱(FFT-log-magnitude)**

STFT 对数幅度谱是在STFT 幅度谱的基础上取对数操作得到的, 主要目的是凸显信号中的高频成分.

![](https://ws1.sinaimg.cn/large/006ocvumgy1g2tyjllr1kj32000xc1kx.jpg)

![](https://ws1.sinaimg.cn/large/006ocvumgy1g2tyku0yyej323114079l.jpg)

#### 3.Separation Targets 分离目标

1. 理想二值掩模(Ideal Binary Mask, IBM)

     The first training target used in supervised speech separation which is inspired by the *auditory masking phenomenon in audition* and *the exclusive allocation principle in auditory scene analysis*.

     The IBM is defined on a two-dimensional T-F representation of a noisy signal, such as a cochleagram or spectrogram：
$$
     I B M=\left\{\begin{array}{ll}{1,} & {\text { if } S N R(t, f)>L C} \\ {0,} & {\text { otherwise }}\end{array}\right.
$$
     where t and f denote time and frequency,respectively. The IBM labels every T-F unit as either target-dominant or interference-dominant. As a result, IBM estimation can naturally be treated as a supervised classification problem. A commonly used cost function for IBM estimation is cross-entropy.

2. 理想浮值掩模(Ideal Ratio Mask, IRM)

     Instead of a hard label on each T-F unit, the IRM can be viewed as a soft version of IBM:
     $$
     I R M=\left(\frac{S(t, f)^{2}}{S(t, f)^{2}+N(t, f)^{2}}\right)^{\beta}
     $$
     where $S(t,f)^2$ and $N(t,f)^2$ denote speech energy and noise energy within a T-F unit, respectively. The tunable parameter $\beta$ scales the mask, and is commonly chosen to 0.5. With the square root the IRM preserves the speech energy with each T-F unit, under the assumption that S(t,f) and N(t, f) are uncorrelated. Without the root the IRM in above function is similar to the classical in the power spectrum. MSE is typically used as the cost function for IRM estimation. 

3. 理想相位感知掩模(Ideal Phase-Sensitive Mask, IPSM)

     The phase-sensitive mask (PSM) extends the spectral magnitude mask(SMM) by including a measure of phase:
     $$
     \operatorname{PSM}(t, f)=\frac{|S(t, f)|}{|Y(t, f)|} \cos \theta
     $$
     where $\theta$ denotes the difference of the clean speech phase and the noisy speech phase within the T-F unit. The inclusion of the phase difference in the PSM leads to higher SNR, and tends to yield a better estimate of clean speech than the SMM.

4. IAM

5. Complex Ideal Ratio Mask, cIRM

     The cIRM is an ideal mask in the complex domain. Unlike the aforementioned masks, it can perfectly reconstruct clean speech from noisy speech:
     $$
     S=c I R M * Y
     $$
     where S,Y denote the STFT of clean speech and noisy speech, respectively, and * represents complex multiplication. Solving for mask components results in the following definition:
     $$
     \operatorname{cIRM}=\frac{Y_{r} S_{r}+Y_{i} S_{i}}{Y_{r}^{2}+Y_{i}^{2}}+i \frac{Y_{r} S_{i}-Y_{i} S_{r}}{Y_{r}^{2}+Y_{i}^{2}}
     $$
     where $Y_r$ and $Y_i$ denote real and imaginary components of noisy speech, respectively, and $S_r$ and $S_i$ real and imaginary components of clean speech, respectively. The imaginary unit is denoted by 'i'.
     Because of complex-domain calculations, mask values become unbounded. So some form of compression should be used to bound mask values, such as a tangent hyperbolic or sigmoidal function.
#### 4.Model Training

#### 5. Waveform Composition

**Inverse short-time Fourier transform, ISTFT 逆短时傅里叶变换**

ISTFT从$X(t,f)$精确重构$x(k)$,也就是说可以通过估计目标语音的短时傅里叶变换系数来实现语音的分离或者增强，用$\hat{Y}_{s}(t, f)$来表示估计的目标语音的短时傅里叶变换系数，那么目标语音的波形$\hat{s}(k)$可以通过ISTFT计算：
$$
\hat{s}(k)=\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \hat{Y}_{s}(k) w(k-t) \exp (j 2 \pi f k) \mathrm{d} f \mathrm{d} k
$$




**基于时域的单通道语音分离的系统架构**

Time-domain approaches have typically relied on differences in the statistical properties of the sources being separated. These methods model the statistics of the target and interfering sources, which can be used in computational frameworks such as the MLE.

#### Independent Component Analysis(ICA,独立成分分析)

根据上文鸡尾酒会问题的描述，我们得到独立成分分析的解法步骤

1. 我们可以得到
   $$
   x=As
   $$
   其中，x是一个矩阵

2. 其中每个列向量
   $$
   x^{(i)}=As^{(i)}
   $$
   ![](https://ws1.sinaimg.cn/large/006ocvumgy1g2v256uo2aj30ed095t92.jpg)

3. A和s都是未知的，x是已知的，我们要想办法根据x来推出s。这个过程也称为盲信号分离。
    令$W = A^{-1}$,那么$s^{(i)}=A^{-1}x^{(i)}=Wx^{(i)}$
$$
W=\left[ \begin{array}{c}{-w_{1}^{T}-} \\ {\vdots} \\ {-w_{n}^{T}-}\end{array}\right]
$$

4. 最终得到：
$$
s_{j}^{(i)}=w_{j}^{T} x^{(i)}
$$
  其中，$s^j_{(i)}$ 表示speaker j在时刻i发出的信号；所以综上，我们需要知道两个量才能求出另一个。

**ICA算法的预处理**

- 中心化：$x^{\prime}=x-\bar{x}$, 其中$\bar{x}$是x的均值

- 漂白：目的是为了让x相互对立。将x乘以一个矩阵变成$\tilde{\mathbf{x}}$(其协方差矩阵是$I$)
  $$
  \tilde{\mathbf{x}}=\mathbf{E} \mathbf{D}^{-1 / 2} \mathbf{E}^{T} \mathbf{x}
  $$
  其中，$E\left\{\tilde{\mathbf{x}} \tilde{\mathbf{x}}^{T}\right\}=\mathbf{I}$
  
  其中使用特征值分解来得到$E$(特征向量矩阵)和$D$(特征值对角矩阵)，计算公式为$E\left\{\tilde{\mathbf{x}} \tilde{\mathbf{x}}^{T}\right\}=EDE^T$
  

**ICA算法**

1. 我们假定每$s_i$有概率密度$p_s$,那么给定时刻原信号的联合分布就是
   $$
   \mathrm{p}(\mathrm{s})=\prod_{i=1}^{n} p_{s}\left(s_{i}\right)
   $$
   每个人发出的声音信号相互独立
   
2. 然后我们就可以求得$p(x)$
   $$
   \mathrm{p}(\mathrm{x})=\mathrm{p}_{s}(W x)|\mathrm{W}|=|\mathrm{W}| \prod_{i=1}^{n} p_{s}\left(w_{i}^{T} x\right)
   $$

3. 现在，我们需要知道$p(s)$和$w$,才能求得$p(x)$。

   首先，我们假设s的累积分布函数符合sigmoid函数
   $$
   g(s)=\frac{1}{1+e^{-s}}
   $$
   求导后
   $$
p_{s}(s)=g^{\prime}(s)=\frac{e^{s}}{\left(1+e^{s}\right)^{2}}
   $$
   这就是s的密度函数。这里s是实数
   
4. 接着用最大似然估计法求解$W$,使用前面得到的x的概率密度函数，得
   $$
   \ell(W)=\sum_{i=1}^{m}\left(\sum_{j=1}^{n} \log g^{\prime}\left(w_{j}^{T} x^{(i)}\right)+\log |W|\right)
   $$
   最终我们求得
   
   $$
   W:=W + \alpha (\left[ \begin{array}{c}{1-2g(w^T_1 x^{(i)})} \\ {1-2g(w^T_2 x^{(i)})} \\{\vdots} \\ {1-2g(w^T_n x^{(i)})}\end{array}\right]x^{(i)^T}+(W^T)^{-1})
   $$
   其中$\alpha$是梯度上升速率，人为指定。
   
5. 迭代求出W后，我们也可以还原出原始信号：
   $$
\mathbf{s}^{(i)}=W x^{(i)}
   $$



[机器学习15-3--独立成分分析ICA（Independent Component Analysis）](http://danieljyc.github.io/2014/06/13/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A015-3--%E7%8B%AC%E7%AB%8B%E6%88%90%E5%88%86%E5%88%86%E6%9E%90ica%EF%BC%88independent-component-analysis%EF%BC%89/)
[FastICA](<http://research.ics.aalto.fi/ica/fastica/>)

#### Non-negative Matrix Factorization(NMF,非负矩阵分解)

The NMF technique uses non-negative dictionaries to decompose the spectrogram of the mixture signal into speaker specific activations, and from these activations an isolated target signal can be approximated using the dictionaries.

## Evaluation 

## Datasets

**WSJ0(Wall Street Journal)** 

**TIMIT** contains broadband recordings of 630 speakers of eight major dialects of American English, each reading ten phonetically rich sentences. TIMIT corpus includes time-aligned orthographic, phonetic and word transcriptions as well as a 16-bit, 16kHz speech waveform file for each utterance.

## Competition

**CHiME Speech Separation and Recognition Challenge**



## SOTA

Deep Clustering(DPCL++)

Permutation Invariant Training(PIT)

Deep Attractor Network(DANet)

Conv-TasNet

## Still need to solve

- 声源数量已知
- 置换问题
- 远场效果差





### Probabilistic Models(like Factorial GMM-HMM)

model the temporal dynamics and the complex interactions of the target and competing speech signals. Unfortunately, these models assume and only work under close-set speaker conditions, i.e. the identity of the speakers must be known a prior.

### The Label Permutation Problem

与说话人无关的多说话人语音分离的难度在于标签的模糊性或排列问题。因为在混合信号中，音频源是对称的，所以在监督学习过程中，并不能预先确定的将正确源目标分配给对应输出层。因此，模型将无法很好地训练以分离语音。

Hershey et al.[111, 112]提出了一种被称为深度聚类（deep clustering/DPCL）的全新技术。这种模型假设每个时频区间都仅属于一个说话人。在训练过程中，每个时频区间都被映射到了一个嵌入空间。然后对这个嵌入进行优化，使属于同一个说话人的时频区间在这个空间中相距更近，属于不同说话人的则相距更远。在评估过程中，该模型会在嵌入上使用一个聚类算法来生成时频区间的分区。

Yu et al.[20]和 Kolbak et al.[21]则提出了一种更简单的技术排列不变训练（permutation invariant training/PIT）来攻克与说话人无关的多说话人语音分离问题。在这种新方法中，源目标被当作一个集合进行处理（即顺序是无关的）。在训练过程中，PIT 首先根据前向结果在句子层面上确定误差最小的输出-目标分配。然后再最小化基于这一分配的误差。这种策略一次性地简单直接地解决了标签排列问题和说话人跟踪问题。PIT 不需要单独的跟踪步骤（因此可用于实时系统）。相反，每个输出层都对应于源的一个流。

对于语音识别，我们可以将每个分离的语音流馈送给 ASR 系统。甚至还能做到更好，基于深度学习的声学模型也许可以和分离组件（通常是 RNN）进行端到端的联合优化。因为分离只是一个中间步骤，Yu et al.[124]提出直接在 senone 标签上使用 PIT 优化交叉熵标准，而不再需要明确的语音分离步骤。

Because the model estimates the masks $\hat{\mathbf{m}}_{1, i}$and$\hat{\mathbf{m}}_{2, i}$ simultaneously, and they depend on the same input mixture, it is unknown in advance whether the resulting output vector $\hat{\mathbf{u}}_{i}$ is ordered as  $\hat{\mathbf{u}}_{i}=\left[\hat{\mathbf{m}}_{1, i}^{T} \hat{\mathbf{m}}_{2, i}^{T}\right]^{T}$or $\hat{\mathbf{u}}_{i}=\left[\hat{\mathbf{m}}_{2, i}^{T} \hat{\mathbf{m}}_{1, i}^{T}\right]^{T}$. That is, the permutation of the output masks is unknown.

*a naive approach* to train a deep learning separation model, without exact knowledge about the permutation about the permutation of the output masks, *is to use a constant permutation* which need the prior information about the utterances and fails if the training set consists of many utterances spoken by many speakers of both genders.

**Permutation Invariant Training**

![](http://ww1.sinaimg.cn/large/006ocvumgy1g2t2b58glqj30ou0m7myi.jpg)

we associate the reference signals for speaker one and two, i.e. $a_{1,i}$ and $a_{2,i}$, to the output masks $\hat{\mathbf{m}}_{1, i}$ and
$\hat{\mathbf{m}}_{2, i}$, by computing the (total of $S^2$) pairwise MSE’s between each reference signal $a_{s,i}$ and each estimated source $\hat{a_{s,i}}$. We then determine the (total of S!) possible permutations between the references and the estimated sources, and compute the per-permutation-loss for each permutation.

The permutation with the lowest MSE is chosen and the model is optimized to reduce this least MSE.

简而言之就是不再按顺序计算error，而是把所有可能的error都计算出来，取最小的一个作为真正的error.



### Computational Auditory Scene Analysis(CASA,计算听觉场景分析)

CASA is based on perceptual principles of **auditory scene analysis** and exploits grouping cues(聚类约束) such as pitch(基音频率) and onset(起音). For example, the **tandem** algorithm separates voiced speech by alternating pitch estimation and pitch-based grouping.

CASA主要关注的领域是声源分离。这里的声源不单是指人的声音，也可能是其它各种声音（比如街上汽车和救护车的声音）---这些都是声源。声源分离的目标就是将这些声音分离开。针对这一问题早期的解决方式是通过统计的方法把声音里面的统计特性提取出来；计算听觉场景分析则在很大程度上是对人的听觉特性的模拟。

什么叫解决了鸡尾酒会问题？也就是说，如果把一个听觉信号在时间域和频率域两个维度（时频二维）进行表示（类似于视觉信号的x轴和y轴两个维度），你就可以把时频这二维表示成一个二维矩阵，这个矩阵中的每一个元素称为一个"时频元（time-frequency unit)"。我们开始研究的就是怎么量化这个时频元，后来我们发现这个量化只要二值就可以了---要么是0要么就是1。这跟传统的声源处理方法是完全不一样的。传统的声源处理要把信号分得很细。一个信号里面可能有很多组成部分---一个部分属于这个声源，另一个部分属于另一个声源。我们的方法就不需要分那么细，就只需要分一次---要么属于目标声源，要么就是背景噪声。这就是“二值”的意思。这样我们就把 CASA 问题变成了一个监督学习（supervised learning）问题；相对地，早期方法则是无监督的（unsupervised）——也就是说把一个信号的权值算一算，而不需要教它。我们从理想二值模的角度考虑，就把它变成了一个分类问题。

一旦把它变成了一个监督学习问题之后，我们就希望学习机的分类结果和理想二值掩模的分类是一样的。理想二值掩模是“理想的”，是在声音没有重叠之前计算出来的，就是说不管噪声比目标声音强多少倍，它都能将目标声音分离出来。

A.S. Bregman,*Auditory scene analysis*,  Cambridge MA:MIT Press,1990

G.Hu and D.L. Wang *"A **tandem** algorithm for pitch estimation and voiced speech segregation"* IEEE TASLP.2010

[专访大象声科汪德亮：利用深度学习解决「鸡尾酒会问题 」--机器之心](<https://www.jiqizhixin.com/articles/2017-02-11-4>)

- **Auditory masking** <https://www.sweetwater.com/sweetcare/articles/what-auditory-masking/>

Auditory masking is when the perception of one sound is affected by the presence of another sound. Masking can be simultaneous or non simultaneous. For this discussion we will focus on simultaneous masking.

This is when a signal, the sound that is desired to be heard, is made inaudible by a masker, noise or unwanted sound that is present throughout the signal.
A not masked threshold is the quietest level of the signal which can be perceived in quiet. Masked thresholds are the quietest level of the signal perceived when presented in noise. The amount of masking is the difference between the masked and not masked thresholds. For example if the masked threshold is 20dB and the not masked threshold is 35dB the amount of masking would be 15dB.

The basic masking test involves the not masked thresholds being measured on a subject. Then the masking noise is introduced at a fixed sound level and the signal is presented at the same time. The level of the signal is varied until the new threshold is measured. This is the masked threshold.

The phenomenon of masking is often used to investigate the auditory system’s ability to separate the components of a complex sound. For example if two sounds of two different frequencies (pitches) are played at the same time, two separate sounds can often be heard rather than a combination tone. This is otherwise known as frequency resolution or frequency selectivity. Frequency resolution is thought to occur due to filtering within the cochlea, the hearing organ in the inner ear. A complex sound is split into different frequency components and these components cause a peak in the pattern of vibration at a specific place on the basilar membrane within the cochlea. These components are then coded independently on the auditory nerve which transmits sound information to the brain. This individual coding only occurs if the frequency components are different enough in frequency, otherwise they are coded at the same place.

Masking illustrates the limits of frequency selectivity even in a normal hearing person. If a signal is masked by a masker with a different frequency to the signal then the auditory system was unable to distinguish between the two frequencies. Therefore by carrying out an experiment to see the conditions which are necessary for one sound to mask a previously heard signal, the frequency selectivity of the auditory system can be investigated.

- **窗函数**

[窗函数](https://zh.wikipedia.org/wiki/窗函數)通常满足下列特性:

1. ![{\displaystyle w(t)=w(-t)\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2086d6e37a35ea0302be4cb1d1e12f78de2cae8f)，即为偶函数。
2. ![{\displaystyle max(w(t))=w(0)\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3a6fbcdeb303d53a1c64df75fae36cd4e74cbe1c)，即窗函数的中央通常是最大值的位置。
3. ![{\displaystyle w(t_{1})\geq w(t_{2}),|t_{2}|\geq |t_{1}|}](https://wikimedia.org/api/rest_v1/media/math/render/svg/731391ebdfd152a498247a12533af7ddc7fc3e95)，即窗函数的值由中央开始向两侧单调递减。
4. ![{\displaystyle w(t)\cong 0,|t|\to \infty }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ea4a72af95ae74a5d7c8a44df9a0bc2d8e2c0e03)，即窗函数的值向两侧递减为零。

常见的[窗函数](https://zh.wikipedia.org/wiki/窗函數)有：方形、三角形、[高斯函数](https://zh.wikipedia.org/wiki/高斯函數)等，而短时距傅里叶变换也因窗函数的不同而有不同的名称。而[加伯变换](https://zh.wikipedia.org/wiki/加伯轉換)，即为窗函数是高斯函数的短时距傅里叶变换，通常没有特别说明的短时距傅里叶变换，即为[加伯变换](https://zh.wikipedia.org/wiki/加伯轉換)。

- **频谱(Spectrogram)**

Spectrogram即短时傅里叶变换后结果的绝对值平方，两者本质是相同的，在文献上也常出现spectrogram这个名词：
$$
S P_{x}(t, f)=|X(t, f)|^{2}=\left|\int_{-\infty}^{\infty} w(t-\tau) x(\tau) e^{-j 2 \pi f \tau} d \tau\right|^{2}
$$

For speaker-independent separation, the key issue is how to group well-separated speech signals at individual frames (or segments) across time. This is precisely the issue of sequential organization, which is much investigated in CASA.

In speaker separation, if the underlying speakers are not allowed to change from training to testing, this is the *speaker-dependent* situation. 

If interfering speakers are allowed to change, but the target speaker is fixed, this is called *target-dependent* speaker separation.

In the last constrained case where none of the speakers are required to be the same between training and testing, this is called *speaker-independent*.

# Inference

[wikipedia-短时距傅里叶变换]([https://zh.wikipedia.org/wiki/%E7%9F%AD%E6%99%82%E8%B7%9D%E5%82%85%E7%AB%8B%E8%91%89%E8%AE%8A%E6%8F%9B](https://zh.wikipedia.org/wiki/短時距傅立葉變換))