# Q5 Answer template
def solution(n, s):
    multi_set = []
    multiply = 1
    answer = [-1]
    for i in range(1, s//2 + 1):
        multi_set.append([i, s - i])
    for i in multi_set:
        if multiply < i[0] * i[1]:
            multiply = i[0] * i[1]
            answer = i
    return answer

n = 2
s = 8
answer = solution(n, s)
print(answer)