import sys

T = int(sys.stdin.readline())

for _ in range(T):
  P = sys.stdin.readline()
  N = int(sys.stdin.readline())
  strArr = sys.stdin.readline()
  arr = strArr[1 : len(strArr) - 2].split(',')
  a = 0
  b = N
  flag = True
  errorFlag = False
  for p in P:
    if p == 'D':
      if b == a:
        print("error")
        errorFlag = True
        break
      if flag:
        a += 1
      else:
        b -= 1
    elif p == 'R':
      flag = not flag
  if errorFlag:
    continue

  print("[", end="")
  if a != b:
    if flag:
      print(arr[a], end="")
      for p in arr[a + 1 : b]:
        print(f",{p}", end="")
    else:
      print(arr[b - 1], end="")
      for p in reversed(arr[a : b - 1]):
        print(f",{p}", end="")
  print("]")