import sys

inputStr = sys.stdin.readline().rstrip()

stack = []
while len(inputStr) != 1 or inputStr[0] !='.':
    for s in inputStr:
        if (
            s not in ['(', '[']
            and s == ')'
            and stack
            and stack[-1] == '('
            or s not in ['(', '[']
            and s != ')'
            and s == ']'
            and stack
            and stack[-1] == '['
        ):
            stack.pop()
        elif (
            s not in ['(', '[']
            and s == ')'
            or s not in ['(', '[']
            and s == ']'
        ):
            stack.append('e')
            break
        elif s in ['(', '[']:
            stack.append(s)
    if stack:
        print("no")
    else:
        print("yes")
    inputStr = sys.stdin.readline().rstrip()
    stack.clear()