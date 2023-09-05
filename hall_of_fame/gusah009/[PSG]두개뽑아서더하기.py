def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.extend(numbers[i] + numbers[j] for j in range(len(numbers)) if i != j)
    return sorted(set(answer))   