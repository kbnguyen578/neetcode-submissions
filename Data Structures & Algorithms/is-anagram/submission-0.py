class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: same LENGTH, same CHARACTERS 

        if len(s) != len(t): 
            return False 
        
        # thought: the number of e/ letter in e/ strings should match the other string's count
        
        # initializing the dictionaries/hash table for the strings
        countS, countT = {}, {}

        # initial if gurantees same length for s & t 
        for i in range(len(s)):
            # key: value | s[i] (letter) : count (0 initial if not there, +1 for every letter)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # the dictionaries/hash table of letter count should be identical 
        return countS == countT
            