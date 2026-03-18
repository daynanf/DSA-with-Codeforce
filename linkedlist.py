class Node:
   def __init__(self, data=None, next=None):
      self.data=data
      self.next=next
class Linkedlist:
   def __init__(self):
      self.head=None
   def addElementAtEnd(self,data):
      newElement=Node(data)
      if self.head is None:
         self.head=newElement
      else:
         n=self.head
         while(n is not None):
            n=n.next
         n=newElement
   def printAll(self):
      n=self.head
      if self.head is None:
         print("ll is empty")
      else:
         while(n is not None):
            print(n.data,end="-->")
ll = Linkedlist()
