def MergeLists(headA, headB):
    if headA.data > headB.data:
        head = headB
        headB = headB.next
    else:
        head = headA
        headA = headA.next
    temp = head

    while True:

        if headA == None:
            temp.next = headB
            return head
        elif headB == None:
            temp.next = headA
            return head
        if headA.data >= headB.data:
            temp.next = headB
            headB = headB.next
        else:
            temp.next = headA
            headA = headA.next
        temp = temp.next
class ll:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    def add(self,val):
        temp = self
        while temp != None:
            if temp.next == None:
                temp.next = ll(val)
                return
            temp =temp.next

    def reverse(self):
        temp1 = self

        if temp1.next == None:
            return temp1
        temp2 =temp1.next
        if temp2.next == None:
            temp2.next = temp1
            temp1.next = None
            return temp2

        temp3 = temp2.next
        temp1.next = None
        while temp2 !=None:
            temp3 =temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
        return temp1
    def last_n(self,position):
        l = 0
        temp =self
        while temp != None:
            l+=1
            temp  =temp.next
        temp = self
        while temp != None:
            if l == position+1:
                return temp
            l-=1
            temp = temp.next

    def RemoveDuplicates(head):
        if head == None:
            return head
        temp1 = head
        while temp1.next != None:
            if temp1.data == temp1.next.data:
                temp1.next = temp1.next.next
            else:
                temp1 = temp1.next
        return head
    def traverse(self):
        temp =self
        while temp != None:
            print(temp.data,end=" ")
            temp=temp.next



t=ll(12)
t.add(12)
t.add(13)
t.add(13)
t.add(116)
t.add(116)
#t.traverse()

x=t.RemoveDuplicates()
x.traverse()
