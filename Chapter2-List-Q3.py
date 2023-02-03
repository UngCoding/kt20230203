# Q) 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는 인덱스를 출력하라.
# 검색방안은 어떤 방안을 사용하여도 됩니다.

numbers = list(map(int, input().split(' ')))
number_find = int(input())

numbers.sort()
pl = 0
pr = len(numbers) - 1

while(True):
    pc = (pl + pr) // 2
    if numbers[pc] == number_find:
        print(pc)
        break
    elif numbers[pc] < number_find:
        pl = pc + 1
    else:
        pr = pc - 1
        
    if pl > pr:
        print(-1)
        break
