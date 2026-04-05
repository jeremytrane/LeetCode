class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        one, two = cost[0], cost[1]

        for i in range(2, n):
            one, two = two, min(one, two) + cost[i]
        return min(one, two)