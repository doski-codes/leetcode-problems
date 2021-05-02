'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

Constraints:

-231 <= x <= 231 - 1
'''

def reverse(x):
    num = 0
    signed = False

    if x == 0:
        return True

    # Check if a number is signed(negative) and convert it to a positive number
    if x < 0:
        x = x * -1
        signed = True

    while x:
        # Get the last digit in x
        value = x % 10
        # Floor division by 10 to get remove the last digit from x
        x = x // 10
        # Add value to the end of num
        num = (num * 10) + value

    if signed:
        return num * -1
    else:
        return num

def main():
    print(reverse(123))

if __name__ == '__main__':
    main()
