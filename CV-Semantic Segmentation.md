CV-Semantic Segmentation

1.Fully Convolutional Networks（2014 UCB）

Github : [Fully Convolutional Networks for Semantic Segmentation](<https://github.com/shelhamer/fcn.berkeleyvision.org>)

Papers : [Fully Convolutional Networks for Semantic Segmentation](<https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf>)

Main Contributions:

- 为语义分割引入了End2End的全卷积网络
- 利用ImageNet的预训练网络做语义分割
- 使用反卷积层（取代线性插值）进行上采样
- 引入少量跳跃连接改善上采样粗糙的像素定位

2.SegNet (2015,Cambridge)

Github : [Caffe SegNet](https://github.com/alexgkendall/caffe-segnet)
Papers : [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://arxiv.org/pdf/1511.00561.pdf)

网络结构示意图：

![](http://ww1.sinaimg.cn/large/006ocvumgy1g23k09oehij32fw0wg4qp.jpg)

Main Contributions:

- 使用了编码-解码结构
- 将池化结果应用到译码的过程，使用的是Pooling indices(记录位置信息)而不是简单地复制特征
- 没有跳跃连接，更节省内存

3.U-Net(2015,)

Github : [Keras U-Net](https://github.com/zhixuhao/unet)
Papers : [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597.pdf)

![u-net-architecture](https://github.com/zhixuhao/unet/raw/master/img/u-net-architecture.png)

Main Contributions:

- 编解码结构Baseline

4.Dilated Convolutions(2015,Princeton&Intel)

Papers : [Multi-Scale Context Aggregation by Dilated Convolutions](https://arxiv.org/abs/1511.07122)

![dilated-convs](https://pic2.zhimg.com/50/v2-4959201e816888c6648f2e78cccfd253_hd.gif)

主要贡献：

- 通过带孔卷积提取和聚合多尺度的信息。

- 提出context module来聚合多尺度的信息。

5.DeepLab(v1&v2)

Github : [DeepLab: Deep Labelling for Semantic Image Segmentation](<https://github.com/tensorflow/models/tree/master/research/deeplab>)

Papers :

DeepLab v1(ICLR2015) :  [SEMANTIC IMAGE SEGMENTATION WITH DEEP CONVOLUTIONAL NETS AND FULLY CONNECTED CRFS](<https://arxiv.org/pdf/1412.7062v3.pdf>)

- 速度：带`atrous`算法的DCNN可以保持8FPS的速度，全连接CRF平均推断需要0.5s
- 准确：在PASCAL语义分割挑战中获得了第二的成绩
- 简单：DeepLab是由两个非常成熟的模块(DCNN和CRFs)级联而成

DeepLab v2(TPAMI2017) : [DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs](<https://arxiv.org/pdf/1606.00915.pdf>)

- 首先，**强调使用空洞卷积，作为密集预测任务的强大工具**。空洞卷积能够明确地控制DCNN内计算特征响应的分辨率，即可以有效的扩大感受野，在不增加参数量和计算量的同时获取更多的上下文。
- 其次，**我们提出了空洞空间卷积池化金字塔(atrous spatial pyramid pooling (ASPP))，以多尺度的信息得到更强健的分割结果**。ASPP并行的采用多个采样率的空洞卷积层来探测，以多个比例捕捉对象以及图像上下文。
- 最后，**通过组合DCNN和概率图模型，改进分割边界结果**。在DCNN中最大池化和下采样组合实现可平移不变性，但这对精度是有影响的。通过将最终的DCNN层响应与全连接的CRF结合来克服这个问题。

6.RefineNet(2016,)

Papers : [RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation](<https://arxiv.org/pdf/1611.06612.pdf>)

Githubs : [Multipath RefineNet](<https://github.com/guosheng/refinenet>)

由于带孔卷积需要大量的高分辨率特征图，对计算和内存的消耗很大，因此无法利用高分辨率的精细预测。

该文章采用编码解码结构。编码器是ResNet-101，解码器是RefineNet模块，用于连接编码器中高分辨率特征和先前RefineNet中低分辨率的特征。

每一个RefineNet都有两个组件，一个组件通过对低分辨率特征的上采样操作融合不同的分辨率特征，另一个组件利用窗口为5*5且步长为1的池化层来获取背景信息。这些组件都遵循恒等映射（identity mapping）思想，采用残差连接设计。

主要贡献：

- 精心设计了译码模块。

- 所有模块遵循残差连接设计。

7.PSPNet(2016,CVPR2017)

Papers : [Pyramid Scene Parsing Network](<https://arxiv.org/pdf/1612.01105.pdf>)

Github : [Pyramid Scene Parsing Network](<https://github.com/hszhao/PSPNet>)

金字塔池化模块通过使用大窗口的池化层来提高感受野。使用带孔卷积来修改ResNet网络，并增加了金字塔池化模块。金字塔池化模块对ResNet输出的特征进行不同规模的池化操作，并作上采样后，拼接起来，最后得到结果。

金字塔池化模块简单来说是将DeepLab（不完全一样）ASPP之前的feature map池化了四种尺度之后，将五种feature map拼接到一起，经过卷积，最后进行预测的过程。

在ResNet的第四个阶段之后（即输入到金字塔池化模块的阶段），在主分支损失之外增加辅助损失（其他论文称为中间监督）。

主要贡献：

- 提出了金字塔池化模块来聚合图片上下文信息。

- 使用附加的辅助损失函数。



8.Large Kernel Matters(2017,face++)

Papers : [Large Kernel Matters Improve Semantic Segmentation by Global Convolutional Network](<https://arxiv.org/pdf/1703.02719.pdf>)

Github : [Pytorch for Semantic Segmentation](<https://github.com/ycszen/pytorch-segmentation>)





9.DeepLab v3 (2017,)

Github : [DeepLab: Deep Labelling for Semantic Image Segmentation](https://github.com/tensorflow/models/tree/master/research/deeplab)

[DeepLab_V3 Image Semantic Segmentation Network](https://github.com/sthalles/deeplab_v3)

Papers : [Rethinking Atrous Convolution for Semantic Image Segmentation](<https://arxiv.org/pdf/1706.05587.pdf>)

- 本文重新讨论了空洞卷积的使用，这让我们在级联模块和空间金字塔池化的框架下，能够获取更大的感受野从而获取多尺度信息。
- 改进了ASPP模块：由不同采样率的空洞卷积和BN层组成，我们尝试以级联或并行的方式布局模块。
- 讨论了一个重要问题：使用大采样率的3×33×3的空洞卷积，因为图像边界响应无法捕捉远距离信息，会退化为1×1的卷积, 我们建议将图像级特征融合到ASPP模块中。
- 阐述了训练细节并分享了训练经验，论文提出的”DeepLabv3”改进了以前的工作，获得了很好的结果

10.PixelNet

**PixelNet: Representation of the pixels, by the pixels, and for the pixels-2017** [[Project\]](http://www.cs.cmu.edu/~aayushb/pixelNet/) [[Code-Caffe\]](https://github.com/aayushbansal/PixelNet) [[Paper\]](https://arxiv.org/abs/1702.06506)

11.DeepLab v3+

DeepLabV3+:Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation – 2018 – Google [[Paper\]](https://arxiv.org/pdf/1802.02611.pdf) [[Code-Tensorflow\]](https://github.com/tensorflow/models/tree/master/research/deeplab) [[Code-Karas\]](https://github.com/bonlime/keras-deeplab-v3-plus)

