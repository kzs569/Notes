# Speech Separation



## 语音分离的问题描述

**语音分离**是指将目标语音从背景干扰中分离出来的任务。传统上，语音分离被当作一个信号处理问题,应用范围很广泛，包括听力假体、移动通信、鲁棒的自动语音以及说话人识别。人类听觉系统能轻易地将一个人的声音和另一个人的分离开来。即使在鸡尾酒会那样的声音环境中，我们似乎也能毫不费力地在其他人的说话声和环境噪声的包围中听到一个人的说话内容。因此语音分离问题通常也被叫做「鸡尾酒会问题」（cocktail party problem），该术语由 Cherry 在他 1953 年那篇著名论文中提出。最近出现一种新方法把语音分离作为监督学习问题处理，从训练数据中学习语音、说话人和背景噪声的判别模式(discriminative pattern)。


鸡尾酒会问题(cocktail party problem)

- n个人，m个麦克风。从m个麦克风得到一组数据：

  $$
  \left\{\mathrm{x}^{(i)}\left(x_{1}^{(i)}, x_{2}^{(i)}, \ldots, x_{n}^{(i)}\right) ; i=1, \dots, m\right\}
  $$
  其中，i表示采样的时间顺序，也就说共得到了m组采样，每一组采样都是n维的。
  
- 我们的目标是单单从这m组采样数据中分别出每个人说话的信号s。有n个信号源
  $$
s\left(s_{1}, s_{2}, \dots, s_{n}\right)^{T}, \quad \mathrm{s} \in \mathbb{R}^{n}
  $$
s相互独立
  
