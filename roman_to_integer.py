'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3

Example 2:

Input: s = "IV"
Output: 4

Example 3:

Input: s = "IX"
Output: 9

Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

# Two different approaches to the same problem

def romanToInt1(var):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    var = var.upper()

    # Loop from the last character to the one before the last character
    for i in range(len(var)-1, 0, -1):
        # Check if the roman numeral on the right is greater than the one on the left
        if (roman[var[i]] > roman[var[i-1]]):
            # Subtract two times the value of the lessor number
            # and add to the sum to arrive at the right conversion
            sum += roman[var[i]] - roman[var[i-1]]*2
        else:
            # Add the number to the sum
            sum += roman[var[i]]
    # Return the sum of the first numeral and the final sum
    return sum + roman[var[0]]

def romanToInt2(var):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    var = var.upper()

    # Loop from the first character to the one before the last character
    for i in range(len(var)-1):
        # Check if the roman numeral on the left is greater than the one on the right
        if (roman[var[i]] >= roman[var[i+1]]):
            # Add the number to the sum
            sum += roman[var[i]]
        else:
            # Subtract the number from the sum to maintain the right conversion
            sum -= roman[var[i]]

    # Return the sum of the last numeral and the final sum
    return sum + roman[var[len(var)-1]]

def main():
    print(romanToInt1('IX'))
    print(romanToInt2('IX'))

if __name__ == '__main__':
    main()
