'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

s = "([]){}"

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def isValid1(s):
    brackets = [('(', ')'), ('{', '}'), ('[', ']')]
    # Convert the string to a list with the individual string elements
    stack = list(s)
    # Set a key value to iterate through the list
    key = 0

    # Loop while the stack has elements and the key value for iterating
    # through the stack is less than the number of elements in the list
    while stack and (len(stack)-1 > key):
        # Check if there brackets are paired (open and closed)
        if (stack[key], stack[key+1]) in brackets:
            # Remove the brackets from the stack if they are paired
            stack.pop(key+1)
            stack.pop(key)
            # Reduce the value of the key by 1 if it's already greater than 0
            if key > 0: key -= 1
        else:
            # Increase the key by 1 if the brackets aren't paired
            key += 1

    # Return True if the stack is empty (all the brackets are paired)
    # and False otherwise
    return not stack

def isValid2(s):
    brackets = {")": "(", "}": "{", "]": "["}
    stack = []

    # Loop through all the elements in the string input
    for i in s:
        # Check if the element is a key in the dictionary
        if i in brackets:
            # Check if the stack has values
            if stack:
                # Get the last element from the stack if it's not empty
                end = stack.pop()
            else:
                # Assign 0 if the stack is empty
                end = 0

            # Check if the opening bracket (value of the element in the dictionary)
            # is the last element that was put in the stack
            if brackets[i] != end:
                return False
        else:
            # Add the element to the stack
            stack.append(i)

    # Return True if the stack is empty (all the brackets are paired)
    # and False otherwise
    return not stack

def main():
    s = "(){}}{"
    print(isValid1(s))
    print(isValid2(s))

if __name__ == '__main__':
    main()
