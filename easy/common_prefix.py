'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


def commonPrefix(strs):
    # Return an empty string if the list/array has no elements
    if len(strs) == 0:
        return ""
    else:
        # Get the length of the first string element in the list/array
        prefix_len = len(strs[0])
        # Loop through the elements in the list/array
        for i in range(len(strs)):
            # Check if the substring(prefix) is in the array element from the loop
            # If the substring(prefix) is not in the array element, reduce the
            # substring(prefix) by one letter
            while strs[0][:prefix_len] not in strs[i][:prefix_len]:
                # If the length of the substring(prefix) is less than 0 return an empty string
                # (That means the substring doesn't exit in the array elements)
                # Else reduce the length of the substring(prefix) by one letter
                if prefix_len < 0:
                    return ""
                else:
                    prefix_len -= 1

    return strs[0][:prefix_len]


def main():
    strs = ["dog","racecar","car"]
    print(commonPrefix(strs))

if __name__ == '__main__':
    main()
