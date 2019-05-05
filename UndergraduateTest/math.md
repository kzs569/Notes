## 数列&极限
1. (张宇八套卷(一).10)
<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}\frac{1}{n}(n!)^{\frac{1}{n}}=" title="\lim_{n\rightarrow\infty}\frac{1}{n}(n!)^{\frac{1}{n}}=" />

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{n}(n!)^{\frac{1}{n}}=&space;(\frac{n!}{n^n})^{\frac{1}{n}}=exp\{\frac{1}{n}\sum^n_{i=1}ln\frac{i}{n}\}" title="\frac{1}{n}(n!)^{\frac{1}{n}}= (\frac{n!}{n^n})^{\frac{1}{n}}=exp\{\frac{1}{n}\sum^n_{i=1}ln\frac{i}{n}\}" />

<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}\frac{1}{n}(n!)^{\frac{1}{n}}=exp\{\lim_{n\rightarrow\infty}\frac{1}{n}\sum^n_{i=1}ln\frac{i}{n}\}=e^{\int^1_0lnxdx}=e^{-1}" title="\lim_{n\rightarrow\infty}\frac{1}{n}(n!)^{\frac{1}{n}}=exp\{\lim_{n\rightarrow\infty}\frac{1}{n}\sum^n_{i=1}ln\frac{i}{n}\}=e^{\int^1_0lnxdx}=e^{-1}" />

2. (张宇八套卷(三).01)设g(x)在x=0的某邻域内连续且
<img src="https://latex.codecogs.com/gif.latex?\lim_{x\rightarrow0}\frac{g(x)}{x}=\frac{1}{4}" title="\lim_{x\rightarrow0}\frac{g(x)}{x}=\frac{1}{4}" />
.又设f(x)在该邻域内存在二阶导数且满足
<img src="https://latex.codecogs.com/gif.latex?x^2f''(x)-[f'(x)]^2=xg(x)" title="x^2f''(x)-[f'(x)]^2=xg(x)" />
。则

A.f(0)是f(x)的极大值

**B.f(0)是f(x)的极小值**

C.f(0)不是f(x)的极值

D.f(0)是否为f(x)的极值要由具体的g(x)决定

由题意易知，
<img src="https://latex.codecogs.com/gif.latex?g(0)=\lim_{x\rightarrow0}g(x)=\lim_{x\rightarrow0}x\cdot\frac{g(x)}{x}=0" title="g(0)=\lim_{x\rightarrow0}g(x)=\lim_{x\rightarrow0}x\cdot\frac{g(x)}{x}=0" />

<img src="https://latex.codecogs.com/gif.latex?f'(x)^2|_{x=0}=x^2f''(x)-xg(x)=0" title="f'(x)^2|_{x=0}=x^2f''(x)-xg(x)=0" />

从而得到，
<img src="https://latex.codecogs.com/gif.latex?f''(0)=\lim_{x\rightarrow0}\frac{f'(x)-f'(0)}{x-0}=\lim_{x\rightarrow0}\frac{f'(x)}{x}" title="f''(0)=\lim_{x\rightarrow0}\frac{f'(x)-f'(0)}{x-0}=\lim_{x\rightarrow0}\frac{f'(x)}{x}" />
然后对所给方程左右两边同除x^2,并求极限
<img src="https://latex.codecogs.com/gif.latex?\lim_{x\rightarrow0}f''(x)-\lim_{x\rightarrow0}\frac{f'(x)}{x}=-\lim_{x\rightarrow0}f''(x)=\lim_{x\rightarrow0}\frac{g(x)}{x}=\frac{1}{4}" title="\lim_{x\rightarrow0}f''(x)-\lim_{x\rightarrow0}\frac{f'(x)}{x}=-\lim_{x\rightarrow0}f''(x)=\lim_{x\rightarrow0}\frac{g(x)}{x}=\frac{1}{4}" />

