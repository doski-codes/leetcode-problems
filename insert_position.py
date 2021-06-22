'''
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
left    right   mid     value
0       4       2       5
0       2       1       3
0       1       0       1

Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
left    right   mid     value
0       4       2       5
2       4       3       6
3       4       3       6

Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
left    right   mid     value
0       4       2       5
0       2       1       3
0       1       0       1

Output: 0

Example 5:

Input: nums = [1], target = 0
left    right   mid     value
0       1       0       1

Output: 0

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

def searchInsert(nums, target):
    # Define the starting and ending indexes
    left = 0
    right = len(nums)
    # Recursive function to get the index of the target
    return getTargetIndex(nums, target, left, right)

def getTargetIndex(nums, target, left, right):
    # Get the middle of the array
    mid = (left + right) // 2

    while left != mid:
        # Return the index if you find the value
        if nums[mid] == target:
            return mid
        # Run the function recursively with the starting index as the middle index
        # of the previous array if the target value is greater than the middle value
        elif nums[mid] < target:
            return getTargetIndex(nums, target, mid, right)
        # Run the function recursively with the ending index as the middle index
        # of the previous array if the target value is lessor than the middle value
        else:
            return getTargetIndex(nums, target, left, mid)

    # Return the index for target if its not in the array
    # The index is the index of the middle value if that value is less than the target
    # The index is the index+1 of the middle value if that value is greater or equal to the target
    return mid if nums[mid] >= target else mid+1

def main():
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums, target))

if __name__ == '__main__':
    main()
