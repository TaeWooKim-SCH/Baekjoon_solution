def solution(lottos, win_nums):
    answer = []
    win_num = []
    zero_count = lottos.count(0)
    for i in lottos:
        for x in win_nums:
            if i == x:
                win_num += [i]
    if len(win_num) == 6:
        answer += [1, 1]
    elif len(win_num) == 5:
        answer += [2 - zero_count, 2]
    elif len(win_num) == 4:
        answer += [3 - zero_count, 3]
    elif len(win_num) == 3:
        answer += [4 - zero_count, 4]
    elif len(win_num) == 2:
        answer += [5 - zero_count, 5]
    elif len(win_num) == 1:
        answer += [6 - zero_count, 6]
    if zero_count >= 1:
        if len(win_num) == 0:
            answer += [7- zero_count, 6]
    elif len(win_num) == 0:
            answer += [6, 6]
    print(answer)
    return(answer)