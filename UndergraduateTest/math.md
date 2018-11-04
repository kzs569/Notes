
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










