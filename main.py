# Завдання
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову

class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data 
        self.prev = prev    
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def append(self, data):
        new_node = Node(data)
        if not self.contains(data):
            if self.head == None:
                self.head = new_node
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node
        else:
            print("value already exists")
    
    def remove(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    return True
            current = current.next 
        return False
    
    def show_list(self, reverse=False):
        if not reverse:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
        else:
            current = self.head
            while current.next:
                current = current.next
                
            while current:
                print(current.data, end=" ")
                current = current.prev
            print()
    
    def replace(self, old_value, new_value, isEach=False):
        current = self.head
        is_found = False
        if not isEach:
            while current:
                if current.data == old_value:
                    current.data = new_value
                    return True
                current = current.next
            return False
        else:
            while current:
                if current.data == old_value:
                    current.data = new_value
                    is_found = True
                current = current.next
            if is_found:
                return True
            else:
                return False


        



my_lst = DoublyLinkedList()
nums = input("Enter strings separated by space: ").split()
for num in nums:
    my_lst.append(int(num))


while True:
    choice = int(input("""
1. Add element
2. Replace element
3. Check element
4. Remove element
5. Display elements
0. Exit                                                                                                                   
"""))
    
    match choice:
        case 0:
            break
        case 1:
            elem = int(input("Enter element: "))
            my_lst.append(elem)
        case 2:
            is_each = int(input("replace one - 1, replace each - 2"))
            elem = int(input("Enter elem to replace: "))
            elem_repl = int(input("Enter new elem: "))
            if is_each == 1:
                my_lst.replace(elem, elem_repl)
            elif is_each == 2:
                my_lst.replace(elem, elem_repl, isEach=True)
        case 3:
            elem = int(input("Enter elem to check: "))
            print(my_lst.contains(elem))
        case 4:
            elem = int(input("Enter elem to remove: "))
            my_lst.remove(elem)
        case 5:
            while True:
                isReverse = int(input("reverse? 1-yes 2-no"))
                if isReverse == 1:
                    my_lst.show_list(reverse=True)
                    break
                elif isReverse == 2:
                    my_lst.show_list()
                    break
                else:
                    print("incorrect action")
        case _:
            print("Incorrect action")