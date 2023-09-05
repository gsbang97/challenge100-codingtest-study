import sys

while True:
    p_list = list(sys.stdin.readline()[:-1])
    if p_list == ["."]:
        break
    #print(p_list)

    s = []

    isValid = True
    for p in p_list:
        if p == "(":
            s.append("(")
        elif p == ")":
            if s:
                if s[-1] == "[":
                    isValid = False
                    continue
                s.pop()
            else:
                isValid = False
        elif p == "[":
            s.append("[")
        elif p == "]":
            if s:
                if s[-1] == "(":
                    isValid = False
                    continue
                pre = s[-1]
                s.pop()
            else:
                isValid = False

    if isValid and not s:
        print("yes")
    else:
        print("no")
            