def solution(new_id):
    new_id = new_id.lower();

    answer = "".join(
        a
        for a in new_id
        if 'a' <= a <= 'z'
        or '0' <= a <= '9'
        or a == '-'
        or a == '_'
        or a == '.'
    )
    tmp = answer
    answer = ""
    prev_a = ''
    for a in tmp:
        if a == '.' and prev_a != '.' or a != '.':
            answer += a
        prev_a = a

    answer = answer.strip('.')

    if answer == "":
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip('.')

    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer