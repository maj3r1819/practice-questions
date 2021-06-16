"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

def isValid(s):
    count1, count2 = 0, 0
    for i in s:
        if i =="(" or i == "[" or i == "{":
            count1+=1
        else:
            count2+=1
    print(count1, count2)


s = "{[]}"
isValid(s)

"""
Not COmplete
"""
