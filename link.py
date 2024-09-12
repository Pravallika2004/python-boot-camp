arr=[1,2,3,4,5]
# hide 1 and do sum 14,hide2 and do sum 13 ,hide 3 and do sum 12,hide 4 and do sum11,hide 5 and do sum 10
# maximum sum:14 minimum sumis 10 difference
arr.sort()
min_sum=sum(arr[:len(arr)-1])
max_sum=sum(arr[1:])
diff=(abs(min_sum-max_sum))
print(diff)