class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            add = 1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] + add <= 9:
                    digits[i] += add
                    return digits
                else:
                    if i != 0:
                        digits[i] = 0
                        continue
                    else:
                        res = [0 for _ in range(len(digits) + 1)]
                        res[0] = 1
                        return res
