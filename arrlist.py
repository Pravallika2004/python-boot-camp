arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
first.extend(second)
print(first)

k=3
first=arr[k-1:]
second=arr[:k-1]
print(first+second)

k=3
first=arr[k+1:k-2:-1]
second=arr[:k-1]
print(first+second)

k=2
first==arr[k-1:]
first=first[::-1]
second=arr[:k-1]
print(first+second)



