#task2
#-*- coding: utf-8 -*-
class Node:
    """
    # Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел

    def __str__(self):
        return str(self.data)


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди
        self.len = 0

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.len == 0:
            print("Очередь пустая")
            return -1
        else:
            val = self.start
            self.start = self.start.nref
            self.start.pref = None
            self.len -= 1
            val.nref = None
            return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if isinstance(val, Node):
            if self.start is None:
                self.start = val
                self.end = val
                self.len += 1
            elif self.len == 1:
                self.start.nref = val
                self.end = val
                self.end.pref = self.start
                self.len += 1
            else:
                self.end.nref = val
                x = self.end
                self.end = val
                self.end.pref = x
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
            self.start.pref = val
            x = self.start
            self.start = val
            self.start.nref = x
            self.len += 1
        elif self.len >= n-1 > 0:
            x = self.start
            for i in range(n-2):
                x = x.nref
            y = x.nref
            val.pref, val.nref = x, y
            x.nref, y.pref = val, val
            self.len += 1
        else:
            print("Нельзя вставить элемент за пределами очереди")

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        if self.len == 0:
            print("Очередь пустая")
        else:
            print(self.end, end=' ')
            x = self.end.pref
            for i in range(self.len-1):
                print(x, end=' ')
                x = x.pref
            print()

    def print_(self):
        """
        вывод на печать элементов очереди с их узлами
        """
        if self.len == 0:
            print("Очередь пустая")
        else:
            print(self.start.pref, self.start, self.start.nref)
            x = self.start.nref
            for i in range(self.len-1):
                print(x.pref, x, x.nref)
                x = x.nref


newQueue = Queue()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
newQueue.print() #вывод о пустом стеке
newQueue.pop() #вывод о пустом стеке
newQueue.push(a)
newQueue.push(b)
newQueue.push(c)
newQueue.push(d)
newQueue.push(5) #вывод о неверном типе
newQueue.push(e)
newQueue.pop()
last = newQueue.pop()
print()
newQueue.insert(3,Node(10))
newQueue.print() #вывод стека
print()
newQueue.print_() #вывод элементов очереди с их узлами
print()
print(last.pref, last.data, last.nref)
#вывод последнего убранного элемента и отсутствие его в очереди