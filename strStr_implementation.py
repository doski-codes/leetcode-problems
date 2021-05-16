'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''

def strStr(haystack, needle):
    # Return 0 if the needle is an empty string
    if needle == "":
        return 0

    hay = len(needle)

    # Loop from the beginning of the string to the point where a needle at the
    # end of the string can be detected
    for i in range(len(haystack)-hay+1):
        # If the substring from i is the needle return the index of the first
        # occurence of the needle
        if haystack[i:i+hay] == needle:
            return i

    # Return -1 if the needle was not found after looping through the string
    return -1

def main():
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))

if __name__ == '__main__':
    main()
