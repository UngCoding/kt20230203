def solution(lottos, win_nums):
    max_cnt = 0
    min_cnt = 0
    for win_num in win_nums:
        if win_num in lottos:
            min_cnt += 1
            max_cnt += 1
        elif 0 in lottos:
            for i in range(6):
                if lottos[i] == 0:
                    lottos[i] = win_num
                    max_cnt += 1                
    answer = [rate(max_cnt), rate(min_cnt)]
    return answer

def rate(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)