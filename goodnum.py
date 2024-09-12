
# print(math.cbrt(35))
# print(math.ceil(math.cbrt(35)))
# print(math.floor(math.cbrt(35)))
# print(math.floor(35**.3)) as we r finding cube we use 3
import math
arr=[35,9,1]
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**.3)
    while low<high:
        res=low**3+high**3
        if res==ele:
            count+=1
        if res<ele:
            low+=1
        else:
            high-=1
print('the count is:',count)