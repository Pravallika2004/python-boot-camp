'''input1=5 4
input2=16352
'''
'''
size,k=list(map(int,input().split()))
hurdles=list(map(int,input().split()))
mpor=max(hurdles)-k
print(mpor)
if mpor <=0:
    print("0")
else:
    print(mpor)
    '''
#question:watermelon
'''
a=int(input())
if a % 2==0 and a>3:
    print("YES")
else:
    print("NO")
    '''
#candies
'''
input1=1--->no.of.testcases
input1:4--->no of boxes
input3=1234--->candies
'''
'''
b=int(input())
for tc in range(b):
    n=int(input())
    candies=list(map(int,input().split()))
    time,fcandies=0,candies[0]
    for i in range(1,len(candies)):
        fcandies+=candies[i]
        time+=fcandies
print(time)
'''
#ordered collection of data mutable(no change)--->list
#ordered collection of data immutable(change)---->tuple
#unordered collection  of data mutable---->set
#find the maximum maximum number of consecutive
'''
num=[1,1,0,1,1,1]
output:3
'''
'''
a=list(map(int,input().split()))
count,res=0,0
for i in range(len(a)):
    if a[i] == 0:
        count=0
    else:
        count+=1
        res=max(res,count)
print(res)
'''
#house problem
'''
input:{6,7,1,3,8,2,5}
output:20
'''
'''
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    if i%2==0:
        sum+=a[i]
print(sum)
'''
#to find the index--->+
#same problem sir answer
'''
def maxIndex(house):
    return house.index(max(house))
house=list(map(int,input().split()))
res=0
i=maxIndex(house)
while(house[i]!=0):
    res+=house[i]
    if(i==0):
        house[i],house[i+1]=0,0
    elif(i==len(house)-1):
        house[i],house[i-1]=0,0
    else:
        house[i],house[i+1],house[i-1]=0,0,0
    i=maxIndex(house)
print(res)
'''

























        
