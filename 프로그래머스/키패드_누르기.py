def solution(numbers, hand):
    answer = ''
    key_pad = ['1', '2', '3', 
               '4', '5', '6', 
               '7', '8', '9', 
               '*', '0', '#']
    left_loc = 0
    right_loc = 0
    # 왼손잡이, 오른손잡이 확인
    if hand == 'left':
        for i in numbers:
            if (i == 1) or (i == 4) or (i == 7):
                left_loc = 0
                answer += 'L'
                left_loc += i
            elif (i == 3) or (i == 6) or (i == 9):
                right_loc = 0
                answer += 'R'
                right_loc += i
            elif (i == 2):
                
                
                


    elif hand == 'right':

    return answer