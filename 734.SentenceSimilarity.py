class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        words = defaultdict(set)
        for word1,word2 in pairs:
            words[word1].add(word2)
            words[word2].add(word1)
        for word1,word2 in zip(words1,words2):
            if word1 != word2 and word2 not in words[word1]:
                return False
        return True
        