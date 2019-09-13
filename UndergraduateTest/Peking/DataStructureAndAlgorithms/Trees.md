# Week seven - Trees

1、(1分)一个深度为h的满k叉树，最多有多少个结点？（独根树深度为0）

There is a full k-ary tree, whose depth is h. How many nodes can it have at most? (The depth of a tree, which only has a root node, is 0.)

 A、 k^(h-1)
 
 B、 k^h
 
 **C、 (k^(h+1)-1)/(k-1)**
 
 D、 (k^h-1)/(k-1)
 
2、(1分)若一个具有N个顶点，K条边的无向图是一个森林（N>K且2K>=N），则该森林有多少棵树？ 

There is an undirected graph. It has N nodes and K edges. (N>K and 2K>=N). If it is a forest, then how many trees will it has?

**答案： N-K**

3、(1分)将下图的二叉树转换为对应的森林，按照先根次序列出其结点。（答案的字母之间没有空格）

Transform this binary tree into the corresponding forest, and write down the pre-order node sequence. (Do not add spaces in your answer.)

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybiu13jaj30a60a1glo.jpg)

**答案： ABECFDGHIJKL**

4、(1分)一棵完全三叉树，下标为121的结点在第几层？

（注：下标号从0开始，根的层数为0）

In a complete 3-ary tree, what level is the node, whose subscript is 121, stand on?

(P.S. the subscript starts form 0, and the level of root node is 0)

**答案： 5**

5、(1分)根据树的双标记层次遍历序列，求其带度数的后根遍历序列

Given the double-tagging level-order traversal sequence of a tree, please write down the post-order traversal sequence with degree.

比如：已知一棵树的双标记层次遍历序列如下：

For example, assume that a tree's double-tagging level-order traversal sequence is shown as followed:

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybj2i6wzj30kb0cp0ta.jpg)

**答案： H0 C1 D0 G0 B3 F0 I0 E2 A2**

6、(1分)给出一棵树的逻辑结构T=(N,R),其中：

N={A,B,C,D,E,F,G,H,I,J,K} 

R={r} 

r={(A,B),(B,E),(B,F),(F,G),(F,H),(A,C),(C,I),(C,J),(J,K),(A,D)}

试回答下列问题：

Given a logical structure of a tree, T=(N, R), and N={A, B, C, D, E, F, G, H, I, J, K}, R={r}, r={(A,B), (B,E), (B,F), (F,G), (F,H), (A,C), (C,I), (C,J), (J,K), (A,D)}  Please answer these questions: 

（1）哪个是F的父结点？which is the parent node of Node F?

（2）哪些是B的子孙？which are the offspring of Node B?

（3）以结点C为根的子树的深度是多少？what is the depth of the sub-tree whose root node is Node C? 

（注：根的层数为0，独根树深度为0，高度为1，其他题目同样如此；各个选项之间的答案用空格分隔就好；同一个选项的答案如果有多个字母，按照字典序排列，且不要以空格分隔） 

（P.S. the level of the root node is 0, the depth of a tree, which only has a root node, is 0, and its height is 1. Other problems have the same regulations. If there are several alphabets in one question, order them by lexicographical order, and do not add spaces.)

**答案： B EFGH 2**

7、(1分)对于以下等价类，采用“加权合并规则”（也称“重量权衡合并规则”），进行并查运算，给出最后父节点索引序列。

For the following equivalence class, please use "weighted union rule" and UNION/FIND algorithm to write down the final parent node index sequence. 

8-9 3-2 7-4 5-9 6-1 8-6 7-3 2-5 8-0 

注意：当合并大小相同的两棵树的时候，将第二棵树的根指向第一棵树的根；根节点的索引是它本身；数字之间用空格隔开。

Notice: When we join two trees with the same size, we let the root of the second tree point to the root of the first tree. The index of the root node is itself. Separate the numbers with only one spaces.

**答案： 8 6 3 7 7 8 8 8 8 8**

8、(1分)2-3树是一种特殊的树，它满足两个条件：

（1）每个内部结点有两个或三个子结点；

（2）所有的叶结点到根的路径长度相同；

如果一棵2-3树有9个叶结点，那么它可能有_________个非叶结点。 (多项)

2-3 tree is a special kind of tree, it satisfy:

（1）Every internal node has 2 or 3 child nodes. 

 (2)All the leaf nodes have the same length of the path to the root node.   If a 2-3 tree has 9 leaf nodes, then it may have __________ non-leaf nodes.（There are more than one correct answers）

 **A、 4**
 
 B、 5
 
 C、 6
 
 **D、 7**

5、(1分)将一棵树T转换为左子/右兄链表表示的二叉树B，则T的后根次序遍历序列是B的相应_________序列。（单选）

 Transform a tree T into a binary tree B, which is represented by Left-Child/Right-Sibling implementation. Then the post-order traversal sequence of T is the same as the __________ sequence of B.（There is only one correct answer）

 A、 前序遍历

 B、 后序遍历

 **C、 中序遍历**

 D、 层次遍历
