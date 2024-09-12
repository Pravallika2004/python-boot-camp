arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(arr)):
    if i%2==0:
        e.append(arr[i])
    else:
        o.append(arr[i]) 
e.sort()
o.sort()
print(e[-2])
print(o[1])
    



