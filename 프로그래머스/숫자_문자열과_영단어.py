def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in num:
            if i in s:
                s = s.replace(i, num.get(i))
                # print(s)
    return int(s)

# print(solution('zeroonezeroone2seven3three'))