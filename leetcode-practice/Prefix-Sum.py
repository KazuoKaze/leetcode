## Summary of what i can do:
## I can make a prefix_arr to find sum in a range
## I can take sums of all arr and minus mah sum of left numbers and my current num to find pivot index # if left_sum == total_sum - left_sum - nums[i] ## i can also use this to make a right sum prefix so i dont need to do right_sum = [] like this i can make this on a fly
## 

## 


class NumArray(object):
    def __init__(self, nums):
        self.prefix_sum = [0] * len(nums)
        self.prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]
        print(self.prefix_sum, 'sum arr')

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param1 = obj.sumRange(0, 5)
print(param1, 'ans')


# 724. Find Pivot Index


class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1
        
nums = [1,7,3,6,5,6]
sl = Solution()
print(sl.pivotIndex(nums))






class Solution(object):
    def leftRightDifference(self, nums):
        left_sum = 0
        output = []
        total_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            output.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return output
    
        ## mah code B:

        # leftSum = [0] * len(nums)
        # rightSum = [0] * len(nums)

        # for i in range(1, len(nums)):
        #     leftSum[i] = leftSum[i - 1] + nums[i - 1]

        # for j in range(len(nums) - 2, -1, -1):
        #     rightSum[j] = rightSum[j + 1] + nums[j + 1]

        # output = [0] * len(nums)
        # for k in range(len(nums)):
        #     num = leftSum[k] - rightSum[k]
        #     output[k] = abs(num)

        # return output

sl = Solution()
nums = [10,4,8,3]
print(sl.leftRightDifference(nums))