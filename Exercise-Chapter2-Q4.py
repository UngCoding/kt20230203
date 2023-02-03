# Q4 Answer Template

def solution(arr):
    max_n = 1
    answer = 0
    
    
    for i in arr:
        max_n *= i
    
    for i in range(max(arr),max_n+1):
        cnt = 1
        for j in arr:
            if i % j:
                break
            elif cnt != len(arr):
                cnt += 1
            elif cnt == len(arr):
                answer = i
        if answer:
            break
        else:
            continue 
                
    return answer

arr = [None]*15
arr = [2,4,6,8]
answer = solution(arr)
print(answer)