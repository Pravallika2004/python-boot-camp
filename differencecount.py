arr=list(map(int,input().split()))
num=13
diff=2
count=0
for i in arr:
    if abs(num-i)<=diff:
        count+=1
print(count)



    