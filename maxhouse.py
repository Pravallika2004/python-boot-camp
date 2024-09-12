def maxIndex(house):
    return house.index(max(house))
house=list(map(int,input().split()))
res=0
maxO=sum(house[1::2])
maxE=sum(house[1::2])
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
print(max(res,maxO,maxE))



