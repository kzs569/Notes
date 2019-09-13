# Week Five - Binary Trees

1、(1分)一棵有512个结点的完全二叉树的高度为多少？（独根树高度为1）

What is the height of a complete binary tree with 512 nodes? (the height of a tree with only a root is 1)

**答案： 10**

2、(1分)已知一棵树的中序遍历为DBGEACF，后序遍历为DGEBFCA，求这棵树的前序遍历。（字母和字母之间不要有空格）

The infix order sequence of a tree is DBGEACF, and its post order sequence is DGEBFCA, please write down its preorder sequence. (There is no blank space between letters)

**答案： ABDEGCF**

3、(1分)请写出下面这棵二叉树的中序遍历（字母和字母之间不要有空格）
 
Please write down the infix order sequence of the following binary tree. (There is no blank space between letters)
![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yafc1uanj309p04y74f.jpg)

**答案： LXMECKPBQHDA**

4、(1分)在一棵非空二叉树中，若度为0的结点的个数n，度为2的结点个数为m，则有n=________ (系统根据字符串匹配来判定答案，所以您的答案中请不要包含空格)
 
For a binary tree with at least one node, if there are n nodes with degree 0 and m nodes with degree 2, then n = ________（This problem is judged by string matching, Please make sure your answer don't contain any blanks.）

**答案： m+1**

5、(1分)下列关于二叉树性质的说法正确的有：（多选）

Which sentences of the followings are right about a binary tree's characterization:（There are more than one correct answers）

**A、 非空满二叉树的结点个数一定为奇数个。 The amount of nodes of a full binary tree with at least one node must be odd.**

 B、 非完全二叉树也可以用像完全二叉树那样使用顺序存储结构进行存储。Sequential storing structure can also be used to store an incomplete binary tree just like to store a complete binary tree.
 
 **C、 当一棵完全二叉树是满二叉树时，叶子结点不一定集中在最下面一层。If a complete binary tree is a full binary tree, it will be possible that leaf nodes is no t on the nethermost layer.**
 
 D、 完全二叉树最多只有最下面的一层结点度数可以小于2。For a complete binary tree, only the degrees of nodes on the nethermost layer could be less than 2.
 
 **E、 一棵非空二叉树的为空的外部结点数目等于其结点数加1。The amount of external null nodes in a binary tree with at least one node equals to its amount of nodes plus 1.**
 
 F、
满二叉树的所有结点的度均为2。All degrees of nodes in a full binary tree are 2.

6、(1分)下列关于二叉树遍历的说法正确的有:

Which sentences of the followings are right about traversal of a binary tree:

 A、 只有空二叉树和一个根结点的二叉树这两种二叉树的前序和中序遍历的顺序恰好一样。Only the sequences of preorder and infix order of the binary tree with no nodes or only one node are the same.

 **B、 所有结点左子树为空的二叉树的前序和中序遍历顺序恰好一样。The sequences of preorder and infix order of a binary tree with all nodes without left child tree are the same.**

 C、 所有结点右子树为空的二叉树的前序和中序遍历顺序恰好一样。The sequences of preorder and infix order of a binary tree with all nodes without right child tree are the same.

 **D、 只有空二叉树和一个根结点的二叉树这两种二叉树的前序和后序遍历的顺序恰好一样。Only the sequences of preorder and post order of the binary tree with no nodes or only one node are the same.**

 E、 所有结点左子树为空的二叉树的前序和后序遍历顺序恰好一样。The sequences of preorder and post order of a binary tree with all nodes without left child tree are the same.

 F、 所有结点右子树为空的二叉树的前序和后序遍历顺序恰好一样。The sequences of preorder and post order of a binary tree with all nodes without left child tree are the same.

 G、 只有空二叉树和一个根结点的二叉树这两种二叉树的中序和后序遍历的顺序恰好一样。Only the sequences of infix order and post order of the binary tree with no nodes or only one node are the same.

 H、 所有结点左子树为空的二叉树的中序和后序遍历顺序恰好一样。The sequences of infix order and post order of a binary tree with all nodes without left child tree are the same.

 **I、 所有结点右子树为空的二叉树的中序和后序遍历顺序恰好一样。The sequences of infix order and post order of a binary tree with all nodes without right child tree are the same.**

 **J、 存在一棵非空二叉树，它的前序、中序和后序遍历都是一样的。There exists a binary tree with at least one node, whose preorder, infix order and post order are all the same.**

7、(1分)一棵有510个结点的完全二叉树的高度为多少？（独根树高度为1)

What is the height of a complete binary tree with 510 nodes? (the height of a tree with only a root is 1)

**答案： 9**

