def digit(n):
    return(n-1)%9+1 if n>0 else 0
n=int(input())
print(digit(n))