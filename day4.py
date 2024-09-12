s='1c0c1c1a0b1'
res=int(s[0])      #a&,b|,c^
for i in range(1,len(s),2):
    if s[i]=='a':
        res=res&int(s[i+1])
    elif s[i]=='b':
        res=res|int(s[i+1])
    else:
        res=res^int(s[i+1])
print(res)


    

    