def solution(new_id):
    answer = ''

    # 1단계: 문자열의 모든 대문자를 대응되는 소문자로 바꿈
    new_id = new_id.lower() # 소문자로 바꿈
    # print(new_id)

    # 2단계: 문자열에서 알파벳 소문자, 숫자, -, _, .를 제외하고 다 제거
    new_id_rm = "abcdefghijklmnopqrstuvwxyz-_.0123456789"
    for i in new_id: # 특정 문자들 제거
        if (i in new_id_rm) == False: # i not in new_id_rm 도 가능.
            new_id = new_id.replace(i, "")
    # print(new_id)

    # 3단계: 문자열에서 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    new_id_2 = ""
    for x in new_id:
        new_id_2 += x
        if ".." in new_id_2:
            new_id_2 = new_id_2.replace("..", ".") # "."이 2번 이상 반복되면 "."으로 변환
    # print(new_id_2)

    # 4단계: 마침표가 문자열의 처음이나 끝에 위치하면 제거
    if new_id_2 != "": # 이것을 안해주면 빈 문자열이 들어갈 때 오류가 발생
        if new_id_2[0] == ".": # 문자열 처음에 "."이 들어왔을 때
            if new_id_2[-1] == ".":
                new_id_2 = new_id_2[1:]
                new_id_2 = new_id_2[:len(new_id_2) - 1]
            elif new_id_2[-1] != ".":
                # new_id_2 = new_id_2.replace(new_id_2[0], "", 1)
                new_id_2 = new_id_2[1:]        
        elif new_id_2[-1] == ".": # 문자열 끝에 "."이 들어왔을 때
            if new_id_2[0] == ".":
                new_id_2 = new_id_2[1:]
                new_id_2 = new_id_2[:len(new_id_2) - 1]
            elif new_id_2[0] != ".":
                # new_id_2 = new_id_2.replace(new_id_2[-1], "", 1)
                new_id_2 = new_id_2[:len(new_id_2) - 1]
    # print(new_id_2)

    # 5단계: 빈 문자열이 들어오면 a를 추가
    if new_id_2 == "": 
        new_id_2 += "a"
    # print(new_id_2)

    # 6단계: 문자열의 길이가 16자 이상이면, 문자열의 첫 15개를 제외하고 제거
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2.replace(new_id_2[15:], "")

        if new_id_2 != "": # 이것을 여기서도 추가를 안해주면 제거하고 난 후 마침표가 남게 되면 답이 틀려짐(4단계)
            if new_id_2[0] == ".": # 문자열 처음에 "."이 들어왔을 때
                if new_id_2[-1] == ".":
                    new_id_2 = new_id_2[1:]
                    new_id_2 = new_id_2[:len(new_id_2) - 1]
                elif new_id_2[-1] != ".":
                    # new_id_2 = new_id_2.replace(new_id_2[0], "", 1)
                    new_id_2 = new_id_2[1:]        
            elif new_id_2[-1] == ".": # 문자열 끝에 "."이 들어왔을 때
                if new_id_2[0] == ".":
                    new_id_2 = new_id_2[1:]
                    new_id_2 = new_id_2[:len(new_id_2) - 1]
                elif new_id_2[0] != ".":
                    # new_id_2 = new_id_2.replace(new_id_2[-1], "", 1)
                    new_id_2 = new_id_2[:len(new_id_2) - 1]
    # print(new_id_2)

    # 7단계: 문자열의 길이가 2자 이하라면, 문자열의 마지막 문자를 문자열의 길이가 3자가 될 때까지 반복함
    if len(new_id_2) <= 2:
        for j in range(3):
            new_id_2 += new_id_2[-1]
            if len(new_id_2) == 3:
                break
    return(new_id_2)


# 예제


solution("...!@BaT#*..y.abcdefghijklm")
solution("")
solution("woewinowegioewiofoirweoiroewinionwefoin")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
print(solution("abcdefghijklmn.p"))
print(solution(".aaaa.aaaa."))
print(solution(" "))









