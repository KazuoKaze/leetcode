

# 66. Plus One


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



# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1



nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
sl = Solution()
print(sl.merge(nums1, m, nums2, n))



