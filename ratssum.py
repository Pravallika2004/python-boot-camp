s=list(map(int,input().split()))
r=7
unit=2
f=(r*unit)
sum=0
count=0
for i in s:
    sum+=i
    count+=1
    if sum>f:
        print(count) 
        break 

    

