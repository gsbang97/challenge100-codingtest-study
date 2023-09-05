def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    array = [[0 for _ in range(1000)] for _ in range(1000)]
    i = 0
    id_dict = {id: index for index, id in enumerate(id_list)}
    for declaration in report:
        a, b = declaration.split()
        array[id_dict[b]][id_dict[a]] = 1

    report_num = []
    for index, _ in enumerate(id_list):
        result = sum(array[index][index2] for index2, _ in enumerate(id_list))
        if result >= k:
            for index2, _  in enumerate(id_list):
                if array[index][index2] == 1:
                    answer[index2] += 1

    # print(report_num)
    return answer