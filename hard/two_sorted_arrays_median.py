'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000

Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = (len(A) + len(B))
    mid = total // 2

    # Check if A has more elements than B and ensure that A has the least number of elements
    if len(A) > len(B):
        A, B = B, A

    left, right = 0, len(A)-1

    # Get the elements that would be in the left half of a merged and sorted A & B array
    # then use that to find the median of the "new array"
    while True:
        # Get the index value for the element in A that may be the
        # largest value from A in left half of the merged and sorted array
        i = (left+right)//2
        # Get the index value for the element in B that may be the largest
        # value from B in the left half of the merges and sorted array
        j = mid - i - 2

        # Get the array elements for the above indexes and the element on their right
        # to be used to check if the right elements have been picked as being in the left
        # half or the merged and sorted array
        leftA = A[i] if i >= 0 else float('-inf')
        rightA = A[i+1] if (i+1) < len(A) else float('inf')
        leftB = B[j] if j >= 0 else float('-inf')
        rightB = B[j+1] if (j+1) < len(B) else float('inf')

        # Check if the array has been partitioned correctly (the right elements
        # have been chosen for the left half of the merged and sorted array)
        if leftA <= rightB and leftB <= rightA:
            # Check if the total array size is an odd number
            if total % 2:
                # Return lessor number of the total array size is odd
                return min(rightA, rightB)
            # Calculate the median if the total array size is even
            return (max(leftA, leftB) + min(rightA, rightB)) / 2
        # Check if the largest number in the half of A is greater than the smallest
        # number outside the half of B (the largest number from the A half should be
        # less than or equal to the smallest number outside the B half and vice versa)
        elif leftA > rightB:
            # Reduce the value for the index of the largest value in all of A
            right = i - 1
        # Else rightB > leftA
        else:
            # Increase the value for the index of the largest value in all of B
            left = j+1

def main():
    nums1 = [1,2]
    nums2 = [3,4]
    print(findMedianSortedArrays(nums1, nums2))

    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))

if __name__ == '__main__':
    main()
