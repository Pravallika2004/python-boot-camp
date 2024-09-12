s='a1b2c3d492nm45'
sum=''
alp=''
for i in s:
    if i.isdigit():
        sum+=i
    else:   
        alp+=i 
print(sum+alp)
