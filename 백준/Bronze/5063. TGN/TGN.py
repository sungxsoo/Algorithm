import sys

N = int(sys.stdin.readline())

for i in range(N):
    a,b,c = map(int, input().split())
    if (b-c) == a:
        print('does not matter')
    elif (b-c) < a:
        print('do not advertise')
    else:
        print('advertise')
        
 