所以，<img src="https://latex.codecogs.com/gif.latex?\lim_{x\rightarrow0}f''(x)=-\frac{1}{4}" title="\lim_{x\rightarrow0}f''(x)=-\frac{1}{4}" />
根据函数的保号性f'(x)在x=0的一个邻域内单调递减，又f'(0)=0,所以f(0)是f(x)的极小值。

3.(张宇八套卷(二).12)设<img src="https://latex.codecogs.com/gif.latex?u_n=\sum^n_{k=1}\frac{k}{(n&plus;k)(n&plus;k&plus;1)},\lim_{n\rightarrow\infty}u_n=" title="u_n=\sum^n_{k=1}\frac{k}{(n+k)(n+k+1)},\lim_{n\rightarrow\infty}u_n=" />

夹逼定理：

<img src="https://latex.codecogs.com/gif.latex?\frac{k}{(n&plus;k)(n&plus;k&plus;1)}&space;\leq&space;\frac{1}{n}\frac{\frac{k}{n}}{(1&plus;\frac{k}{n})^2}" title="\frac{k}{(n+k)(n+k+1)} \leq \frac{1}{n}\frac{\frac{k}{n}}{(1+\frac{k}{n})^2}" />

<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}\frac{1}{n}\sum^n_{k=1}\frac{\frac{k}{n}}{(1&plus;\frac{k}{n})^2}=\int^1_0\frac{x}{(1&plus;x)^2}dx=ln2&plus;1/2" title="\lim_{n\rightarrow\infty}\frac{1}{n}\sum^n_{k=1}\frac{\frac{k}{n}}{(1+\frac{k}{n})^2}=\int^1_0\frac{x}{(1+x)^2}dx=ln2+1/2" />

<img src="https://latex.codecogs.com/gif.latex?\frac{k}{(n&plus;k)(n&plus;k&plus;1)}=\frac{1}{n&plus;1}\frac{\frac{k}{n}}{(1&plus;\frac{k}{n})(1&plus;\frac{k}{n&plus;1})}\geq&space;\frac{n}{n&plus;1}[\frac{1}{n}\frac{\frac{k}{n}}{(1&plus;\frac{k}{n})^2}]" title="\frac{k}{(n+k)(n+k+1)}=\frac{1}{n+1}\frac{\frac{k}{n}}{(1+\frac{k}{n})(1+\frac{k}{n+1})}\geq \frac{n}{n+1}[\frac{1}{n}\frac{\frac{k}{n}}{(1+\frac{k}{n})^2}]" />

<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}&space;\frac{n}{n&plus;1}[\frac{1}{n}\sum^n_{k=1}\frac{\frac{k}{n}}{(1&plus;\frac{k}{n})^2}]=\lim_{n\rightarrow\infty}\frac{n}{n&plus;1}\int^1_0\frac{x}{(1&plus;x)^2}dx=ln2&plus;1/2" title="\lim_{n\rightarrow\infty} \frac{n}{n+1}[\frac{1}{n}\sum^n_{k=1}\frac{\frac{k}{n}}{(1+\frac{k}{n})^2}]=\lim_{n\rightarrow\infty}\frac{n}{n+1}\int^1_0\frac{x}{(1+x)^2}dx=ln2+1/2" />

