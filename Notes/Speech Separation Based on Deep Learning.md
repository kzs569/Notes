# Speech Separation Based on Deep Learning

- Speech + noise:speech enhancement

- Speech + speech:speaker separation

- Reflection:speech de-reverberation

## Classifiers and learning machines

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da8517aea3e.jpg?imageMogr2/format/jpg/quality/90)

## Training targets

一类是基于Mask的方法：

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da852716db1.jpg?imageMogr2/format/jpg/quality/90)

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da8532581fd.jpg?imageMogr2/format/jpg/quality/90)

基于Mask的方法又可以分为几类

- “理想二值掩蔽”（Ideal Binary Mask）中的分离任务就成为了一个二分类问题。这类方法根据听觉感知特性，把音频信号分成不同的子带，根据每个时频单元上的信噪比，把对应的时频单元的能量设为0（噪音占主导的情况下）或者保持原样（目标语音占主导的情况下）。

- 第二类基于Mask的方法是IRM（Ideal Ratio Mask），它同样对每个时频单元进行计算，但不同于IBM的“非零即一”，IRM中会计算语音信号和噪音之间的能量比，得到介于0到1之间的一个数，然后据此改变时频单元的能量大小。IRM是对IBM的演进，反映了各个时频单元上对噪声的抑制程度，可以进一步提高分离后语音的质量和可懂度。

- TBM与IRM类似，但不是对每个时频单元计算其中语音和噪声的信噪比，而是计算其中语音和一个固定噪声的信噪比

- SMM是IRM在幅度上的一种形式

- PSM中加入了干净语音和带噪语音中的相位差信息，有更高的自由度

虽然基于Mask的方法有这么多，但最常用的还是开头的IBM和IRM两种

一类是基于频谱映射的方法：

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da8539e4adf.jpg?imageMogr2/format/jpg/quality/90)

如果使用频谱映射，分离问题就成为了一个回归问题。

频谱映射可以使用幅度谱、功率谱、梅尔谱以及Gammatone功率谱。Gammatone是模拟人耳耳蜗滤波后的特征。为了压缩参数的动态范围以及考虑人耳的听觉效应，通常还会加上对数操作，比如对数功率谱。

基于频谱映射的方法，是让模型通过有监督学习，自己学习有干扰的频谱到无干扰的频谱（干净语音）之间的映射关系；模型可以是DNN,CNN,LSTM,GAN

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da854558f19.jpg?imageMogr2/format/jpg/quality/90)

这一页是使用相同的DNN模型、相同的输入特征、不同的训练目标得到的结果。

左边的STOI指语音的可懂度，得分在0到1之间，越高越好；右边的PESQ是语音的听觉质量、听感，范围为-0.5到4.5，也是越高越好。

基于Mask的方法STOI表现较好，原因是有共振峰的能量得到了较好的保留，而相邻共振峰之间波谷处的声音虽然失真较大，但人耳对这类失真并不敏感；两类方法在PESQ中表现相当。

## Training data

针对语音分离中的语音增强任务，首先可以通过人为加噪的方法生成带噪音和干净语音对，分别作为输入和输出（有标注数据），对有监督学习模型进行训练。加入的噪声可以是各种收集到的真实世界中的噪声。

不过收集噪声需要样本，而且人工能收购到的噪音总是有限的，最好有能够有一套完备、合理的方案，用仿真的方式生成任意需要的噪声。在今年的MLSP会议上，搜狗语音团队就发表了一项关于噪声基的工作，通过构造一个噪声基模型，在不使用任何真实噪音数据的情况下，生成带噪语音对语音增强模型进行训练，达到了与50种真实噪音的情况下相当的性能。

![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da85751912d.jpg?imageMogr2/format/jpg/quality/90)

如果将这50种真实噪声和噪声基产生的数据混合在一起，性能可以比单独使用真实噪音的情况得到进一步提高。这也说明噪声基生成的噪声和真实噪声数据之间有着互补性，在实际应用中，也可以解开一些真实噪声数据不足带来的限制。

- 单通道语音分离算法
![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da85917c888.jpg?imageMogr2/format/jpg/quality/90)
对于语音增强，基于Mask的方法首先进行耳蜗滤波，然后特征提取、时频单元分类、二值掩蔽、后处理，就可以得到增强后的语音了。
![](https://static.leiphone.com/uploads/new/article/740_740/201710/59da85c5d6f8e.jpg?imageMogr2/format/jpg/quality/90)
语音增强的另一类基于频谱映射的方法中，先提取特征，用深度网络学习带噪语音和干净语音的对数功率谱之间映射关系，再加上波形重建，就可以得到增强后的语音。

基于有监督学习的算法都存在泛化性问题，语音增强也不例外。针对噪音类型、信噪比和说话人的泛化性都还有提升的空间。

## Monaural separation algorithms



  

时频分解技术：短时傅里叶变换(Short-time Fourier transform,STFT)和Gammatone听觉滤波模型