#consecutive ones
#far pointer dlow pointer
#n=[1,1,0,1,1,1]
#count=0
 #   if n[s]=
 #   count+=1
blist=list(map(int,input().split()))
count,res=0,0
for i in range(len(blist)):
    if(blist[i]==0):
        count=0
    else:
        count+=1
        res=max(res,count)
print(res)

