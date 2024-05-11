class node:
      def __init__(self,data):
          self.data=data
          self.next=None
class Linked:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new
        self.next=None
    def pri(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
            

ep=Linked()

ep.insert(5)
ep.insert(6)
ep.insert(67)
ep.pri()
