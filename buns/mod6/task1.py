#-*- coding: utf-8 -*-
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Основной класс для листа
    """

    def __init__(self):
        self.start = None  # ссылка на начало листа
        self.end = None
        self.len = 0
        self.counter = 0
        self.current = self.start

    def __iter__(self):
        self.counter = 0
        self.current = self.start
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.len:
                raise StopIteration
            self.current = self.current.nref
        return self.current

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if isinstance(val, Node):
            if self.start is None:
                self.start = val
                self.end = val
                self.len += 1
            else:
                self.end.nref = val
                self.end = val
                self.len += 1
        else:
            print("Неверный тип данных")

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n - 1 == self.len:
            self.push(val)
        elif n - 1 == 0:
            val.nref = self.start
            self.start = val
            self.len += 1
        elif self.len >= n - 1 > 0:
            x = self.start
            for i in range(n - 2):
                x = x.nref
            y = x.nref
            x.nref, val.nref = val, y
            self.len += 1
        else:
            print("Нельзя вставить элемент за пределами очереди")

    def get(self, index):
        """
        получение элемента по индексу
        """
        if index + 1 > self.len or index + 1 <= 0:
            print("Элемента не существует")
        else:
            x = self.start
            for i in range(index):
                x = x.nref
            return x

    def remove(self, index):
        """
        удаление элемента по индексу
        """
        if index + 1 > self.len or index + 1 <= 0:
            print("Элемента не существует")
        else:
            if index == 0:
                x = self.start.nref
                self.start.nref = None
                self.start = x
                self.len -= 1
            else:
                x = self.start
                for i in range(index - 1):
                    x = x.nref
                y = x.nref.nref
                x.nref.nref = None
                x.nref = y
                self.len -= 1

    def print(self):
        """
        вывод на печать содержимого стека
        """
        if self.len == 0:
            print("Стек пустой")
        else:
            print(self.start, end=" ")
            x = self.start.nref
            for i in range(self.len-1):
                print(x, end=" ")
                x = x.nref
        print()

    def print_(self):
        """
        вывод на печать элементов листа с их узлами
        """
        if self.len == 0:
            print("Очередь пустая")
        else:
            print(self.start, self.start.nref)
            x = self.start.nref
            for i in range(self.len-1):
                print(x, x.nref)
                x = x.nref


newLinked = LinkedList()
newLinked.push(Node(1))
newLinked.push(Node(2))
newLinked.push(Node(3))
newLinked.push(Node(4))
newLinked.push(Node(5))
newLinked.push(Node(6))
newLinked.insert(5, Node(10))
newLinked.print()
print()
newLinked.remove(3)
newLinked.print()
print()
newLinked.print_()
print()
for item in newLinked:
    print(item, end=" ")
