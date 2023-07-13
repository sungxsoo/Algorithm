N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

# 방향 전환
def turn_left():
    global d
    d = (d + 3) % 4

# 초기 청소 영역 카운트
count = 1
board[r][c] = 2  # 청소한 위치는 2로 표시

while True:
    check = False
    for _ in range(4):
        turn_left()
        nx = r + dx[d]
        ny = c + dy[d]
        # 아직 청소하지 않은 경우
        if board[nx][ny] == 0:
            r = nx
            c = ny
            board[nx][ny] = 2  # 청소하고 표시
            count += 1
            check = True
            break
    # 모든 방향을 확인 후 청소할 곳이 없는 경우
    if not check:
        # 후진
        nx = r - dx[d]
        ny = c - dy[d]
        if board[nx][ny] == 1:  # 벽인 경우 종료
            break
        else:  # 빈 칸인 경우 위치 변경
            r = nx
            c = ny

print(count)
