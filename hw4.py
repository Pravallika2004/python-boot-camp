s='abc'
k=2
li=[]
st=''
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        st+=s[i]+s[j]
        li.append(st)
        st=''
print(li)        