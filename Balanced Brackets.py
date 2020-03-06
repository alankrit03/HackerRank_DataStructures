def isBalanced(s):
    stack = []
    for ch in s:
        if ch == ']':
            if not stack:
                return 'NO'
            if stack[-1] != '[':
                return 'NO'
            stack.pop()
        elif ch == '}':
            if not stack:
                return 'NO'
            if stack[-1] != '{':
                return 'NO'
            stack.pop()
        elif ch == ')':
            if not stack:
                return 'NO'
            if stack[-1] != '(':
                return 'NO'
            stack.pop()
        else:
            stack.append(ch)
    if stack:
        return 'NO'
    else:
        return 'YES'

