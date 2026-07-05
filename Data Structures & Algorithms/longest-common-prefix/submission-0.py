class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # longest prefix = check the first few until dead end 

        # start with first word, AT MOST the base, could be "" 
        prefix = strs[0]

        for i in range(1, len(strs)): 
            # idx tracker of prefix length, 0 = nothing match
            j = 0

            # increment j as long as the idx is valid 
            # (smaller than the length of 1st word or the words we check after )
            while j < min(len(prefix), len(strs[i])):
                # if the letters dont match @ the idx, dont increment and return what we have so far
                if prefix[j] != strs[i][j]:
                    break
                # increment if letters match to be included in prefix 
                j += 1
            # return thr running prefix length, [:0] means nothing in common ""
            prefix = prefix[:j]
            
        
        return prefix