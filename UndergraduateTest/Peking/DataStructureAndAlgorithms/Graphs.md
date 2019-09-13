# Week eight - Graphs

1、(1分)下图中的强连通分量的个数为多少个？

 How many strongly connected graphs in the under graph?

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybozd1rxj308s037jra.jpg)

**答案： 3**

2、(1分)在有向图G的拓扑序列中，若顶点$V_i$在$V_j$之前，则下列情形不可能出现的是（    ）。

In the topological order sequences of the directed graph G, if vertex Vi appears before Vj, then the impossible situation of the following is ()

 **A、G中有一条从$V_j$到$V_i$的路径 There is a path from $V_j$ to $V_i$ in the G.**

 B、G中有边($V_i$，$V_j$) G contains edge ($V_i$,$V_j$).

 C、G中有一条从$V_i$到$V_j$的路径    G contains a path from $V_i$ to $V_j$.

 D、G中没有边($V_i$，$V_j$) G doesn't contain edge($V_i$,$V_j$)

3、(1分)请使用Prim算法从结点0出发求下图的最小生成树，依次写出每次被加入到最小生成树中边的编号（如果同时存在多条边满足要求，选择编号最小的）。顶点a到顶点b (a < b)之间的边编号为ab，例如图中权值为1的边编号为02。(不同编号之间用一个空格分隔）

Please use prim algorithm starting from vertex 0 to find the minimum spanning tree of the following graph, write the number of the edge added into the minimum spanning tree in turn((if there are many vertices satisfy requirement, choose the vertex with minimum number). The number of the edge connecting vertex a and vertex b is ab. Like the edge with weight 1 in the graph, its number is 02(different numbers separated by a blank space).Screen Shot 2016-10-20 at 21.47.02.png

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybs8fkq4j30a708bq3o.jpg)

**答案： 02 25 35 12 14**

4、(1分)下列关于最短路算法的说法正确的有：

The right statements of the following are:

 **A、 当图中不存在负权回路但是存在负权边时，Dijkstra算法不一定能求出源点到所有点的最短路。 When the graph doesn't contain circuit of negative weight, but contains the edge of negative weight. Dijkstra algorithm can't guarantee the correctness of the algorithm.**

 **B、 当图中不存在负权边时，Dijkstra算法能求出每对顶点间最短路径。 When the graph doesn't contain edge of negative weight, Dijkstra algorithm can calculate the shortest path of each pair of vertices.**

 C、 当图中存在负权回路时，Dijkstra算法也一定能求出源点到所有点的最短路。When the graph contains the circuit of negative weight, Dijkstra algorithm can certainly calculate the shortest path form the single source to all the vertices.

 D、 Dijkstra算法不能用于每对顶点间最短路计算。Dijkstra algorithm can't be applied to calculate the shortest path of each pair of vertices.

5、(1分)题图为一无向图,分别写出从顶点1出发,按深度优先搜索遍历算法得到的顶点序列,和按广度优先搜索遍历算法得到的顶点序列

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybsf25saj30n60b70w6.jpg)

**答案： 123456 123564**

6、(1分)如果无向图G=(V,E)是简单图，并且|V|=n>0，那么图G最多包含多少条边？

答案是n-1, n*(n-1)/2, (n-1)*(n-2)/2，n*n/2 中的一个

If undirected graph G = (V,E) is simple graph, and |V| = n > 0, then how many edges can graph G contains at most？（There is only one correct answer）

**答案： n*(n-1)/2**

7、(1分)无向图G=(V, E)，其中：V={a, b, c, d, e, f}, E={(a, b), (a, e), (a, c), (b, e), (c, f), (f, d), (e, d)}，对该图进行深度优先遍历（优先访问编号小的结点），得到的顶点序列为？

Undirected G = (V,E), concretely: V = {a,b,c,d,e,f}, E = {(a,b),(a,e),(a,c),(b,e),(c,f),(f,d),(e,d)},perform depth-first traversal(visit the vertex of small number firstly), what vertices sequence do we get? 

 **A、 abedfc**

 B、 aebdfc

 C、 abcedf

8、(1分)下列关于最短路算法的说法正确的有：

The right statements of the following are:

 **A、 当图中不存在负权回路但是存在负权边时，Dijkstra算法不一定能求出源点到所有点的最短路。 When the graph doesn't contain circuit of negative weight, but contains the edge of negative weight. Dijkstra algorithm can't guarantee the correctness of the algorithm.**

 **B、 当图中不存在负权边时，Dijkstra算法能求出每对顶点间最短路径。 When the graph doesn't contain edge of negative weight, Dijkstra algorithm can calculate the shortest path of each pair of vertices.**

 C、 当图中存在负权回路时，Dijkstra算法也一定能求出源点到所有点的最短路。When the graph contains the circuit of negative weight, Dijkstra algorithm can certainly calculate the shortest path form the single source to all the vertices.

 D、 Dijkstra算法不能用于每对顶点间最短路计算。Dijkstra algorithm can't be applied to calculate the shortest path of each pair of vertices.


9、(1分)下面关于图的说法正确的有 The right statements of graphs in the following are:
 
 A、 对于有向图，每个结点的出度必须要等于入度。As for directed graph, each vertices’ out-degree is equal to its in-degree.
 
 B、 对于一个连通图，一定存在一种给边添加方向的方案使得这个图变成强连通图。For a connected graph, there must be a way of directing all the edges of the original graph to make the graph strongly connected graph.
 
 C、 对于有向图，所有结点的入度加起来一定为奇数。For directed graph, the sum of in-degrees of all nodes must be odd number.
 
 **D、 对于无向图，所有结点的度数加起来一定是偶数。As for undirected graphs, the sum of degrees of all vertices is definitely even number.**
 
 **E、 将有向图的一个强连通分量中的边全部反向仍然是强连通分量。Reversion all the edges of a strongly connected component of a directed graph, then the subgraph is still a strongly connected component.**

10、(1分)有向图G如下图所示，请写出所有拓扑排序序列。所有的顶点都直接用其数字标号表示，如拓扑排序序列为25.png，那么请写成1234（中间没有空格）。不同的拓扑排序序列按照字典序排序，中间用一个空格隔开。

Directed graph G looks like following graph, please list all the topological order sequences. All the vertices are marked by numbers directly. Like topological order sequence V1V2V3V4, we write it as 1234(with no blank space).Different topological order sequences are sorted according to alphabet order, and separated by a blank space.

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6ybuzvazbj30bs05fwej.jpg)

**答案： 1234 1324 2134**