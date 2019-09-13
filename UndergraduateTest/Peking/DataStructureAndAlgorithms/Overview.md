# Week One - Overview
1、(1分)下列不属于线性结构的是：

Which one of the followings does not belong to linear structure:（There is only one correct answer）

 A、 队列(queue)

 B、 散列表(hash table)

 C、 向量(vector)

 **D、 图(graph)**


2、(1分)关于算法特性描述正确的有：

Which one is right about algorithm’s characterization:（there are more than one correct answers）

 **A、 算法保证计算结果的正确性。Algorithm will ensure the correctness of the calculation results.**

 B、 组成算法的指令可以有限也可能无限。 Instructions which composite algorithms can be infinite or finite

 C、 算法描述中下一步执行的步骤不确定。 The next step in the implementation of the algorithm described is uncertain.

 **D、 算法的有穷性指算法必须在有限步骤内结束。The finite nature of algorithms means algorithm must be completed within a limited step.**

3、(1分)计算运行下列程序段后m的值：

Calculate the value of m after running the following program segment
``` 
n = 9; m = 0; 

for (i=1;i<=n;i++)

  for (j = 2*i; j<=n; j++)

    m=m+1;
```
求m的值

**答案： 20**

4、(1分)下列说法正确的是：

Which options may be correct?（there are more than one correct answers）

 **A、 如果函数f(n)是O(g(n))，g(n)是O(h(n))，那么f(n)是O(h(n))【 if f(n) is O(g(n))，g(n) is O(h(n))，then f(n) is O(h(n))】**

 **B、 如果函数f(n)是O(g(n))，g(n)是O(h(n))，那么f(n)+g(n)是O(h(n))【if f(n) is O(g(n))，g(n) is O(h(n))，so f(n)+g(n) is O(h(n))】**

 C、 如果a>b>1,logan是O(logbn)，但logbn不一定是O(logan)【if a>b>1,logan is O(logbn)， logbn may not be O(logan)】

 D、
函数f(n)是O(g(n))，当常数a足够大时，一定有函数g(n)是O(af(n))【if f(n)是O(g(n))，When constant a is big enough ，there must be g(n) is O(af(n))】


5、(1分)由大到小写出以下时间复杂度的序列： 答案直接写标号，如：(1)(2)(3)(4)(5) （提示：系统基于字符匹配来判定答案，所以您的答案中不要出现空格）

Write the following time complexity in descending sequence:Write down the answer labels such as (1)(2)(3)(4)(5). （Hint：This problem is judged by string matching, Please make sure your answer don't contain any blanks. ）

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6y7bhwtw9j306l05iwed.jpg)

**答案： (5)(1)(2)(4)(3)**

6.(1分)已知一个数组a的长度为n，求问下面这段代码的时间复杂度: 

An array of a, its length is known as n. Please answer the time complexity of the following code.（There are more than one answers.）
```
for (i=0,length=1;i<n-1;i++){

  for (j = i+1;j<n && a[j-1]<=a[j];j++)

    if(length<j-i+1)

      length=j-i+1;

}
```
A. $\Omega(n)$

B. $O\left(n^{2}\right)$

C. $ \theta(n^{2}) $

D. $O\left(n\right)$

答案 ： A,B

7. 以下哪种结构是逻辑结构，而与存储和运算无关：

Which of the following structure is a logical structure regardless of the storage or algorithm:（There is only one correct answer）

 **A、 队列(queue)**
 
 B、 双链表(doubly linked list)
 
 C、 数组(array)
 
 D、 顺序表(Sequential list)