import sys

input = sys.stdin.readline

sen = input().rstrip()

while sen != ".":
    lst = list(sen)

    bra = []

    for st in lst:
        
        if (
            st not in ['[', '(']
            and st == ']'
            and bra
            and bra[-1] == '['
            or st not in ['[', '(']
            and st != ']'
            and st == ')'
            and bra
            and bra[-1] == '('
        ):
            bra.pop()
        elif st not in ['[', '('] and st == ']':
            bra.append(']')
            break
        elif st not in ['[', '('] and st == ')':
            bra.append(')')
            break

        elif st in ['[', '(']:
            bra.append(st)
    if not bra:
        print('yes')
    else:
        print('no')

    sen = input().rstrip()