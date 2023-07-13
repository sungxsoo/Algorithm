def calc_difference(A, B):
    return sum([a != b for a, b in zip(A, B)])

A, B = input().split()
differences = []

# i번째부터 A의 길이만큼 B의 문자열을 슬라이싱하고 그 문자열과 A 사이의 차이를 계산
for i in range(len(B) - len(A) + 1):
    sliced_B = B[i : i+len(A)]
    diff = calc_difference(A, sliced_B)
    differences.append(diff)

# 계산한 차이 중 최솟값을 출력
print(min(differences))
