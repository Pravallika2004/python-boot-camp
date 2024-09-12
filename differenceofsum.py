n=int(input())
m=int(input())
d=0
c=0
for i in range(1,n+1):
    if i%m==0:
        c+=i
    else:
        d+=i
print(abs(d-c))


