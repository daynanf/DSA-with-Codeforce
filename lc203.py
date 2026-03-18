class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
    def addelem(self,data):
        newNode=ListNode(data)
        n=self.head
        if self.head is None:
            self.head=newNode
        else:
            while n.next is not None:
                n=n.next
            n.next=newNode
    def removeE(self,data):
        if self.head is None:
            pass
            # return self.head
        else:
            
        # return self.head
    def printAll(self):
        if self.head is None:
            print("linked list is empyt")
        else:
            n=self.head
            while n is not None:
                print(n.val,end="-->")
                n=n.next
x=input("enter numbers").split()
ll=linkedlist()
for i in x:
    ll.addelem(int(i))
data=int(input("enter a data to remove from ll"))
print(f"ll before removing{data}")
ll.printAll()
ll.removeE(data)
print(f"ll after removing{data}")
ll.printAll()
