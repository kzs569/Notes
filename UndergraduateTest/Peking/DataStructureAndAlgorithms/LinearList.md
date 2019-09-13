# Week two - Linear List

1、(1分)下面关于线性表的叙述中，正确的是哪些？

Which of the followings about linear list are correct?（There are more than one answers.）
Select the answer that matches

 **A、 线性表采用顺序存储，必须占用一片连续的存储单元。Linear lists use sequential storage which must occupy a continuous memory units.**

 B、 线性表采用顺序存储，便于进行插入和删除操作。Linear lists using sequential storage, it is easy to do insert and delete operations.

 **C、 线性表采用链接存储，不必占用一片连续的存储单元。Linear lists using the linked storage, do not occupy a continuous memory units.**

 **D、 线性表采用链接存储，便于插入和删除操作。Linear lists using the linked storage, it is easy for insert and deleting operations.**

2、(1分)下面的叙述中正确的是：
Select the answer that matches （There are more than one correct answers）

 A、 线性表在链式存储时，查找第i个元素的时间与i的数值无关。When the linear list stored in linked form, the time to find the i-th element is regardless of the value of i.

 B、 线性表在顺序存储时，查找第i个元素的时间与i的数值成正比。When the linear list stored sequentially, the time to insert the i-th element is proportional to value with i.

 **C、 线性表在顺序存储时，查找第i个元素的时间与i的数值无关。When the linear list stored sequentially, the time to find the i-th element is regardless of the value of i.**

 **D、 线性表在链式存储时，插入第i个元素的时间与i的数值成正比。When linear lists stored in the linked form, the time to insert the i-th element is proportional to value with i.**

3、(1分)对于一个具有n个结点的单链表，在已知的结点*p后插入一个新结点的时间复杂度为O(___),在给定值为x的结点后插入一个新结点的时间复杂度为O(___)。（请依次填入,格式为(a)(b),如果您的答案中出现字母，请使用小写;后一空系统基于字符匹配来判定答案，所以您的答案中不要出现空格）

For a single linked list with n nodes, and after a known node *p to insert a new node, the time complexity is O (___); after a given node with x value insert a new node, the time complexity is O (___). (If your answer contains letters, use lowercase one.The second blank is judged by string matching, Please make sure your answer don't contain any blanks. )

**答案： (1)(n)**

4、(1分)带头结点head的循环链表的尾结点tail的特点是:  _____ （提示： 1.请使用“=” 2.系统基于字符匹配来判定答案，所以您的答案中不要出现空格）

The circular linked list with a head node, its tail node’s character is: _____.

(Hint:1. Please use "=" 2.This problem is judged by string matching, Please make sure your answer don't contain any blanks. )

**答案： tail->next=head**

5、(1分)完成在双循环链表结点p之后插入s的操作为：

The operation to insert s after the doubly circular linked list’s node p is: (There are more than one answers.)

 **A、 p->next->prev=s; s->prev=p; s->next=p->next; p->next=s;**
 
 B、 p->next->prev=s; p->next=s; s->prev=p; s->next=p->next;
 
 C、 s->prev=p; s->next=p->next; p->next=s; p->next->prev=s;
 
 **D、 s->next=p->next; p->next->prev=s; s->prev=p; p->next=s;**
