class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

hous1 = House('Бунино-парк', 45)
print(House.houses_history)
hous2 = House('Городские поляны', 35)
print(House.houses_history)
hous3 = House('Москва-сити', 94)
print(House.houses_history)

del hous2
del hous3

print(House.houses_history)