## 反常积分
1. (2016.1)若反常积分
<a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_{0}\frac{1}{x^a(1&plus;x)^b}dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_{0}\frac{1}{x^a(1&plus;x)^b}dx" title="\int^{+\infty}_{0}\frac{1}{x^a(1+x)^b}dx" /></a>
收敛，则

    A.a<1且b>1

    B.a>1且b>1

    **C.a<1且a+b>1**

    D.a>1且a+b>1

    两个重要结论：无穷区间的反常积分
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_{1}\frac{dx}{x^p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_{1}\frac{dx}{x^p}" title="\int^{+\infty}_{1}\frac{dx}{x^p}" /></a>
    ：在p>1时收敛，在p<=1时发散；无界函数的反常积分
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{1}_{0}\frac{dx}{x^p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{1}_{0}\frac{dx}{x^p}" title="\int^{1}_{0}\frac{dx}{x^p}" /></a>
    （奇点x=0)：在p<=1时收敛，在p>1时发散。

    本题首先需要把左奇点右无限区间的反常积分化为单边反常积分：

    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_{0}\frac{1}{x^a(1&plus;x)^b}dx=\int^{1}_{0}\frac{1}{x^a(1&plus;x)^b}dx&plus;\int^{&plus;\infty}_{1}\frac{1}{x^a(1&plus;x)^b}dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_{0}\frac{1}{x^a(1&plus;x)^b}dx=\int^{1}_{0}\frac{1}{x^a(1&plus;x)^b}dx&plus;\int^{&plus;\infty}_{1}\frac{1}{x^a(1&plus;x)^b}dx" title="\int^{+\infty}_{0}\frac{1}{x^a(1+x)^b}dx=\int^{1}_{0}\frac{1}{x^a(1+x)^b}dx+\int^{+\infty}_{1}\frac{1}{x^a(1+x)^b}dx" /></a>

    由于
    <a href="https://www.codecogs.com/eqnedit.php?latex=\lim_{x\rightarrow&space;0^&plus;}\frac{\frac{1}{x^a(1&plus;x)^b}}{\frac{1}{x^a}}=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\lim_{x\rightarrow&space;0^&plus;}\frac{\frac{1}{x^a(1&plus;x)^b}}{\frac{1}{x^a}}=1" title="\lim_{x\rightarrow 0^+}\frac{\frac{1}{x^a(1+x)^b}}{\frac{1}{x^a}}=1" /></a>
    ，
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^1_0\frac{1}{x^a(1&plus;x)^b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^1_0\frac{1}{x^a(1&plus;x)^b}" title="\int^1_0\frac{1}{x^a(1+x)^b}" /></a>
    与
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^1_0\frac{1}{x^a}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^1_0\frac{1}{x^a}" title="\int^1_0\frac{1}{x^a}" /></a>
    同敛散，故a<1时其收敛；

    由于
    <a href="https://www.codecogs.com/eqnedit.php?latex=\lim_{x\rightarrow&plus;\infty}\frac{\frac{1}{x^a(1&plus;x)^b}}{\frac{1}{x^(a&plus;b)}}=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\lim_{x\rightarrow&plus;\infty}\frac{\frac{1}{x^a(1&plus;x)^b}}{\frac{1}{x^(a&plus;b)}}=1" title="\lim_{x\rightarrow+\infty}\frac{\frac{1}{x^a(1+x)^b}}{\frac{1}{x^(a+b)}}=1" /></a>
    ，
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_1\frac{1}{x^a(1&plus;x)^b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_1\frac{1}{x^a(1&plus;x)^b}" title="\int^{+\infty}_1\frac{1}{x^a(1+x)^b}" /></a>
    与
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_1\frac{1}{x^(a&plus;b)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_1\frac{1}{x^(a&plus;b)}" title="\int^{+\infty}_1\frac{1}{x^(a+b)}" /></a>
    同敛散，故a+b>1时收敛。

    综上，则a<1且a+b>1时反常积分
    <a href="https://www.codecogs.com/eqnedit.php?latex=\int^{&plus;\infty}_0\frac{1}{x^a(1&plus;x)^b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int^{&plus;\infty}_0\frac{1}{x^a(1&plus;x)^b}" title="\int^{+\infty}_0\frac{1}{x^a(1+x)^b}" /></a>
    收敛

## 空间解析几何与向量代数
1. (张宇八套卷(一).01)

![images](./Pics/math_1.png)

<img src="./Pics/math_2.png" width = "300" height = "300" />


作水平刨面，此刨面切在离底h处，图中阴影是一个正方形，此正方形的边长为
<img src="https://latex.codecogs.com/gif.latex?\sqrt{R^2-h^2}" title="\sqrt{R^2-h^2}" />
。于是正方形的面积为
<img src="https://latex.codecogs.com/gif.latex?R^2-h^2" title="R^2-h^2" />
。用微元法，薄片的厚度为dh,薄片的体积：

<img src="https://latex.codecogs.com/gif.latex?dV=(R^2&space;-&space;h^2)dh" title="dV=(R^2 - h^2)dh" />

<img src="https://latex.codecogs.com/gif.latex?V=\int_0^R&space;(R^2&space;-&space;h^2)dh=(R^2h&space;-&space;\frac{1}{3}h^3)|^R_0=\frac{2}{3}R^3" title="V=\int_0^R (R^2 - h^2)dh=(R^2h - \frac{1}{3}h^3)|^R_0=\frac{2}{3}R^3" />

图中画的是整个公共部分的1/8，所以所求公共部分是
<img src="https://latex.codecogs.com/gif.latex?\frac{16}{3}R^3" title="\frac{16}{3}R^3" />
。


2. (张宇八套卷(二).04)空间n个点
<img src="https://latex.codecogs.com/gif.latex?P_i(x_i,y_i,z_i),i=1,2,...,n,n\geq4" title="P_i(x_i,y_i,z_i),i=1,2,...,n,n\geq4" />
矩阵

<img src="https://latex.codecogs.com/gif.latex?A=&space;\begin{bmatrix}&space;x_1&space;&&space;y_1&space;&&space;z_1&space;&&space;1\\&space;x_2&space;&&space;y_2&space;&&space;z_2&space;&&space;1\\&space;...&space;&&space;...&space;&&space;...&space;&&space;...\\&space;x_n&space;&&space;y_n&space;&&space;z_n&space;&&space;1&space;\end{bmatrix}" title="A= \begin{bmatrix} x_1 & y_1 & z_1 & 1\\ x_2 & y_2 & z_2 & 1\\ ... & ... & ... & ...\\ x_n & y_n & z_n & 1 \end{bmatrix}" />

的秩记为r，则n个点共面的充分必要条件是（）

A. r=1 B. r=2 C. r=3 **D.1<=r<=3**

设这n个点共面，则其中任取4个点，例如P1,P2,P3和P4也必共面。于是

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;x_1&space;&&space;y_1&space;&&space;z_1&space;&&space;1\\&space;x_2&space;&&space;y_2&space;&&space;z_2&space;&&space;1\\&space;x_3&space;&&space;y_3&space;&&space;z_3&space;&&space;1\\&space;x_4&space;&&space;y_4&space;&&space;z_4&space;&&space;1&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_1&space;&&space;y_1&space;&&space;z_1&space;&&space;1\\&space;x_2-x_1&space;&&space;y_2-y_1&space;&&space;z_2-z_1&space;&&space;0\\&space;x_3-x_1&space;&&space;y_3-y_1&space;&&space;z_3-z_1&space;&&space;0\\&space;x_4-x_1&space;&&space;y_4-y_1&space;&&space;z_4-z_1&space;&&space;0&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;x_2-x_1&space;&&space;y_2-y_1&space;&&space;z_2-z_1&space;\\&space;x_3-x_1&space;&&space;y_3-y_1&space;&&space;z_3-z_1&space;\\&space;x_4-x_1&space;&&space;y_4-y_1&space;&&space;z_4-z_1&space;\end{bmatrix}&space;=0" title="\begin{bmatrix} x_1 & y_1 & z_1 & 1\\ x_2 & y_2 & z_2 & 1\\ x_3 & y_3 & z_3 & 1\\ x_4 & y_4 & z_4 & 1 \end{bmatrix} = \begin{bmatrix} x_1 & y_1 & z_1 & 1\\ x_2-x_1 & y_2-y_1 & z_2-z_1 & 0\\ x_3-x_1 & y_3-y_1 & z_3-z_1 & 0\\ x_4-x_1 & y_4-y_1 & z_4-z_1 & 0 \end{bmatrix} = \begin{bmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ x_3-x_1 & y_3-y_1 & z_3-z_1 \\ x_4-x_1 & y_4-y_1 & z_4-z_1 \end{bmatrix} =0" />

最后一个行列式为0来自三点式平面方程，所以D项正确。

反之，设1<=r<=3，则A中任取一个4阶矩阵，其对应的行列式必为零，因此4点必共面，所以这n个点必共面。





## 多元函数微分



## 无穷级数
(2016.19)已知函数f(x)可导，且f(0)=1,
<a href="https://www.codecogs.com/eqnedit.php?latex=0<{f}'(x)<\frac{1}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0<{f}'(x)<\frac{1}{2}" title="0<{f}'(x)<\frac{1}{2}" /></a>
,设数列
<a href="https://www.codecogs.com/eqnedit.php?latex=\{x_n\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\{x_n\}" title="\{x_n\}" /></a>
满足
<img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}=f(x_n)(n=1,2,3,...)" title="x_{n+1}=f(x_n)(n=1,2,3,...)" />
证明：

1）级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}(x_{n&plus;1}-x_n)" title="\sum^{+\infty}_{n=1}(x_{n+1}-x_n)" />
绝对收敛

2）
<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}x_n" title="\lim_{n\rightarrow\infty}x_n" />
存在，且
<img src="https://latex.codecogs.com/gif.latex?0<\lim_{n\rightarrow\infty}x_n<2" title="0<\lim_{n\rightarrow\infty}x_n<2" />

证明：

1）若要证明级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}(x_{n&plus;1}-x_n)" title="\sum^{+\infty}_{n=1}(x_{n+1}-x_n)" />
绝对收敛，即证明
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}|x_{n&plus;1}-x_n|" title="\sum^{+\infty}_{n=1}|x_{n+1}-x_n|" />
收敛。

