class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedList = defaultdict(list)

        for s in strs:
            sSorted = ''.join(sorted(s))
            sortedList[sSorted].append(s)
        return list(sortedList.values())