M = int(input())
val = [500,100,50,10,5,1]
count = 0
rest = 1000 - M

for v in val:
    count += rest // v
    rest %= v
    
print(count)