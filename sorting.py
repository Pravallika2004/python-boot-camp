# arr=[4,5,3,1,2]
# first=[0]
# last=len(arr)-1
# while first<last:
#     last=arr[first]
#     first=arr[last]
#     first+=1
#     last-=1

arr=[1,2,3,4,5]
k=6
count=0
f=0
l=len(arr)-1
while f<l:
    if arr[f]+arr[l]==k:
        print(f,l)
        count+=1
        f+=1
        l-=1
#also use elif
    elif arr[f]+arr[l]<k:
        f+=1
    else:
        l-=1
print(count)
    







