## Q1) 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하여라.
prime = set(range(3,1001,2))
prime.add(2)

for n in range(3,1001,2):
    if n in prime:
        prime -= set(range(2*n,1001,n))
        
print(prime)