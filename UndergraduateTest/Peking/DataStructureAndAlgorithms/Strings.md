# Week four - Strings

1、(1分)若字符串s=“software”，则其子串个数为： 

If the string s = "software", then the number of its sub-string is:

**答案： 37**

2、(1分)S=“S1S2…Sn”是一个长为n的字符串，存放在一个数组中，编程序将S改造之后输出。

S = "S1S2 ... Sn" is a string of length n, and stored in an array, output S after its programmable transformation.              

1.将S的所有第偶数个字符按照其原来的下标从大到小的次序放在S的后半部分；       

1.All the even-numbered characters of S should be placed in accordance with their subscript descending order in the second half of S;

2.将S的所有第奇数个字符按照其原来的下标从小到大的次序放在S的前半部分；

2.All the odd-numbered characters of S should be placed in accordance with their subscript ascending order in the first half of S.

例如：S=‘ABCDEFGHIJKL’，则改造后的S为‘ACEGIKLJHFDB’。则 S=’algorithm’, 改造后为____________（Hint： 1. 答案不需要加引号 2. 系统基于字符匹配来判定答案，所以您的答案中不要出现空格）。

For example: S = 'ABCDEFGHIJKL', then after the transformation S is 'ACEGIKLJHFDB'. If S = 'algorithm', then after the transformation S is ____________ (Hint:1. please don’t include any quotes in your answer. 2.This problem is judged by string matching, Please make sure your answer don't contain any blanks ).

**答案： agrtmhiol**

3、(1分)设有两个串p和q，其中q是p的子串，求q在p中首次出现的位置的算法称为( )（单选）

There are two strings p q, q is p’s substring. The algorithm to search the first time q appeared in p is called ( )（There is only one correct answer）

 A、 求子串 Seeking substring
 
 B、 联接 Concatenation
 
 **C、 匹配 Matching**
 
 D、 求串长 Seeking length
 
4、(1分)下列程序判断字符串s 是否对称，对称则返回1，否则返回0；如 f("abba")返回1，f("abab")返回0；

Use the following procedures to determine whether the string s is symmetry, symmetry returns 1, otherwise return 0; such as f ("abab") returns 0;

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yb29ojpgj30dj05i0sr.jpg)

注：(1)和(2)和(3)三个答案之间用空格分隔，每个答案是一个字符,不要加空格

**答案： j i j**

5、(1分)下面关于串的的叙述中，哪一个是不正确的:（单选）
 
Which of the following descriptions about string is not correct? （There is only one correct answer）

 A、 串是字符的有限序列 String is a finite sequence of characters.
 
 B、 模式匹配是串的一种重要运算 Pattern matching is an important operation.
 
 C、 串是一种数据对象和操作都特殊的线性表 String is a linear list whose data objects and operations both special
 
 **D、 空串是由空格构成的串 Empty string is a string consisting of spaces.**

6、(1分)一个文本串可用事先给定的字母映射表进行加密。例如，设字母映射表为：

A text string can be encrypted by the given letters mapping table. For example, the letters mapping table is:

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yb3ej5shj30860183yd.jpg)

比如字符串"encrypt"被加密为"tkzwsdf"。则字符串 “algorithm”，被加密为________________（Hint： 1. 答案不需要加引号 2. 系统基于字符匹配来判定答案，所以您的答案中不要出现空格）。

As the string "encrypt" is encrypted as "tkzwsdf", then the "algorithm" is encrypted as ________ (Hint：1. please don’t include any quotes in your answer 2. This problem is judged by string matching, Please make sure your answer don't contain any blanks.).

**答案：neopwmfbl**

7、(1分)若串S1=‘ABCDEFG’, S2=‘9898’ ,S3=‘###’,S4=‘012345’,执行       

concat(replace(S1,substr(S1,length(S2),length(S3)),S3),substr(S4,index(S2,‘8’),length(S2)))

注意：substr(S,i,j)是对字符串S的下标为i开始取j个字符，这里的下标是从0开始的(单选)

If the string S1 = 'ABCDEFG', S2 = '9898', S3 = '###', S4 = '012345', execute concat (replace (S1, substr (S1, length (S2), length (S3)), S3), substr (S4, index (S2, '8'), length (S2)))  Note substr (S, i, j) is the operation to take string S’s j characters from subscript i. Subscript here is starting from 0.（There is only one correct answer）

 A、 ABC###G0123
 
 B、 ABCD###2345
 
 **C、 ABCD###1234**
 
 D、 ABC###G2345

8、(1分)在字符{A, C, G, T}组成的DNA序列中，A和T、C和G是互补对。判断一个DNA序列中是否存在互补回文串（例如，ATCATGAT的补串是TAGTACTA，与原串形成互补回文串）。下面DNA序列中存在互补回文串的是：（多选）

In the DNA sequences consisting of character {A, C, G, T}, A and T, C and G are complementary pairs. Judging whether there is a complementary palindrome sequence in a DNA sequence (e.g., ATCATGAT’s complement strings is TAGTACTA, it is complementary palindrome sequence with the original sequence). Which of the following DNA sequences have complementary palindrome string? （There are more than one answers.）

 **A、 CTGATCAG**
 
 **B、 AATTAATT**
 
 C、 TGCAACGT
 
 D、 CATGGTAC
 
 **E、 GTACGTAC**
 
 **F、 AGCTAGCT**

9、(1分)Seek the string "BAAABBBAA" ‘s feature vector, where the feature vector is defined as follows:（There is only one correct answer）

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yb4cakhuj30n005fwfv.jpg)

 A、 {-1, 0, 0, 0, 0, 0, 0, 1, 2}

 **B、 {-1, 0, 0, 0, 0, 1, 1, 1, 2}**

 C、 {-1, 0, 0, 0, 0, 0, 1, 1, 2}

 D、 {-1, 0, 0, 0, 1, 1, 1, 1, 2}

10、(1分)下列说法正确的是：（单选）
 
Which of the following statements is correct? （There is only one correct answer）

 A、 空串就是空白串“Empty string” is blank string.

 **B、 空串是任意字符串的子串 Empty string is a substring of arbitrary string.**

 C、 串只可以采用顺序存储，不可以采用链式存储 String only can be stored in sequential method and cannot be stored in linked method.

 D、 在C++标准中，char S[M]最多能表示长度为M的字符串 In C ++ standards, char S[M] can represent up to a string of length M.

11、(1分)设有字符串变量String A ＝“”，B＝“MULE”，C＝“OLD”，D＝“MY” ; 请计算下列表达式 （3个答案本身不要出现空格，答案之间用空格分开）

 Assume that there is a string variable String A = "", B = "MULE", C = "OLD", D = "MY"; Please calculate the following expression: 

(1) D+C+B

(2) B.substr(3，2) 

(3) A.strlength()

**答案： MYOLDMULE E 0**

3、(1分)上一题中的字符串"BAAABBBAA"，与目标"BAAABBBCDDDCCHHHHBBBAAABBBAADD"进行匹配，至少需要多少次字符匹配（提示：利用优化后的Next数组):

The string in question above "BAAABBBAA" matches with "BAAABBBCDDDCCHHHHBBBAAABBBAADD". How many times character matching will need at least? (Hint: Use “Next” arrays ):

![undefined](http://ww1.sinaimg.cn/large/006ocvumly1g6yb83sbisj30ij0eqaay.jpg)

 A、 29
 
 B、 30
 
 **C、 31**
 
 D、 32
