# 4 
#1 2 3 4 
t=int(input())
for tc in range(t):
    n=int(input())
    candies=list(map(int,input().split()))
    time,fcandies=0, candies[0]
    for i in range(1,len(candies)):
        fcandies+=candies[i]
        time+=fcandies
    print(time)
