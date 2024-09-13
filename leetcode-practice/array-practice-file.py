

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


# 108. Convert Sorted Array to Binary Search Tree


# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2

        root_node = TreeNode(nums[mid])

        root_node.left = self.sortedArrayToBST(nums[:mid])
        root_node.right = self.sortedArrayToBST(nums[mid + 1:])

        return root_node


sl = Solution()
nums = [-10,-3,0,5,9]
# print(sl.sortedArrayToBST(nums))
bst = sl.sortedArrayToBST(nums)



# 118. Pascal's Triangle

class Solution(object):
    def getRow(self, rowIndex):
        triangle = []
        for i in range(rowIndex):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

sl = Solution()
numRows = 1
print(sl.getRow(numRows))


