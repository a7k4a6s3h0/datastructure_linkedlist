class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        value = self.head

        while value:
            if value.next is None:
                node = Node(data, None)
                value.next = node
                break
            value = value.next

    def insertBased_on_index(self, data, index):
        i = 0
        value = self.head
        if value is None:
            self.insert_at_begin(data)
        while value:
            if i == index:
                node = Node(data, value.next)
                value.next = node
                break
            i += 1
            value = value.next

    def deleteBased_on_index(self, index):
        value = self.head
        if value is None:
            print("Your LinkedList is empty")
        elif index == 0:
            self.head = self.head.next
        i = 1
        while value:
            if i == index:
                value.next = value.next.next
                break
            i += 1
            value = value.next

    def DeletionionBased_on_values(self, user_given_data):
        value = self.head
        if value is None:
            print("Your LinkedList is empty")
        elif value.data == user_given_data:
            self.head = self.head.next
        while value:
            if value.next.data == user_given_data:
                value.next = value.next.next
                break
            value = value.next

    def Search_item(self, val):
        value = self.head
        if value is None:
            print("Your LinkedList is empty")
        i = 0
        while value:
            if value.data == val:
                print("searched value ", value.data, "index = ", i + 1)
                break

            i += 1
            value = value.next

    def converting_array_to_linkedList(self):
        list_item = []
        array_size = int(input("Enter the size of the array :"))
        print("Enter array values")
        for i in range(0, array_size):
            receiver = int(input())
            list_item.append(receiver)

        counter = 0
        while list_item:
            if counter != array_size:
                # Calling insert function and passing list values to linkedList. This function create a Node to Each
                # values in the array
                self.insert_at_begin(list_item[counter])
            else:
                break
            counter += 1

    def display(self):
        value = self.head
        collect_values = []

        while value:
            collect_values.append(value.data)
            value = value.next
        print(collect_values)


if __name__ == '__main__':
    ul = Linkedlist()
    ul.insert_at_begin(10)
    ul.insert_at_begin(50)
    ul.insert_at_begin(60)
    ul.insert_at_begin(90)
    ul.display()
    #ul.converting_array_to_linkedList()
    #ul.display()
    #ul.Search_item(20)
    #ul.DeletionionBased_on_values(10)
    #ul.display()
    #ul.deleteBased_on_index(2)
    #ul.display()
    # ul.insert_at_end(80)
    # ul.display()
    ul.insertBased_on_index(80, 3)
    ul.display()
