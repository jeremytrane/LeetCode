class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)

        for i in range(len(s1)):
            count_s1[s1[i]] += 1
            count_s2[s2[i]] += 1

        k = len(s1)

        if count_s1 == count_s2:
            return True

        for i in range(k, len(s2)):
            count_s2[s2[i]] += 1
            count_s2[s2[i-k]] -= 1
            if count_s2[s2[i-k]] == 0:
                del count_s2[s2[i-k]]

            if count_s1 == count_s2:
                return True

        return False