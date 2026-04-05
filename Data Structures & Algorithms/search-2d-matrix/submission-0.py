class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l+r)//2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                ll, rr, = 0, len(matrix[m])-1

                while ll <= rr:
                    mm = (ll + rr)//2
                    if target > matrix[m][mm]:
                        ll = mm + 1
                    elif target < matrix[m][mm]:
                        rr = mm - 1
                    else:
                        return True
                return False
        return False
                    
