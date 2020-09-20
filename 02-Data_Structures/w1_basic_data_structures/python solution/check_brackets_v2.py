# python3

'''Approach: Stack'''
  # Each time, when an open parentheses is encountered push it in the stack, and when closed parenthesis is encountered, match it with the top of stack and pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced.
  # LIFO principle: Last-In First-Out

from collections import namedtuple

open_char = ["[", "{", "("]
close_char = ["]", "}", ")"]


# Function to check parentheses
def check(text):
    stack = []
    for i in text:
        if i in open_char:
            stack.append(i)
        elif i in close_char:
            pos = close_char.index(i)
            if (len(stack) > 0) and (open_char[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == "__main__":
    string_1 = "{[]{()}}"
    print(string_1, "-", check(string_1))

    string_2 = "[{}{})(]"
    print(string_2, "-", check(string_2))

    string_3 = "((()"
    print(string_3, "-",check(string_3))
