n=int(input())
s=0
c=0
while n!=0:
    s+=n%10
    n//=10
for i in range(1,s+1):
    if s%i==0:
        c+=1
if c==2:
    print("number is goggly")
else:
    print("number is not goggly")