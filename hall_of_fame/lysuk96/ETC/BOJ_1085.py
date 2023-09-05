def solve(x, y, w, h):
    can1 = x if x < w / 2 else w - x
    can2 = y if y < h / 2 else h - y
    return min(can1, can2)

x, y, w, h = map(int, input().split())
print(solve(x,y,w,h))    

