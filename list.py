friends=['pravs','keers','yashs','venns','sars']
print(friends[2])
friends.insert(2,"srees")              #insert
print(friends)
friends.append("srees")             #append
print(friends)
friends.pop(4)                 #pop
print(friends)
friends.remove("sars")               #remove
print(friends)
friends[2]='sravani'             #replace
print(friends)
count=1
for ele in friends:   
    print(count,ele)                #get number for each eleemt
    count+=1
for i in range(0,len(friends)):
    if i%2==0:                     #even
        print(friends[i])
for i in range(0,len(friends)):
    if i%2==0:
        rev=friends[i]
        print(rev[::-1])            #reverse
    else:
        print(friends[i])


