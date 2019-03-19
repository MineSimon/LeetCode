class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            mid = len(nums2) // 2
            if len(nums2) % 2 == 0:
                return (nums2[mid - 1] + nums2[mid]) / 2
            else:
                return nums2[mid]
        if len(nums2) == 0:
            mid = len(nums1) // 2
            if len(nums1) % 2 == 0:
                return (nums1[mid - 1] + nums1[mid]) / 2
            else:
                return nums1[mid]

        # 判断谁先结束取值（最大值小的），这里将nums1设置为先结束
        if nums1[-1] > nums2[-1]:
            temp = nums1
            nums1 = nums2
            nums2 = temp

        n1 = len(nums1)
        n2 = len(nums2)
        mid = (n1 + n2) // 2
        l = []
        i, j = 0, 0
        while i + j <= mid:
            if i < n1:
                if nums1[i] < nums2[j]:
                    l.append(nums1[i])
                    i += 1
                elif nums1[i] > nums2[j]:
                    l.append(nums2[j])
                    j += 1
                else:
                    l.append(nums1[i])
                    l.append(nums2[j])
                    i += 1
                    j += 1
            else:
                l.append(nums2[j])
                j += 1
        if (n1 + n2) % 2 == 0:
            return (l[mid - 1] + l[mid]) / 2
        else:
            return l[mid]



if __name__ == "__main__":
    s = Solution()
    print("中位数为:", s.findMedianSortedArrays([1,2],[3,4]))