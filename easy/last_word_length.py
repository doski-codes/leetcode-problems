'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5

Explanation: The words are "Hello" and "World", both of length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4

Explanation: The longest word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6

Explanation: The longest word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

def lengthOfLastWord(s):
    lastSum = None
    runSum = 0

    for letter in s:
        # If the element from the loop is a space make runSum 0 (stop the count)
        # Then continue the loop from the next element
        if letter == " ":
            runSum = 0
            continue

        # Increment runSum by one if the element from the loop is a letter
        runSum += 1

        # Assign runSum to lastSum so that we can have the value for the length
        # of the last word at the end of the loop
        lastSum = runSum

    return lastSum

def main():
    s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s))

if __name__ == '__main__':
    main()
