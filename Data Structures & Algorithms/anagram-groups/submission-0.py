class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = same sort order, ''.join(sorted(string))
        # hash table: {sorted string : [anagram array]}

        d = defaultdict(list)

        for word in strs: 
            str_sort = ''.join(sorted(word))
            d[str_sort].append(word)


        return list(d.values())