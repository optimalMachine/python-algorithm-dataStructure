#linked-list example

#the Node class
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val

    def insert(self,data):
        new_node = Node(data)
        