依题意，利用比较审敛法：

<img src="https://latex.codecogs.com/gif.latex?|x_{n&plus;1}-x_n|=|f(x_n)-f(x_{n-1})|=|f'(\xi)(x_n-x_{n-1})|=f'(\xi)|(x_n-x_{n-1})|" title="|x_{n+1}-x_n|=|f(x_n)-f(x_{n-1})|=|f'(\xi)(x_n-x_{n-1})|=f'(\xi)|(x_n-x_{n-1})|" />

其中，
<img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" />
介于
<img src="https://latex.codecogs.com/gif.latex?x_n,x_{n-1}" title="x_n,x_{n-1}" />
之间

<img src="https://latex.codecogs.com/gif.latex?<\frac{1}{2}|x_n-x_{n-1}|<...<\frac{1}{2^{n-1}}|x_2-x_1|" title="<\frac{1}{2}|x_n-x_{n-1}|<...<\frac{1}{2^{n-1}}|x_2-x_1|" />

显然，无穷级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{\infty}_{n=1}\frac{1}{2^{n-1}}|x_2-x_1|=|x_2-x_1|\sum^{\infty}_{n=1}\frac{1}{2^{n-1}}" title="\sum^{\infty}_{n=1}\frac{1}{2^{n-1}}|x_2-x_1|=|x_2-x_1|\sum^{\infty}_{n=1}\frac{1}{2^{n-1}}" />
收敛，所以根据比较审敛法，无穷级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}|x_{n&plus;1}-x_n|" title="\sum^{+\infty}_{n=1}|x_{n+1}-x_n|" />
收敛，即无穷级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}(x_{n&plus;1}-x_n)" title="\sum^{+\infty}_{n=1}(x_{n+1}-x_n)" />
绝对收敛。

