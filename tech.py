class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
head=first
first.next=second
second.next=third
third.next=None
while head!=None:
    print(head.data)
    head=head.next