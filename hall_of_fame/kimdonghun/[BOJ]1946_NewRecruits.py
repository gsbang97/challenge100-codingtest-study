import sys

T = int(sys.stdin.readline())
applicant_list = []

for _ in range(T):
    N = int(sys.stdin.readline())

    applicant_list.extend(
        list(map(int, sys.stdin.readline().split())) for _ in range(N)
    )
    applicant_list.sort()
    #print(applicant_list)

    appointing_mem = 0

    cur_doc_ranking = N+1
    cur_interview_ranking = N+1

    for applicant in applicant_list:
        #print(applicant[0])
        #print(type(applicant[0]))

        doc_flag = False
        interview_flag = False

        if cur_doc_ranking >= applicant[0]:
            cur_doc_ranking = applicant[0]
            doc_flag = True
        if cur_interview_ranking >= applicant[1]:
            cur_interview_ranking = applicant[1]
            interview_flag = True

        if doc_flag or interview_flag:
            appointing_mem += 1

            #print(appointing_mem, cur_doc_ranking, cur_interview_ranking)

    print(appointing_mem)
    applicant_list.clear()
