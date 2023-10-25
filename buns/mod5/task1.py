#task1
#-*- coding: utf-8 -*-
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

    def __str__(self):
        return str(self.data)


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека
        self.len = 0

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.len == 0:
            print("Стек пустой")
            return -1
        else:
            val = self.end
            self.end = self.end.pref
            self.len -= 1
            val.pref = None
            return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if isinstance(val, Node):
            if self.end is None:
                self.end = val
                self.len += 1
            else:
                x = self.end
                self.end = val
                self.end.pref = x
                self.len += 1
        else:
            print("Неверный тип данных")

    def print(self):
        """
        вывод на печать содержимого стека
        """
        if self.len == 0:
            print("Стек пустой")
        else:
            print(self.end)
            x = self.end.pref
            for i in range(self.len-1):
                print(x)
                x = x.pref

    def print_(self):
        """
        вывод на печать элементов стека с их узлами
        """
        if self.len == 0:
            print("Очередь пустая")
        else:
            print(self.end.pref, self.end)
            x = self.end.pref
            for i in range(self.len-1):
                print(x.pref, x)
                x = x.pref


newStack = Stack()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
newStack.print() #вывод о пустом стеке
newStack.pop() #вывод о пустом стеке
newStack.push(a)
newStack.push(b)
newStack.push(c)
newStack.push(d)
newStack.push(5) #вывод о неверном типе
newStack.push(e)
newStack.pop()
last = newStack.pop()
print()
newStack.print() #вывод стека
print()
newStack.print_() #вывод элементов стека с их узлами
print()
print(last.data, last.pref)
#вывод последнего убранного элемента и отсутствие его в стеке