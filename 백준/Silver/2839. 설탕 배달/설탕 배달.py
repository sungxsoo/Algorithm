N = int(input())

sugar = [5,3]

# 5a + 3b = N 를 만족할 때 a+b 의 최소 값을 구하시오

a = N // sugar[0]
N %= sugar[0]
b = 0

while a>=0:
    if N%3 == 0:
        b = N//3
        N %= 3
        break
    a -= 1
    N += 5

if N==0:
    print(a+b)
else:
    print(-1)
    
    