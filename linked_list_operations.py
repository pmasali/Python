class node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head=None

    def add(self, data):
        newnode = node(data, None)
        newnode.next = self.head
        self.head = newnode
        return

    def delete_list(self):
        while self.head:
            tmp = self.head
            self.head = tmp.next
            tmp = None
        print("list deleted!")

    def delete_node(self,data):

        if self.head == None:
            print("nothing to delete!")
            return

        itr = self.head

        if itr.data == data:
            self.head = itr.next
            itr = None
            print("found at head, deleted")
            return

        while itr:
            nxt = itr.next
            if nxt is not None:
                if nxt.data == data:
                    itr.next=nxt.next
                    nxt = None
                    print("node deleted!")
                    return
            itr = nxt

        print("node not found!")
        return

    def print_list(self):
        itr = self.head

        if itr == None:
            print("list empty!")
            return
        llst = ''
        while itr:
            llst = llst + str(itr.data) + "-->"
            itr = itr.next

        print(llst)



llist = linkedlist()
llist.delete_node(5)
llist.print_list()
llist.add(5)
llist.print_list()
llist.delete_node(5)
llist.add(10)
llist.print_list()
llist.add(15)
llist.print_list()
llist.add(20)
llist.print_list()
llist.add(25)
llist.print_list()
llist.delete_node(5)
llist.print_list()
llist.delete_list()


