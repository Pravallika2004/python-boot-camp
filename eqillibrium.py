n=int(input())
a=list(map(int,input().split()))
l=[]
r=[]
f=0
for i in range(len(a)):
    l=a[0:i]
    r=a[i+1:]
    if sum(l)==sum(r):
        f=1
        print(i+1)
        break
if f==0:
    print("not found")
