
## Prefix Sum


# Prefix Sum is a powerful technique used to quickly answer range sum queries in an array. It involves creating an auxiliary array where each element at index i stores the sum of the elements from the start of the array up to index i. This allows you to calculate the sum of any subarray efficiently.

# Basic Concept
# Given an array arr, the prefix sum array prefix is defined as:

# prefix[0] = arr[0]
# prefix[i] = prefix[i - 1] + arr[i] for i > 0
# For example, if arr = [2, 4, 5, 7, 8], then the prefix sum array would be:

# prefix[0] = 2
# prefix[1] = 2 + 4 = 6
# prefix[2] = 6 + 5 = 11
# prefix[3] = 11 + 7 = 18
# prefix[4] = 18 + 8 = 26
# So, the prefix sum array is [2, 6, 11, 18, 26].

# How to Use Prefix Sum
# To find the sum of any subarray arr[l:r] (from index l to r inclusive):

# If l == 0, the sum is simply prefix[r].
# If l > 0, the sum is prefix[r] - prefix[l-1].
# Example: To find the sum of the subarray from index 1 to 3 in [2, 4, 5, 7, 8]:

# Using prefix sum: prefix[3] - prefix[0] = 18 - 2 = 16.
# When to Use Prefix Sum
# Range Sum Queries: If you need to perform multiple range sum queries on an array.
# Subarray Problems: Problems involving finding subarrays that meet specific criteria, such as maximum subarray sum.
# Dynamic Arrays: When you need to answer dynamic queries about sums in an array that is not frequently updated.
# Variations of Prefix Sum
# 2D Prefix Sum: Used for matrices where you want to find the sum of elements in a submatrix efficiently.
# Difference Array: Useful when you need to apply updates to a range of indices in an array.
# Cumulative Product: Instead of sums, you can use a similar approach for cumulative products.
# Common Problems and Approaches
# Subarray Sum Equals K:

# Approach: Use prefix sums with a hash map to store the frequency of prefix sums. For each prefix sum, check if current prefix sum - k exists in the hash map.
# Find Pivot Index:

# Approach: Use prefix sums to compare the sum of elements on the left and right of each index.
# Maximum Size Subarray Sum Equals K:

# Approach: Similar to subarray sum equals k, but you need to track the longest subarray length.
# Problem-Solving Tips
# Identify Patterns: If a problem involves querying or updating subarray sums frequently, prefix sums might be a good fit.
# Pre-compute Values: Pre-compute prefix sums so that you can answer queries in constant time.
# Use Auxiliary Structures: For variations like subarray sum equals k, use additional data structures like hash maps.
# Example Problem
# Problem: Given an array, find the sum of elements between indices l and r.

# Solution:


def range_sum(arr, start, end):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    if start == 0:
        return prefix[end]
    else:
        return prefix[end] - prefix[start - 1]

# Example Usage
arr = [2, 4, 5, 7, 8]
print(range_sum(arr, 1, 3))  # Output: 16



# Key Takeaways
# Efficiency: Prefix sum technique allows you to reduce the time complexity of range sum queries to O(1) after an initial O(n) preprocessing step.
# Flexibility: Can be adapted to various problem types, including multi-dimensional arrays.
# Complementary Structures: Often used with hash maps or other data structures to solve more complex problems efficiently.








###  Two Pointers Technique










# The Two Pointers technique is a common algorithmic approach that uses two pointers to traverse data structures, usually arrays or linked lists. This technique helps in optimizing problems that can be solved by iterating over the data structure from both ends or in a bidirectional manner.

# Basic Concept
# The idea is to use two pointers (indices) to scan the data structure, usually one starting from the beginning (left) and the other from the end (right). By moving these pointers based on certain conditions, you can efficiently solve problems that would otherwise require more complex or slower algorithms.

# When to Use Two Pointers

# Sorting and Searching: Finding pairs in a sorted array that sum to a target value.
# Merging: Merging two sorted arrays.
# Palindrome Checking: Checking if a string is a palindrome by comparing characters from both ends.
# Partitioning: Partitioning arrays in quicksort.


# Common Variations


# Opposite Ends: Start with pointers at opposite ends and move them towards each other based on some conditions.
# Same Direction: Both pointers start from the same end but move at different speeds or steps, often used in linked list problems.
# Sliding Window: One pointer represents the start of a window and the other represents the end, useful in substring or subarray problems.


# How to Approach Two Pointers Problems


# Identify Conditions: Understand the problem constraints and how moving pointers will help achieve the goal.
# Initialize Pointers: Typically, left at the beginning (0) and right at the end (len(arr) - 1) of the array.
# Move Pointers: Decide when to move which pointer based on the conditions:
# If sum is too small, move the left pointer to increase the sum.
# If sum is too large, move the right pointer to decrease the sum.
# Edge Cases: Handle cases where pointers meet, arrays are empty, or values are out of bounds.


# Example Problems and Approaches
# Two Sum (Sorted Array):

# Problem: Find two numbers in a sorted array that add up to a target sum.
# Approach: Use two pointers; start one pointer at the beginning and the other at the end. Check their sum:
# If the sum is too low, move the left pointer right to increase the sum.
# If the sum is too high, move the right pointer left to decrease the sum.


def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No valid pair found

nums = [2, 3, 4, 5, 9, 11]
target = 14
print(two_sum(nums, target))  # Output: [1, 4]



# Removing Duplicates from Sorted Array:

# Problem: Given a sorted array, remove duplicates in place and return the new length.
# Approach: Use two pointers:
# One pointer (i) keeps track of the unique elements.
# The second pointer (j) traverses the array to find new unique elements.


def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1  # Length of the array with unique elements

nums = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(nums))  # Output: 4, nums = [1, 2, 3, 4, ...]



# Container With Most Water:

# Problem: Given an array representing the height of lines, find two lines that together with the x-axis form a container that holds the most water.
# Approach: Use two pointers starting at the ends of the array, calculate the area, and move the pointer at the shorter line to try and find a taller line.


def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)

        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(heights))  # Output: 49


# Key Takeaways


# Efficiency: Two pointers often reduce the time complexity of problems that might require nested loops, usually bringing them down to O(n).
# Versatility: This technique can be used in various contexts like arrays, strings, and linked lists.
# Problem-Solving Strategy: Recognize patterns where two elements need to be compared or merged, especially when dealing with sorted data.
