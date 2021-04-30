'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 1221
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

Constraints:

-231 <= x <= 231 - 1
'''

def isPalindrome(x):
    num = 0

    # Return false if number is negative
    if (x < 0):
        return False

    # Divide number(x) into two halves then compare them
    while x > num:
        # Get last digit of x
        var = x % 10
        # Floor division to remove the last digit of x
        x = x // 10
        # Place the removed digit behind num
        num = (num * 10) + var

    # Check if the two halves(x, num) are equal
    # if the number doesn't have even number of digits
    # Check if the lesser number equals the floor division of the greater number
    if (x == num) or (x == (num // 10)):
        return True

def main():
    print(isPalindrome(121))

if __name__ == '__main__':
    main()
