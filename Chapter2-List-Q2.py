# Q) 리스트를 사용자로부터 입력받아서 역순으로 정렬하여 리스트의 원소를 출력하여라.
# 원소 수를 미리 묻지 말고 코드가 실행될 수 있도록하라.

numbers = list(map(int, input().split(' ')))

for n in range(len(numbers)//2):
    numbers[n], numbers[len(numbers) - n - 1] = numbers[len(numbers) - n - 1], numbers[n]

print(numbers)