8、(1分)从空二叉树开始，严格按照二叉搜索树的插入算法（不进行旋转平衡），逐个插入关键码{18,73,10,5,68,99,27,41,51,32,25}构造出一棵二叉搜索树，对该二叉搜索树按照前序遍历得到的序列为？（答案中每两个元素之间用一个空格隔开）

From a null binary tree, insert key values {18, 73, 10, 5, 68, 99, 27, 41, 51, 32, 25} successively according to the insertion algorithm of a binary search tree strictly (no rotation and balance) to construct a binary search tree. Please write down the sequence of preorder of this binary search tree. (There is one blank space between two elements)

**答案： 18 10 5 73 68 27 25 41 32 51 99**

9、(1分)题目如下未答题
![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yal2ujgej30wc01u0sv.jpg)

**答案： 6**

10、(1分)对于如下图所示的最大堆，删除掉最大的元素后，堆的前序遍历结果是

For the following maximum heap, after deleting the maximum element, the preorder traversal sequence is

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yaljkx3zj30ar05wdg9.jpg)

请依次写出插入到树中的元素，每两个元素之间用一个空格隔开。

Please write down the elements successively, and there is one blank space between two elements.

**答案： 59 43 24 12 23 37 28 5 57 48 3**

11、(1分)一组包含不同权的字母已经对应好Huffman编码，如果某一个字母对应编码001,下面说法正确的有

A group of letters with different weights has corresponded with Huffman codes, if a letter's corresponding code is 001, which sentences of the followings are right:

 **A、 以001开头的编码不可能对应其他字母。A code beginning with 001 couldn't correspond with other letters.**
 
 B、 以000开头的代码不可能对应任何字母。Codes beginning with 000 couldn't correspond with any letter.
 
 **C、 以01开头和1开头的代码肯定对应某个字母。Codes beginning with 01 or 1 must correspongding with some letters.**
 
 **D、 建好的Huffman树至少包含4个叶结点。The Huffman tree contains at least 4 leaf nodes.**
 
 E、 编码0和00可能对应于其他字母。Code 0 and 00 could corresponding with other letters.

12、(1分)请阅读下面一段代码 
Please read the following code 

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yamm3egxj30ax0bb74n.jpg)

若此段代码的作用是用来进行前序遍历，那么应该在几号访问点进行访问？（只需要填写数字）

if this code is used to do a preorder traversal, which visiting point should be visited? (You only need to write down the number)

**答案： 1**

13、(1分)如果按关键码值递增的顺序依次将n个关键码值插入到二叉搜索树中，如果对这样的二叉搜索树进行检索时，每次检索的字符都等概率的从这n个关键码值中选取，平均比较次数为多少？

If we insert n key values to a binary search tree successively from small to large, when we search this binary search tree, each time the search character is selected from these n key values with the same possibility, then how many times will the comparison be on average?

**答案： (n+1)/2**

14、(1分)下列关于堆的说法正确的有:
 
Which sentences of the followings are right:

 A、 堆一定是满二叉树。A heap must be a full binary tree.
 
 B、 最小堆中，最下面一层最靠右的结点一定是权值最大的结点。In a minimum heap, the rightest node on the nethermost layer must be the node with the largest value.
 
 C、 堆是实现优先队列的惟一方法。A heap is the only method to implement a priority queue.
 
 **D、 堆一定是完全二叉树。A heap must be a complete binary tree.**
 
 **E、 最小堆中，某个结点左子树中最大的结点可能比右子树中最小的结点小。In a minimum heap, the largest value on some node's left child tree could be possibly smaller than the smallest value of its right child tree.**
 
 **F、 使用筛选法建堆要比将元素一个一个插入堆来建堆效率高。Screening method has a higher efficiency than inserting elements one by one while constructing a heap.**

15、(1分)下列关于Huffman树和Huffman编码的说法正确的有:

Which sentences of the followings are right about Huffman tree and Huffman code:

 **A、 Huffman树一定是满二叉树。A Huffman tree must be a full binary tree.**

 **B、 Huffman编码是一种前缀编码。Huffman code is a kind of prefix code.**

 C、 Huffman树一定是完全二叉树。A Huffman tree must be a complete binary tree.

 D、 Huffman编码中所有编码都是等长的。All codes in a Huffman code have the same length.

 **E、 对于同样的一组权值两两不同的内容可以得到不同的Huffman编码方案。Different content with the same group of weights can get different Huffman codes.**

 F、 使用频率越高的字母，Huffman编码越长。The higher a letter's frequency is, the longer its Huffman code is.

16、(1分)对于给定的一组权W={1,4,9,16,25,36,49,64,81,100}，构造一棵具有最小带权外部路径长度的三叉树，写出这棵树的带权外部路径长度。

For a given group of weights W={1, 4, 9, 16, 25, 36, 49, 64, 81, 100}, please construct a ternary tree with a minimum weighted route length and write down this weighted route length.

**答案： 705**