2）由1）问结论，无穷级数
<img src="https://latex.codecogs.com/gif.latex?\sum^{&plus;\infty}_{n=1}(x_{n&plus;1}-x_n)" title="\sum^{+\infty}_{n=1}(x_{n+1}-x_n)" />
绝对收敛，则其部分和的极限
<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}S_n=\sum^{\infty}_{i=1}(x_{n&plus;1}-x_n)=\lim_{n\rightarrow\infty}(x_{n&plus;1}-x_1)" title="\lim_{n\rightarrow\infty}S_n=\sum^{\infty}_{i=1}(x_{n+1}-x_n)=\lim_{n\rightarrow\infty}(x_{n+1}-x_1)" />
存在，即
<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}x_n" title="\lim_{n\rightarrow\infty}x_n" />
存在。

设<img src="https://latex.codecogs.com/gif.latex?\lim_{n\rightarrow\infty}x_n=a" title="\lim_{n\rightarrow\infty}x_n=a" />

由于f(x)可导，从而f(x)连续，对
<img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;f(x_n)" title="x_{n+1} = f(x_n)" />
等式两边取极限得 a = f(a)

又 <img src="https://latex.codecogs.com/gif.latex?f(x_n)-f(0)=f'(\xi)x_n" title="f(x_n)-f(0)=f'(\xi)x_n" />

