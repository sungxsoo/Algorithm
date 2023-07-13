def cycle_length(n):
    original_n = n
    cycle_len = 0

    while True:
        n = (n % 10) * 10 + ((n // 10 + n % 10) % 10)
        cycle_len += 1
        if n == original_n:
            return cycle_len

n = int(input())
print(cycle_length(n))