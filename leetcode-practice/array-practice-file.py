

## 66. Plus One


class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0 

        digits.insert(0, 1)
        return digits
            

sl = Solution()
digits = [9,9,9]
print(sl.plusOne(digits))