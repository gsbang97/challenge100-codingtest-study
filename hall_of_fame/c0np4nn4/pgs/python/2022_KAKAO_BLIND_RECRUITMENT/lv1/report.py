def solution(id_list, report, k):
    report_cnt = {}
    mail_cnt = {}

    for id in id_list:
        report_cnt[id] = 0
        mail_cnt[id] = 0

    report_log = {r: False for r in report}
    for r in report:
        if report_log[r] == True:
            continue
        id = r.split(" ")[0]
        b = r.split(" ")[1]

        if id == b:
            continue

        report_cnt[b] += 1
        report_log[r] = True

    report_log = {r: False for r in report}
    for r in report:
        if report_log[r] == True:
            continue
        id = r.split(" ")[0]
        bad = r.split(" ")[1]

        if id == bad:
            continue

        if report_cnt[bad] >= k:
            mail_cnt[id] += 1
        report_log[r] = True

    return [mail_cnt[id] for id in id_list]

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3


print(solution(id_list, report, k))
