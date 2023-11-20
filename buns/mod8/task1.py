class Transport():
    """Arguments: coordinates, speed, brand, year, number"""
    def __init__(self, coordinates: list, speed: int,
                 brand: str, year: int, number: int) -> None:
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    def __str__(self) -> str:
        '''
           Представление всей информации для вывода в методе print()
        '''
        return ("Координаты: {}, Скорость: {}, Марка: {}, Год: {}, Число: {}".
               format(self.coordinates, self.speed, self.brand, self.year, self.number))

    @property
    def coordinates(self) -> list:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: list) -> None:
        self._coordinates = coordinates

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, speed: int) -> None:
        self._speed = speed

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, brand: str) -> None:
        self._brand = brand

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        self._year = year

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number

    def isInArea(self, pos_x: float, pos_y: float, length: float, width: float) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        if (pos_x <= self.coordinates[0] <= pos_x + length and
            pos_y <= self.coordinates[1] <= pos_y + width):
            return True
        else:
            return False


class Passenger():
    """Arguments: passengers_capacity, number_of_passengers"""
    def __init__(self, passengers_capacity: int,
                 number_of_passengers: int) -> None:
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    def __str__(self) -> str:
        return ("Кол-во мест: {}, кол-во пассажиров: {}".
                format(self.__passengers_capacity, self.__number_of_passengers))

    @property
    def passengers_capacity(self) -> int:
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity: int) -> None:
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self) -> int:
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers: int) -> None:
        if number_of_passengers > self.__passengers_capacity:
            print("Количество пассажиров будет ограничено максимальной вместимостью")
            self.__number_of_passengers = self.__passengers_capacity
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo():
    """Arguments: carrying"""
    def __init__(self, carrying: bool) -> None:
        self._carrying = carrying

    def __str__(self) -> str:
        return ("Наличие груза: {}".format(self._carrying))

    @property
    def carrying(self) -> bool:
        return self._carrying

    @carrying.setter
    def carrying(self, carrying: bool) -> None:
        self._carrying = carrying


class Plane(Transport):
    """Arguments: height, coordinates, speed, brand, year, number"""
    def __init__(self, height: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._height = height

    def __str__(self) -> str:
        st = super().__str__()
        return ("{}, Высота: {}".format(st, self.height))

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height


class Auto(Transport):
    """Arguments: coordinates, speed, brand, year, number"""


class Ship(Transport):
    """Arguments: port, coordinates, speed, brand, year, number"""
    def __init__(self, port: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._port = port

    def __str__(self) -> str:
        st = super().__str__()
        return ("{}, Порт: {}".format(st, self.port))

    @property
    def port(self) -> str:
        return self._port

    @port.setter
    def port(self, port: str) -> None:
        self._port = port


class Car(Auto):
    """Arguments: coordinates, speed, brand, year, number"""


class Bus(Auto, Passenger):
    """Arguments: coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers"""

    def __init__(self, *args, **kwargs):
        Auto.__init__(self, *args[:5])
        Passenger.__init__(self, *args[5:], **kwargs)

    def __str__(self):
        return (Auto.__str__(self) + ", " + Passenger.__str__(self))


class CargoAuto(Auto, Cargo):
    """Arguments: coordinates, speed, brand, year, number, carrying"""

    def __init__(self, *args, **kwargs):
        Auto.__init__(self, *args[:5])
        Cargo.__init__(self, *args[5:], **kwargs)

    def __str__(self):
        return (Auto.__str__(self) + ", " + Cargo.__str__(self))


class Boat(Ship):
    """Arguments: port, coordinates, speed, brand, year, number"""


class PassengerShip(Ship, Passenger):
    """Arguments: port, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers"""
    def __init__(self, *args, **kwargs):
        Ship.__init__(self, *args[:6])
        Passenger.__init__(self, *args[6:], **kwargs)

    def __str__(self):
        return (Ship.__str__(self) + ", " + Passenger.__str__(self))


class CargoShip(Ship, Cargo):
    """Arguments: port, coordinates, speed, brand, year, number, carrying"""
    def __init__(self, *args, **kwargs):
        Ship.__init__(self, *args[:6])
        Cargo.__init__(self, *args[6:], **kwargs)

    def __str__(self):
        return (Ship.__str__(self) + ", " + Cargo.__str__(self))


class Seaplane(Plane, Ship):
    """Arguments: height, port, coordinates, speed, brand, year, number"""


def classprint(x):
    print("|", x.__class__.__name__, "|")
    print(x, end='\n\n')




a = Transport([5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(a)

b = Passenger(15, 10)
classprint(b)
print("Кол-во пассажиров 20")
b.number_of_passengers = 20
print(b, end='\n\n')

c = Cargo(True)
classprint(c)

d = Plane(1000, [5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(d)

e = Auto([5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(e)

f = Ship("№5", [5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(f)

g = Car([5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(g)

h = Bus([5.0, 10.0], 90, "Shipland", 1985, 2, 15, 10)
classprint(h)

i = CargoAuto([5.0, 10.0], 90, "Shipland", 1985, 2, True)
classprint(i)

j = Boat("№5", [5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(j)
print("{} находится в области, задающейся (pos_x: {}, pos_y: {}, length: {}, width: {}): {}".
      format(j.__class__.__name__, 0, 0, 10, 10, j.isInArea(0, 0, 10, 10)))
print()

k = PassengerShip("№5", [5.0, 10.0], 90, "Shipland", 1985, 2, 15, 10)
classprint(k)

l = CargoShip("№5", [5.0, 10.0], 90, "Shipland", 1985, 2, True)
classprint(l)

m = Seaplane(1000, "№5", [5.0, 10.0], 90, "Shipland", 1985, 2)
classprint(m)
print("{} находится в области, задающейся (pos_x: {}, pos_y: {}, length: {}, width: {}): {}".
      format(m.__class__.__name__, 0, 0, 10, 10, m.isInArea(0, 0, 10, 10)))
print("{} находится в области, задающейся (pos_x: {}, pos_y: {}, length: {}, width: {}): {}".
      format(m.__class__.__name__, 0, 0, 5, 5, m.isInArea(0, 0, 5, 5)))
