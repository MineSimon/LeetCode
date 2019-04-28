class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m+n-1
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[idx] = nums1[m-1]
                m -= 1
            else:
                nums1[idx] = nums2[n-1]
                n -= 1
            idx -= 1
        if n:
            nums1[:n] = nums2[:n]
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    s.merge([0],0,[1],1)
