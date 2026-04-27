class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedStrings = defaultdict(list)
        for s in strs:
            sortedString = ''.join(sorted(s))
            sortedStrings[sortedString].append(s)

        return list(sortedStrings.values())
