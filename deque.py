from collections import deque
numbers=[1,2,3,4] #deque is used for deleting adding from left or right accordingly
numbers=deque(numbers)
numbers.pop()
print(numbers)
numbers.popleft()
print(numbers)