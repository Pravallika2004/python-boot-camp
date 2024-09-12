try:
    a=5
    print(b)
except NameError:
    print('variable b is not assigned')

try:
    arr=[1,7,8,12,36]
    print(arr[0])
except IndexError:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('finally wednesday is last day of traininng')


