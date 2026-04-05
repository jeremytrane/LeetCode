class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWordMap = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            sortedWordMap[sortedWord].append(word)
        return list(sortedWordMap.values())