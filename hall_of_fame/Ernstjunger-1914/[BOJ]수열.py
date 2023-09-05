import sys

def main():
  input=sys.stdin.readline
  n, k=map(int, input().split())
  li=list(map(int, input().split()))

  res = [sum(li[:k])]
  res.extend(res[i]-li[i]+li[k+i] for i in range(n-k))
  print(max(res))
  
if __name__=='__main__':
  main()