
class Node:
    def __init__(self, value = None):
        self.__value = value
        self.__next = None
        self.__previous = None 
          
    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def get_previous(self):
        return self.__previous

    def set_previous(self,value):
        self.__previous = value

    def set_next(self, value):
        self.__next = value
        
    def set_value(self, value):     #O(1)
        self.__value = value


class LinkedList():
    def __init__(self):
        self.__headvalue = None
        self.__tailvalue = None

    def __getitem__(self, key):
        return self.access_by_index(key)

    def __setitem__ (self, index, value):
        self.replace(index, value)

    def __set_first_value(self, first_value):
        self.__headvalue = first_value
        self.__tailvalue = first_value

    def replace(self, index, value):
        current = self.__headvalue
        for i in range(index):
            current = current.get_next()
        current.set_value(value)
        

    def push_back(self,value):
        new_node = Node(value)
        if self.__headvalue is None:
            self.__set_first_value(new_node)
        else:
            self.__tailvalue.set_next(new_node)
            new_node.set_previous(self.__tailvalue)
            self.__tailvalue = new_node
      
    def printlist(self):
        value_for_print = self.__headvalue
        while value_for_print is not None:
           print (value_for_print.get_value())
           value_for_print = value_for_print.get_next()

    def access_by_index(self, index):
        node_iterator = self.__headvalue
        for i in range (index):
            node_iterator = node_iterator.get_next()
        return node_iterator.get_value()

    def insert(self, index, value):
        new_node = Node(value)
        node_iterator = self.__headvalue
        previous = new_node
        for i in range (index):
            previous = node_iterator
            node_iterator = node_iterator.get_next() 
        new_node.set_next(node_iterator)
        node_iterator.set_previous(new_node)
        if index == 0:
            self.__headvalue = new_node
        else:
            new_node.set_previous(previous)
            previous.set_next(new_node)
            
    def remove(self, index):
        current = self.__headvalue
        previous = None
        for i in range (index): 
            previous = current
            current = current.get_next()
        if index == 0:
            self.__headvalue = current.get_next()
            self.__headvalue.set_previous(None) 
        else:
            previous.set_next(current.get_next())
            current.get_next().set_previous(previous)

    def find_node(self, value):
        count = 0
        node_iterator = self.__headvalue
        result = None
        while node_iterator:
            if node_iterator.get_value() == value:
                result = node_iterator
                break
            node_iterator = node_iterator.get_next()
            count += 1
        return count, result

    def rfind_node(self, value):
        count = 0
        node_iterator = self.__tailvalue
        result = None
        while node_iterator:
            if node_iterator.get_value() == value:
                result = node_iterator
                break
            node_iterator = node_iterator.get_previous()
            count += 1
        
        
        return count, result



list = LinkedList()

list.push_back("1")
list.push_back("2")    
list.push_back("3")       
list.push_back("4")
list.push_back("5")
list.push_back("6")

#list.insert(0, '6')

#list.remove(2)
#list.rfind_node('4')




list[1] = 'dwdwdwdw'
list.printlist()


#print(list[2])