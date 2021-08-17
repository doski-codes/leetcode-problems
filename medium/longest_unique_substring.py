'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s):
    subStr = {}
    count = 0
    maxCount = 0
    pointer = 0

    for letter in range(len(s)):
        # While looping through the string check if there are any duplicated letters
        # in the dictionary. If there are remove the letter placed in the dictionary
        # according to the order in which they were placed and decrease the count
        while s[letter] in subStr.values():
            del subStr[pointer]
            # Increase pointer to remove letters in dicitonary from the left to
            # right of the string
            pointer += 1
            # Decrease the count of letters
            count -= 1

        # Add unique letters to the dictionary and increase the count
        subStr[letter] = s[letter]
        count += 1

        # Get the maximum count
        maxCount = max(count, maxCount)

    return maxCount

def main():
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))

if __name__ == '__main__':
    main()
