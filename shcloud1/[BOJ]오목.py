from os.path import join
#오목판 그려주는 draw 함수
def draw(a):
    for row in a:
        print(' '.join(row))

#grid 함수
def grid(a,b):
    return [['-' for _ in range(a)] for _ in range(b)]

#오목판 크기 n
n = 3
grid = [['-' for _ in range(n)] for _ in range(n)]
dr = draw(grid)
round = 0
status = 'playing'
while status == 'playing':
    player = 'X' if round % 2 == 0 else 'O'
    print(f"{player}의 턴입니다.")
    row = int(input(f"행 번호를 선택하세요 (1-{n}): "))
    col = int(input(f"열 번호를 선택하세요 (1-{n}): "))
    print("\n====================================\n")
    grid[row-1][col-1] = player
    draw(grid)
    round += 1
    #끝나는 조건: 가로세로줄 또는 대각선 줄
    a = list(np.diag(grid))
    b = list(np.diag(grid).T)
    c = list(np.repeat(player,n))
    for i in range(n):
        if grid[i][:] != c and grid[:][i] != c:
            if a != c and b != c:
                continue
        #while문 끝내기위한 상태 설정
        status = 'end'
        print(f"{player}가 이겼습니다!")
        break