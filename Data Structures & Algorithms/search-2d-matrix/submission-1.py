class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l+r)//2

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                ll, rr = 0, len(matrix[m])-1
                while ll <= rr:
                    mm = (ll+rr)//2

                    if matrix[m][mm] == target:
                        return True
                    elif matrix[m][mm] < target:
                        ll = mm + 1
                    else:
                        rr = mm - 1
                return False
        return False