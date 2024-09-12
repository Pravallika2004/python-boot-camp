s='12344potddd'
count=0
for i in s:
    if(not(i.isdigit())):
        count+=1
print(count)