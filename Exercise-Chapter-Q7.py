# Q7 Answer Template

def solution(arr):
    answer = [arr[0]]

    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
  

    return answer

#arr = [1,1,3,3,0,0,1,1]
arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)