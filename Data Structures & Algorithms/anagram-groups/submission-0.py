class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            sorted_dict[sorted_word].append(word)
        return list(sorted_dict.values())