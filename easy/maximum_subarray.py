'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
'''

def maxSubArray(nums):
    maxSum = None
    runningSum = 0

    for num in range(len(nums)):
        # Add the value of the element from the loop to runningSum
        runningSum += nums[num]

        # If maxSum is None (for the first iteration) or there's a new largest sum
        # (runningSum > maxSum) change the maxSum
        if maxSum is None or runningSum > maxSum:
            maxSum = runningSum

        # If the runningSum becomes negative start the sum over again with the
        # value from the next element in the array
        if runningSum < 0:
            runningSum = 0

    return maxSum


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

if __name__ == '__main__':
    main()
