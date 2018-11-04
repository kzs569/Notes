数据集整理
=====
# 目录
<!-- TOC -->
-
<!-- TOC -->

## Tencent中文词向量数据集

主页传送门 ： [Tencent AI Lab Embedding Corpus for Chinese Words and Phrases](https://ai.tencent.com/ailab/nlp/embedding.html)

概况：800w+中文词汇（每个词对应200维向量）

重点提升：覆盖率、新鲜度、准确性

语料：腾讯新闻和天天快报的新闻语料，自行抓取的互联网网页和小说语料。

词库构建：除了引入维基百科和百度百科的部分词条之外，还实现了Shi等人于2010年提出的[语义扩展算法](http://aclweb.org/anthology/N18-2028)，可从海量的网页数据中自动发现新词——根据词汇模式和超文本标记模式，在发现新词的同时计算新词之间的语义相似度。

训练算法：Tencent自研的[Directional Skip-Gram(DSG)](http://aclweb.org/anthology/N18-2028)算法。DSG算法基于广泛采用的词向量训练算法Skip-Gram (SG)，在文本窗口中词对共现关系的基础上，额外考虑了词对的相对位置，以提高词向量语义表示的准确性。