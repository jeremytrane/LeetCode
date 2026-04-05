class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        fullLength = len(A) + len(B) 
        half = fullLength // 2
        l, r = 0, len(A) - 1

        while True:
            m = (l + r) // 2 
            m2 = half - m - 2
            
            Aleft = A[m] if m >= 0 else float("-inf")
            Aright = A[m+1] if m+1 < len(A) else float("inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")
            Bright = B[m2+1] if m2+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if fullLength%2:
                    return float(min(Aright, Bright))
                return (max(Aleft, Bleft)+min(Aright, Bright))/2.0
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1