其中，
<img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" />
介于
<img src="https://latex.codecogs.com/gif.latex?0,x_{n}" title="0,x_{n}" />
之间

同样，对等式两边取极限

<img src="https://latex.codecogs.com/gif.latex?f(a)-f(0)=f'(\xi)a" title="f(a)-f(0)=f'(\xi)a" />

<img src="https://latex.codecogs.com/gif.latex?\frac{a-1}{a}=f'(\xi)" title="\frac{a-1}{a}=f'(\xi)" />

则，

<img src="https://latex.codecogs.com/gif.latex?0<\frac{a-1}{a}<2" title="0<\frac{a-1}{a}<2" />

所以
<img src="https://latex.codecogs.com/gif.latex?0<a<2" title="0<a<2" />
,即
<img src="https://latex.codecogs.com/gif.latex?0<\lim_{n\rightarrow\infty}x_n<2" title="0<\lim_{n\rightarrow\infty}x_n<2" />

题设得证。

## 线性方程组
(张宇八套卷(三).06)设A是3阶矩阵，
<img src="https://latex.codecogs.com/gif.latex?\xi_1=(1,2,-2)^T,&space;\xi_2=(2,1,-1)^T,\xi_3=(1,1,t)^T," title="\xi_1=(1,2,-2)^T, \xi_2=(2,1,-1)^T,\xi_3=(1,1,t)^T," />
是非齐次线性方程组Ax=b的解向量，其中
<img src="https://latex.codecogs.com/gif.latex?b=(1,3,-2)^T" title="b=(1,3,-2)^T" />
则

A. t=-1时，必有r(A)=1

B. t=-1时，必有r(A)=2

**C. t!=-1时，必有r(A)=1**

D. t!=-1时，必有r(A)=2

记
<img src="https://latex.codecogs.com/gif.latex?B=(\xi_1,\xi_2,\xi_3)=&space;\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1\\&space;2&space;&&space;1&space;&&space;1\\&space;-2&space;&&space;-1&space;&&space;t&space;\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1\\&space;0&space;&&space;-3&space;&&space;-1\\&space;0&space;&&space;3&space;&&space;t&plus;2&space;\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1\\&space;0&space;&&space;-3&space;&&space;-1\\&space;0&space;&&space;0&space;&&space;t&plus;1&space;\end{bmatrix}" title="B=(\xi_1,\xi_2,\xi_3)= \begin{bmatrix} 1 & 2 & 1\\ 2 & 1 & 1\\ -2 & -1 & t \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 1\\ 0 & -3 & -1\\ 0 & 3 & t+2 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 1\\ 0 & -3 & -1\\ 0 & 0 & t+1 \end{bmatrix}" />
由
<img src="https://latex.codecogs.com/gif.latex?\xi_1,\xi_2,\xi_3" title="\xi_1,\xi_2,\xi_3" />
是Ax=b的解向量，t!=-1时，r(B)=3,知
<img src="https://latex.codecogs.com/gif.latex?\xi_1,\xi_2,\xi_3" title="\xi_1,\xi_2,\xi_3" />
线性无关，
<img src="https://latex.codecogs.com/gif.latex?\xi_1-\xi_2,\xi_2-\xi_3" title="\xi_1-\xi_2,\xi_2-\xi_3" />
是对应其次方程组Ax=0的两个线性无关解，故r(A)=<1

