ISTA-Net: Interpretable Optimization-Inspired Deep Network for Image Compressive Sensing 
=============================================================

## Background
- Compressed sensing 压缩感知
    压缩感知是一个针对信号采样的技术，它通过一些手段，实现了“压缩的采样”，准确说是在采样过程中完成了数据压缩的过程。
    
    通常将模拟信号转换为计算机能处理的数字信号，必须经过采样过程。奈奎斯特Nyquist采样定理，只要采样频率大于被采样信号最高频率的两倍，就能完全恢复。
    
    两倍的原因，主要是因为在信号处理过程中，时域以<img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" />
    为间隔进行采样，频域以<img src="https://latex.codecogs.com/gif.latex?\frac{1}{\tau&space;}" title="\frac{1}{\tau }" />
    为周期发生周期延拓。那么如果采样频率低于两倍的信号最高频率，信号在频域频谱搬移后就会发生混叠。
    
    但是在2004年Candes在陶哲轩和Donoho教授的协助下，提出了压缩感知理论，该理论认为：如果信号是稀疏的，那么它可以由远低于采样定理要求的采样点重建恢复
    
    即由 等间距采样→不等间距采样or随机采样
    
    最终的结果是随机的亚采样给了我们恢复信号的可能，下图一个典型的亚采样的采样和恢复过程
    
    ![](http://ww1.sinaimg.cn/large/006ocvumgy1g0iliu19thj30k00dzwin.jpg)
    
    ![](http://ww1.sinaimg.cn/large/006ocvumgy1g0iljhulb4j30k00e040b.jpg)
    
    基于匹配追踪的典型恢复算法
    
    1. 由于原信号的频率非零值在亚采样后的频域中依然保留较大的值，其中较大的两个可以通过设置阈值，检测出来（过程（a））
    2. 然后假设信号只存在这两个非零值（图b），则可计算出由这两个非零值引起的干扰（图c）
    3. 用a-c即可得到只有蓝色非零值和由它导致的干扰值（图d），再设置阈值检测，检出蓝色非零值，得到最终复原频域
    4. 如果原信号频域中有更多的非零值，则可通过迭代将其一一解出。
    
    核心思想：以比奈奎斯特采样频率要求的采样密度更稀疏的密度对信号进行随机亚采样，由于频谱是均匀泄露的，而不是整体延拓的，因此可以通过特别的追踪方法将原信号恢复。
    
    前提条件：1.信号在频域稀疏（稀疏性）2.随机亚采样（不相关性）
    
    - 稀疏性
    
        信号需要在某一个变换域具有稀疏性，如果信号在某个域中非零点远远小于信号总点数，则信号在改域中是稀疏的。在压缩感知中，只要信号在某一个变换域满足近似稀疏特性，称为稀疏域，重建将在稀疏域进行。
        将信号转换到稀疏域的变换我们称为<img src="https://latex.codecogs.com/gif.latex?\Psi" title="\Psi" />，<img src="https://latex.codecogs.com/gif.latex?\Psi" title="\Psi" />可以是频域、小波变换、离散余弦变换等。
        
        <img src="https://latex.codecogs.com/gif.latex?x'=&space;\Psi&space;x" title="x'= \Psi x" />
        
    - 图像压缩与压缩感知的不同点
    
    ![](http://ww1.sinaimg.cn/large/006ocvumgy1g0ilxxtui2j30k00dsn07.jpg)
    
    - 压缩感知的数学表达
    
    ![](http://ww1.sinaimg.cn/large/006ocvumgy1g0ilz03cdfj30k00e7djf.jpg)
    
    如图，x是为长度N的一维信号，也就是原信号，稀疏度为k。此刻它是未知的。

    Φ为观测矩阵，对应着亚采样这一过程。它将高维信号x投影到低维空间，是已知的。
    
    y=Φx为长度M的一维测量值，也就是亚采样后的结果。显然它也是已知的。
    
    因此，压缩感知问题就是在已知测量值y和测量矩阵Φ的基础上，求解欠定方程组y=Φx得到原信号x。
    
    然而，一般的自然信号x本身并不是稀疏的，需要在某种稀疏基上进行稀疏表示。令x=Ψs，Ψ为稀疏基矩阵，s为稀疏系数。
    
    于是最终方程就变成了：y=ΦΨs。已知y、Φ、Ψ，求解s。
        
    
## Abstract & Introduction

## Related Work
主要分为两类：基于优化的CS方法，基于网络的CS方法
1. 基于优化的CS方法

    对于所给的线性观测y，传统的CS方法通过求解以下凸优化问题来重建原始图片x：
    
    <img src="https://latex.codecogs.com/gif.latex?\underset{x}{min}\frac{1}{2}||\Phi&space;x-y||^2_2&plus;\lambda||\Psi&space;x||_1" title="\underset{x}{min}\frac{1}{2}||\Phi x-y||^2_2+\lambda||\Psi x||_1" />
        
2. 基于网络的CS方法

    
        
    
    
## 
    
    
    
    
    
    
    
# Inference
- [形象易懂讲解算法II——压缩感知](https://zhuanlan.zhihu.com/p/22445302)

- [ISTA算法求解L1正则化问题](https://blog.csdn.net/qq_23968185/article/details/53414225)