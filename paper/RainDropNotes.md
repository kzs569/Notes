雨滴去除(RainDrop Removal)
======================

##


## 损失函数

- SSIM

- [Image Quality Assessment: From Error Visibility to Structural Similarity](http://www.cns.nyu.edu/pub/lcv/wang03-preprint.pdf)

当对一幅图片进行有损压缩，或者一幅图片有了噪声、畸变（distortion）等。我们人可以分辨出这两幅图大概率还是同一幅图，但如何有效地衡量他们的相似性呢？
为了抵消普通的L2距离（Mean Square Error,MSE）无法衡量图片的结构相似性的缺陷，这篇文章提出了SSIM这种structure similarity的方法来做最后变化后的图片与变化前的结构相似性。

(各类相机的宗旨也是提供给更接近人眼感知系统(human vision system,HVS)的感知能力)
人眼对光照不敏感，但对局部（图像不同部分）光照的变化敏感。对灰度不敏感但对各部分灰度的相对变化程度敏感（对比度变化）。以及对整个很大局部的结构敏感。基于以上认知，作者最后提出的：

<img src="https://latex.codecogs.com/gif.latex?SSIM(x,y)=\frac{(2\mu_x\mu_y&plus;C_1)(2\sigma_{xy}&plus;C_2)}{(\mu^2_x&plus;\mu^2_y&plus;C_1)(\sigma^2_x&plus;\sigma^2_y&plus;C_2)}" title="SSIM(x,y)=\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu^2_x+\mu^2_y+C_1)(\sigma^2_x+\sigma^2_y+C_2)}" />

对于两个DxD的图像块，他们的SSIM始终小于1，1表示完全相似。

其中
<img src="https://latex.codecogs.com/gif.latex?\mu_x,\mu_y" title="\mu_x,\mu_y" />
是图像块所有像素的平均值，
<img src="https://latex.codecogs.com/gif.latex?\sigma_x,\sigma_y" title="\sigma_x,\sigma_y" />
是图像像素值的方差

SSIM实际上三个比较部分的乘积：

*图像照明度比较部分：*

<img src="https://latex.codecogs.com/gif.latex?l(x,y)&space;=&space;\frac{2\mu_x\mu_y&plus;C_1}{\mu^2_x&plus;\mu^2_y&plus;C_1}" title="l(x,y) = \frac{2\mu_x\mu_y+C_1}{\mu^2_x+\mu^2_y+C_1}" />

*图像对比度比较部分：*

<img src="https://latex.codecogs.com/gif.latex?c(x,y)&space;=&space;\frac{2\sigma_{xy}&plus;C_2}{\sigma^2_x&plus;\sigma^2_y&plus;C_2}" title="c(x,y) = \frac{2\sigma_{xy}+C_2}{\sigma^2_x+\sigma^2_y+C_2}" />

*图像结构对比部分：*

<img src="https://latex.codecogs.com/gif.latex?s(x,y)&space;=&space;\frac{\sigma_{xy}&plus;C_3}{\sigma_x\sigma_y&plus;C_3}" title="s(x,y) = \frac{\sigma_{xy}+C_3}{\sigma_x\sigma_y+C_3}" />

其中

<img src="https://latex.codecogs.com/gif.latex?\sigma_{xy}=\frac{1}{N-1}\sum^N_{i=1}(x_i-\mu_x)(y_i-\mu_y)" title="\sigma_{xy}=\frac{1}{N-1}\sum^N_{i=1}(x_i-\mu_x)(y_i-\mu_y)" />

SSIM相当于将数据进行归一化后，分别计算图像块照明度（图像块的均值），对比度（图像块的方差）和归一化后的像素向量这三者相似度，并将三者相乘。
SSIM计算某个window的相似度（比如11X11),然后将所有window的相似度做一个平均（得到MSSIM）作为整张图片的相速度。

照明度部分对各个部分明度差异更敏感，对比度部分对低对比度部分更加敏感。
作者在计算每个图像块之前，会先对要计算的window进行一个高斯模糊(即点乘上一个与window同等大小的高斯分布的权重mask)

- [Loss Functions for Neural Networks for Image Processing ](https://arxiv.org/abs/1511.08861)

之前会用L2,Pek signal-to-Noise Ratio , PSNR，等作为损失函数.
L1,L2,SSIM,MS-SSIM,MS-SSIM+L1
目前神经网络已经大量用于降噪，降模糊，提升分辨率，去马赛克等工作中。但这些工作中大家往往执着于调整网络结构，而非代价函数。

作者发现即使在L2表现良好的情况下，L1,SSIM等能获得更好的表现。而且令人惊讶的是L1表现与SSIM差别不大。因此作者提出将“combines the advantages of l1 and MS-SSIM ”
即最终：

<img src="https://latex.codecogs.com/gif.latex?L^{mix}=\alpha&space;L^{MS-SSIM}&space;&plus;&space;(1-\alpha)G_{\sigma^M_G}L^{l_1}" title="L^{mix}=\alpha L^{MS-SSIM} + (1-\alpha)G_{\sigma^M_G}L^{l_1}" />

顺便介绍：MS-SSIM是图像进行缩放之后形成金字塔的SSIM

<img src="https://latex.codecogs.com/gif.latex?MS-SSIM(p)=l^{\alpha}_{M}(p)\prod^M_{j=1}cs^{\beta_j}_j(p)" title="MS-SSIM(p)=l^{\alpha}_{M}(p)\prod^M_{j=1}cs^{\beta_j}_j(p)" />

其中\alpha=0.84

实验阶段，作者分别作了打马赛克和去马赛克、提升分辨率、jpeg压缩后的图片失真度检测四个人物分别测试这种混合的代价函数的，结果优于L2.