若A=O，则Ax=b无解，故r(A)>0，综上r(A)=1

## 随机事件和概率

1. (张宇八套卷(二).07) 设A,B为两个事件，若P(B)>0,则下列结论正确的是（）

A.<img src="https://latex.codecogs.com/gif.latex?P(A|A\cup&space;B)=P(A|B)" title="P(A|A\cup B)=P(A|B)" />

B.<img src="https://latex.codecogs.com/gif.latex?P(A|A\cup&space;B)<P(A|B)" title="P(A|A\cup B)<P(A|B)" />

C.<img src="https://latex.codecogs.com/gif.latex?P(A|A\cup&space;B)>P(A|B)" title="P(A|A\cup B)>P(A|B)" />

D.<img src="https://latex.codecogs.com/gif.latex?P(A|A\cup&space;B)\geq&space;P(A|B)" title="P(A|A\cup B)\geq P(A|B)" />

设P(A-B)=x,P(B-A)=y,P(AB)=z,

<img src="https://latex.codecogs.com/gif.latex?P(A|A\cup&space;B)=\frac{P[A|(A\cup&space;B)]}{P(A\cup&space;B)}=\frac{P(A)}{P(A)&plus;P(B)-P(AB)}=\frac{x&plus;z}{x&plus;y&plus;z}" title="P(A|A\cup B)=\frac{P[A|(A\cup B)]}{P(A\cup B)}=\frac{P(A)}{P(A)+P(B)-P(AB)}=\frac{x+z}{x+y+z}" />

<img src="https://latex.codecogs.com/gif.latex?P(A|B)=\frac{P(AB)}{P(B)}=\frac{z}{y&plus;z}" title="P(A|B)=\frac{P(AB)}{P(B)}=\frac{z}{y+z}" />

D项正确！


## 一维随机变量函数的分布

(2016.22)设二维随机变量(X,Y)在区域
<img src="https://latex.codecogs.com/gif.latex?D=\{(x,y)|0<x<1,x^2<y<\sqrt{x}\}" title="D=\{(x,y)|0<x<1,x^2<y<\sqrt{x}\}" />
上服从均匀分布，令


3)求Z=U+X的分布函数F(z)

首先求出(X,Y)的概率密度f(x,y)

<img src="https://latex.codecogs.com/gif.latex?f(x,y)&space;=\begin{cases}\frac{1}{S_D}&space;&&space;(x,y)&space;\in&space;D\\0&space;&&space;others\end{cases}" title="f(x,y) =\begin{cases}\frac{1}{S_D} & (x,y) \in D\\0 & others\end{cases}" />

其中
<img src="https://latex.codecogs.com/gif.latex?S_D" title="S_D" />
为区域D的面积

<img src="https://latex.codecogs.com/gif.latex?S_D=\int^1_0(\sqrt&space;x&space;-&space;x^2)dx&space;=&space;1/3" title="S_D=\int^1_0(\sqrt x - x^2)dx = 1/3" />

<img src="https://latex.codecogs.com/gif.latex?f(x,y)&space;=\begin{cases}3&space;&&space;0<x<1,x^2<y<\sqrt&space;x\\0&space;&&space;others\end{cases}" title="f(x,y) =\begin{cases}3 & 0<x<1,x^2<y<\sqrt x\\0 & others\end{cases}" />

然后开始求F(z)










