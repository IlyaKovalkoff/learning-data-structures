#list make nodes not user(take only value)
#


class Node:
    def __init__(self, value = None):
        self.__value = value
        self.__next = None 
    
    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value
        
    def set_value(self, value):     #O(1)
        self.__value = value


class LinkedList():
    def __init__(self):
        self.__headvalue = None
        self.__talevalue = None

    def return_object(self):
        return self.__headvalue

    def __set_first_value(self, first_value):
        self.__headvalue = first_value
        self.__talevalue = first_value

    def push_back(self,object):
        if self.__headvalue is None:
            self.__set_first_value(object)
        self.__talevalue.set_next(object)
        self.__talevalue = object
      

    def printlist(self):
        value_for_print = self.__headvalue
        while value_for_print is not None:
           print (value_for_print.get_value())
           value_for_print = value_for_print.get_next()

    def access_by_index(self, index):
        node_iterator = self.__headvalue
        for i in range (index):
            if i == index - 1:
                print(node_iterator.get_value())
            else:
                node_iterator = node_iterator.get_next()

    def insert(self, index, value):
        node_iterator = self.__headvalue
        previous = None
        for i in range (index):
            previous = node_iterator
            node_iterator = node_iterator.get_next()
        
        value.set_next(node_iterator)
        previous.set_next(value)

    def remove(self, index):
        index += 1
        node_iterator = self.__headvalue
        for i in range (index):
            if i == index - 2:
                link_from = node_iterator
                node_iterator = node_iterator.get_next()
            elif i == index - 1:
                link_to = node_iterator.get_next()
                link_from.set_next(link_to)
                break
            else:
                node_iterator = node_iterator.get_next()


list = LinkedList()

list.push_back(Node("1"))

e2 = Node("2")
e3 = Node("3")
e4 = Node("4")
e5 = Node("5")       #**
e6 = Node("6")

e_in = Node('-+-')

list.push_back(e2)     
list.push_back(e3)       
list.push_back(e4)
list.push_back(e5)
list.push_back(e6)

list.insert(2, e_in)

#list.remove(3)

list.printlist()
