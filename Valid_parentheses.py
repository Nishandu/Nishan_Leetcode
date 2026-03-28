def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping:   # closing bracket
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)  # opening bracket

    return not stack


# Test
print(isValid("()[]{}"))   
print(isValid("(]"))       
print(isValid("([)]"))     
print(isValid("{[]}"))     