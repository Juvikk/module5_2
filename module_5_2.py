class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(new_floor):
        if 0 < new_floor <= floors:
            for floor in range(1, new_floor ):
                print(floor)
        else:
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

def __len__(self):
    return ( self.number_of_floors)
def __str__(self):
    return (Название: {self.name}, кол-во этажей:{self.number_of_floors})