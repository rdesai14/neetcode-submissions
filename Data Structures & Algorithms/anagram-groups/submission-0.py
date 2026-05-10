class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = defaultdict(list)

        for s in strs:
            sortStr = "".join(sorted(s))

            print (sortStr)

            anagram[sortStr].append(s)
        
        return list(anagram.values())

        