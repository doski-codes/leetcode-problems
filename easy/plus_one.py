'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''

def plusOne(digits):
    size = len(digits)
    rem = 1

    # Loop through array from the last element to the first
    for idx in reversed(range(size)):
        # Add 1 to the element from the array for the first run then the carry value
        # for the subsequent iterations
        num = digits[idx]
        # Let the new value of the element in the array be a number between 0 & 9
        # after adding the remainder
        digits[idx] = (digits[idx] + rem) % 10
        rem = (num + rem) // 10

    # Insert the remainder into the beginning of the array if the remainder after
    # the loop is greater than 0 (the largest value possible for rem is 1)
    if rem: digits.insert(0, rem)

    return digits

def main():
    digits = [1,2,3]
    print(plusOne(digits))

if __name__ == '__main__':
    main()