- 在盲分离问题中,鸡尾酒会问题(假设无噪声的情况下)可以建模为一个free mixing model
  $$
  x=As
  $$
  where the mixing matrix A is unknown, we can recover the sources only using the observed data matrix X as soon as we know the mixing matrix A.
  
  [Blind Source Separation of Speech Signals using Mixing Matrix Estimation and Subspace Method](<https://www.ijert.org/research/blind-source-separation-of-speech-signals-using-mixing-matrix-estimation-and-subspace-method-IJERTCONV3IS12056.pdf>)
  
  

In the monaural speech separation task, a linearly mixed single-microphone signal 
$$
y[t]=\sum^S_{s=1}x_s[t]
$$
is given, where t is the time index, and $x_s[t](s\in\{1,2,...,S\})$ are S individual source signals.




根据分离对象的属性不同，分离方法可以分为

- 语音增强（语音-非语音分离）

- 说话人分离（多人谈话分离）

- 语音混响削减

根据传感器或麦克风的数量，分离方法可以分为

- 单声道方法
- 阵列方法

## 语音分离的历史发展流程（几种经典方法和派系，基于深度学习方法的派系）

1953年，**Edward Colin Cherry(E.C. Cherry)**在论文 *Some experiments on the recognition of speech, with one and with two ears* 中提出鸡尾酒会问题。

1990年，麦吉尔大学的**Albert Bregman**教授出版了《听觉场景分析（Auditory Scene Analysis）》,在书中提出了听觉场景分析理论ASA，后来被引入计算领域。

2006年，Wang D. and Brown G.J.在"Computational auditory scene analysis: principles, algorithms, and applications"中提出了计算听觉场景分析，旨在建立像人类一样处理鸡尾酒会问题的智能系统用以分离混合的声音，根据听觉场景分析研究中发现的一些规则或机制来对鸡尾酒会问题进行建模。

2013年，Wang等在*Towards scaling up classification based speech separation.*将时频单元级别的特征作为深度神经网络(Deep neural networks, DNN)的输入, 将学习到的特征和原始特征拼接在一起作为输入, 利用线性SVM进行二分类并得到IBM, 在一定程度上缓解了传统语音分离问题难以在大数据集上进行训练的问题。

2014年，Weninger等将信号估计(Signal approximation, SA)作为目标, 并将长短时记忆网络(Long-short term memory networks, LSTM)应用到语音分离问题中, 其实验结果显示LSTM比DNN在分离性能上更优。

2015年， Sprechmann等提出每层产生不同时间分辨率的特征图的Wavelet pyramid scattering transform网络, 并将学习到的多时间分辨率特征作为深度神经网络, 卷积神经网络的输入。 实验结果显示使用了多时间分辨率的小波特征作为输入的模型在语音分离各项指标SDR, SIR和SAR上表现远超使用单一时间分辨率的短时傅里叶变换表示作为输入的模型。

2015年，Zhang等利用集成学习的思想提出Multi-context networks, 对有不同尺度的上下文窗口时间长度的DNN的输出作平均(Multi-context averaging, MCA)或者堆栈(Multi-context stacking, MCS), 其中MCS模型的模块可以是基于时频掩蔽的模型, 基于频谱映射的模型和基于信号近似的模型; 实验结果显示Multi-context networks比单一固定上下文窗口时间长度的DNN在语音分离任务上效果更好.

2016年，Hershey等将深度神经网络模型和谱聚类结合起来, 提出深度聚类(Deep clustering, DC)算法来解决排列问题(Permutation problem)和输出维度不匹配问题(Output dimension mismatch problem).

2017年，Yu等提出帧级别的具有排列不变性的训练方法(Permutation invariant training, PIT)来解决排列问题，PIT方法的关键在于误差回传的时候计算预测输出序列与标注序列各种排列的均方差, 并选择最小均方差用于优化参数.

2017年，Chen等根据人类听觉认知研究中的感知磁效应(Perceptual magnet effect)提出深度吸引子网络(Deep attractor network, DANet), 从而做到端到端训练.

2018年，Yi Luo等为了解决语音分离的准确性，等待时间和计算成本等问题。并提升包括信号的相位和幅度的解耦，用于语音分离的频谱图表示的最优性，以及计算中的长延迟、谱图的不足，提出了一种用于时域语音分离的深度学习自动编码器框架（TasNet）。 TasNet使用Conv1D编码器来创建信号的表示，该信号被优化以提取单个扬声器。通过将加权函数（掩模）应用于编码器输出来实现扬声器提取。然后使用线性解码器将修改编码器表示反转为声音波形。使用由扩张的卷积组成的时间卷积网络找到掩模，其允许网络模拟语音信号的长期依赖性。

![](https://ws1.sinaimg.cn/large/006ocvumly1g2w7ivqd4rj31ca0kxgp4.jpg)

[**鸡尾酒会问题与相关听觉模型的研究现状与展望**](<http://html.rhhz.net/ZDHXBZWB/html/2019-2-234.htm>)

Multi-channel techniques in dealing with the cocktail party problem:

- Beamforming

  A beamformer is spatial filter that operates on the outputs of a microphone array and forms a beam (directivity) pattern to enhance the desired speech coming from one direction when suppressing interfering speech or noise from other directions.

- multi-channel blind source separation.

## 单通道监督学习语音分离的系统架构

**基于时频域的单通道监督学习语音分离的系统架构**

![](https://ws1.sinaimg.cn/large/006ocvumly1g2w8liudt3j314p0wwn2u.jpg)

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

#### 3.Training Criteria 分离目标

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

4. Ideal  Amplitude Mask, IAM

     Practically, we can use IAM defined as
     $$
     M_{s}^{\operatorname{IAM}}(t, f)=\frac{\left|\boldsymbol{X}_{s}(t, f)\right|}{|\boldsymbol{Y}(t, f)|}
     $$
     to reconstruct $\boldsymbol{X}_s$, because the magnitude spectra of the mixed speech $\boldsymbol{Y}$ is known during testing. IAMs have the constraint $0 \leq M_{s}^{\operatorname{IAM}}(t, f) \leq \infty$, although it is found empirically that the majority of the T-F units are in the range of $0 \leq M_{s}^{\mathrm{IAM}}(t, f) \leq 1$. Accordingly, softmax, sigmoid, and ReLU are possible activation functions for estimating IAMs in the implementation.

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

![nmf_1](https://img-blog.csdn.net/20160421172752611)

数学表达：

$$
V^{n\times m} \approx W^{n\times r} * H^{r\times m}
$$
其中，V是原矩阵，W即基矩阵，H为系数矩阵

**为什么分解的矩阵是非负的呢？**
1. 在音频处理的过程中，音频读入以矩阵形式存在，矩阵元素都是非负的，即 >=0。即在音频处理时，V本身就是非负的。那么在分解时，也必须保证W,H的元素非负。
2. 非负性会引入稀疏
3. 非负性会使计算过程进入部分解

**为什么NMF可以用于语音分离？**

由上述，NMF是一种压缩感知，会丢失信息。

我一直认为，NMF是降维方法，将原始较大的空间（维度），用另外一个小空间（维度）来表征。

那么，如果丢失的维度（空间）是噪声空间，是不是就可以认为起到语音分离的作用了？如果分解所得的基矩阵 W 是原始信号的基本特征，那么是不是就可以达到一种语音分离的效果。这其实和神经网络类似，在进行学习时，我们认为神经网络学习到的是task本身的潜在规律，再以此规律求解或回归或分类问题。



**R选择困难**

- 数据拟合：R越大那么对于数据拟合更好
- 模型复杂性：一个更小的R模型更简单（易于预测、少输入参数等）

**解不唯一**
对于V=WH;W>=0,H>=0，那么任意一个矩阵Q有 
$$
W Q>=0, Q^{-1} H>=0
$$
这就提供了一个可以替换的因子$V=W H=(W Q)\left(Q^{-1} H\right)$,特殊情况下，Q可以为任意非负广义置换矩阵。虽然解不唯一，但是也不用太担心，一般情况下解不唯一仅仅是基向量$W_k$的缩放和转置，意思就是换来换去还是它自己本身。



在语音处理中, 一种最广泛的做法是令 WW和 H 非负, 从而得到非负矩阵分解(Non-negative matrix factorization, NMF). NMF能够挖掘到语音或噪音中非负数据的基本谱模式.在NMF的基础上引入其他约束, 则可以得到NMF的不同变种.稀疏NMF对NMF加入稀疏约束, 来提高分解的鲁棒性.卷积NMF则将频谱 X 分解成矩阵卷积的形式来对时间依赖进行建模, 此时基矩阵随时间变化, 每个时刻的基矩阵编码了该时刻的频谱, 激活矩阵也对应变化.

![](https://ws1.sinaimg.cn/large/006ocvumly1g2w85d1ptwj311j0oy7tv.jpg)


[NMF详解（一）——什么是NMF](<https://zhuanlan.zhihu.com/p/55644116>)

[NMF 非负矩阵分解 -- 原理与应用](https://blog.csdn.net/qq_26225295/article/details/51211529)

[Music&Audio Computing Lab, citi.sinica Lecture 9 Source Separation](<http://mac.citi.sinica.edu.tw/~yang/teaching/lecture09_separation.pdf>)

## Performance Criteria 

**Source to Distortion Ratio, SDR**
$$
\mathrm{SDR} :=10 \log _{10} \frac{ \| s_{\text { target }}\left\|^{2}\right.}{ \| e_{\text { interf }}+e_{\text { noise }}+e_{\text { artif }}\left\|^{2}\right.}
$$
**Source to Interferences Ratio, SIR**
$$
\mathrm{SIR} :=10 \log _{10} \frac{ \| s_{\text { target }}\left\|^{2}\right.}{ \| e_{\text { interf }}\left\|^{2}\right.}
$$
**Source to Artifacts Ratio, SAR**
$$
\mathrm{SAR} :=10 \log _{10} \frac{ \| s_{\text { target }}+e_{\text { interf }}+e_{\text { noise }}\left\|^{2}\right.}{ \| e_{\text { artif }}\left\|^{2}\right.}
$$

其中：


$$
\begin{aligned} 
s_{\text { target }} & :=P_{s_{j}} \widehat{s}_{j} 
\\ e_{\text { interf }} & :=P_{\mathbf{s}} \widehat{s}_{j}-P_{s_{j}} \widehat{s}_{j} 
\\ e_{\text { noise }} & :=P_{\mathbf{s}, \mathbf{n}} \widehat{s}_{j}-P_{\mathbf{s}} \widehat{s}_{j} 
\\ e_{\text { artif }} & :=\widehat{s}_{j}-P_{\mathbf{s}, \mathbf{n}} \widehat{s}_{j} 
\\ P_{s_{j}} :=\Pi\left\{s_{j}\right\} 
\\ P_{\mathbf{s}} :=\Pi\left\{\left(s_{j^{\prime}}\right)_{1 \leq j^{\prime} \leq n}\right\} 
\\ P_{\mathbf{s}, \mathbf{n}} :=\Pi\left\{\left(s_{j^{\prime}}\right)_{1 \leq j^{\prime} \leq n},\left(n_{i}\right)_{1 \leq i \leq m}\right\}
\end{aligned}
$$

[Performance measurement in blind audio source separation](https://hal.inria.fr/inria-00544230/document)

**Short-time Objective Intelligibility, STOI**



**Perceptual Evaluation of Speech Quality, PESQ**



Word Error Rate, WER



Equal Error Rate, EER

## Datasets

**WSJ0(Wall Street Journal)** 

**TIMIT** contains broadband recordings of 630 speakers of eight major dialects of American English, each reading ten phonetically rich sentences. TIMIT corpus includes time-aligned orthographic, phonetic and word transcriptions as well as a 16-bit, 16kHz speech waveform file for each utterance.

VCTK

[LibriSpeech](<http://www.openslr.org/12/>)

[AVSpeech](<https://looking-to-listen.github.io/avspeech/download.html>)

[NSynth: Neural Audio Synthesis](<https://magenta.tensorflow.org/nsynth>)

[VoxCeleb1/VoxCeleb2](<http://www.robots.ox.ac.uk/~vgg/data/voxceleb/>)

[CSTR VCTK Corpus ](<https://homepages.inf.ed.ac.uk/jyamagis/page3/page58/page58.html>)

MUSDB18 <https://sigsep.github.io/datasets/musdb.html>

## Competition

**CHiME Speech Separation and Recognition Challenge**



## SOTA

**Deep Clustering(DPCL++)**

paper : <https://arxiv.org/pdf/1508.04306.pdf>

Different from the supervised regression framework, they cast the separation problem as a segmentation problem. Specifically, they assumed that each T-F bin (t,f) of the mixed speech belongs to only one speaker. If we assign the same unique color to the bins belonging to the same speaker, the spectrogram is segmented into clusters, one for each speaker. The key observation in this framework is that during training we need only to know which bins belong to the same speaker(or cluster), and which is unambiguous, thus avoiding the label permutation problem.

Because clustering is defined based on some distance between bis, Hershey et al.(2016) proposed to define the distance in the embedding space of the bins that the system can learn from the training data. If two bins belong to the same speaker, their distance in the embedding is small, and if two bins belong to different speakers, their distance in the embedding space is large.

Precisely, given a raw input signal $\mathcal{y}$, its feature vector is defined as

$$
 \boldsymbol{Y}_{i}=g_{i}(\boldsymbol{y})(i \in\{1,2, \cdots, N\})
$$

, where $i$ is the T-F index $(t,f)$ in the case of audio signals. A deep neural network is used to transform input signal $\mathcal{x}$ into D-dimensional embeddings 

$$
\boldsymbol{V}=f_{\theta}(\boldsymbol{Y}) \in \mathbb{R}^{N \cdot D}
$$

,where each row vector $v_i$ has unit norm.

Performing clustering in the embedding space will likely lead to a partition of {1,2,...,N}, which is close to the target. 

Embeddings V is considered to implicitly represent an $N \times N$ estimated affinity matrix $V V^T$. 

The target partition is represented by indicator $E={e_{i,s}}$, mapping each element i to each of S clusters; thus, $e_{i,s}=1$ if element i is in cluster c. 

In this case, $EE^T$ is considered as binary affinity matrix that represents the cluster assignments in a permutation-independent way : 
$$
(EE^T)_{i,j}=\left\{\begin{array}{ll}{1,} & {\text { if }  i,j \in cluster} \\ {0,} & {\text { otherwise }}\end{array}\right.
$$
and $(EP)(EP)^T = EE^T$ for any permutation matrix

Thus, we can learn affinity matrix $VV^T$, as a function of inputs X, to match affinities $EE^T$, by minimizing the training cost function, with respect to to $V=f_{\theta}(\boldsymbol{Y}) $
$$
C_{E}(\boldsymbol{V})=\left\|\boldsymbol{V} \boldsymbol{V}^{\mathrm{T}}-\boldsymbol{E} \boldsymbol{E}^{\mathrm{T}}\right\|_{\mathrm{F}}^{2}=\sum_{i, j}\left(\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle-\left\langle\boldsymbol{e}_{i}, \boldsymbol{e}_{j}\right\rangle\right)^{2}=\sum_{i, j \cdot e_{i}=e_{j}}\left(\left|v_{i}-v_{j}\right|^{2}-1\right)+\sum_{i, j}\left\langle v_{i}, v_{j}\right\rangle^{2}
$$
summed over training examples, where $\|\cdot\|_{\mathrm{F}}^{2}$ is the squared Frobenius norm.



**Permutation Invariant Training(PIT)**

**Deep Attractor Network(DANet)**

![](https://ws1.sinaimg.cn/large/006ocvumgy1g34k6q1abyj30j10ipwfc.jpg)

Given the mixture signal with S sources, a K-dimensional embedding $\boldsymbol{V} \in \mathbb{R}^{F \cdot T \cdot K}$ of the mixed acoustic signal $\boldsymbol{Y}=[F \cdot T]$ , is learned by the neural network. During training, attractors $\boldsymbol{A} \in \mathbb{R}^{S \cdot K}$ are learned as
$$
A_{s, k}=\frac{\sum_{f, t} V_{k, f t} \cdot E_{s, f t}}{\sum_{f, t} E_{s, f t}}
$$

in the embedding space, where $\boldsymbol{E} \in \mathbb{R}^{F \cdot T \cdot S}$ is the dominant source membership function for each T-F bin. A mask M is then estimated in the embedding space as 
$$
M_{f, t, s}=\operatorname{Softmax}\left(\sum_{K} A_{s, k} \cdot V_{f t, k}\right)
$$
Finally, the neural network is trained to minimize
$$
\mathcal{L}=\sum_{f, t, s}\left\|\boldsymbol{X}_{f, t, s}-\boldsymbol{Y}_{f, t} \cdot M_{f, t, s}\right\|_{2}^{2}
$$
where X is the clean spectrogram of S sources.

**Conv-TasNet**

## Still need to solve

- 声源数量已知
- 置换问题
- 远场效果差



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

[wikipedia-短时距傅里叶变换]([https://zh.wikipedia.org/wiki/%E7%9F%AD%E6%99%82%E8%B7%9D%E5%82%85%E7%AB%8B%E8%91%89%E8%AE%8A%E6%8F%9B](https://zh.wikipedia.org/wiki/短時距傅立葉變換))

- **Speak Dependent/Speaker Independent**

Speech recognition is classified into two categories, speaker dependent and speaker independent.

**Speaker dependent** systems are trained by the individual who will be using the system. These systems are capable of achieving a high command count and better than 95% accuracy for word recognition. The drawback to this approach is that the system only responds accurately only to the individual who trained the system. This is the most common approach employed in software for personal computers.

**Speaker independent** is a system trained respond to a word regardless of who speakers. Therefore the system must respond to a large variety of speech patterns, inflections(音调变化) and enunciation's(清晰的发音) of the target word. The command word count is usually lower than the speaker dependent however high accuracy can still be maintain within processing limits. Industrial requirements more often need speaker independent voice systems, such as the AT&T system used in the telephone systems.



