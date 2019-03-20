class Solution:
    def isRectangleOverlap(self, rec1: list, rec2: list) -> bool:
        # 当矩阵1的右上角的坐标大于矩阵2的左下角坐标并且矩阵2的右上角坐标大于矩阵1的左下角坐标时，一定有重叠面积。
        return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[0] < rec1[2] and rec1[3] > rec2[1]

if __name__ == "__main__":
    s = Solution()
    print(s.isRectangleOverlap([7,8,13,15],[10,8,12,20]))
