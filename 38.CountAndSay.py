
######################
#
#author:StefanPochmann 
#
######################
class Solution:
#Solution 1 ...using a regular expression
	import re
	def countAndSay(self, n):
	    s = '1'
	    for _ in range(n - 1):
	        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
	    return s
# Why does ((.)*) work?
# Because that matches any amount of any characters, without caring whether they're the same.
#((.)\2*) on the other hand captures one character and then looks for more of that character

#Solution 2 ...using a regular expression

	def CountAndSay(self,n):
		s = '1'
		for _ in range(n-1):
			s = ''.join(str(len(group))+ digit for group, digit in re.findall(r'((.)\2*)',s))
		return s	
#Solution 3 ...using group by
	def countAndSay(self, n):
	    s = '1'
	    for _ in range(n - 1):
	        s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
	    return s

