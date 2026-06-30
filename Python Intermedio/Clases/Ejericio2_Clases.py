#Cree una clase de Bus con:
#Un atributo de max_passengers.
#Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.

class Person:

    def __init__(self, name):
        self.name = name


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self, person):

        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(person.name, "se subió al bus")
        else:
            print("BUS FULL")


    def remove_passenger(self, person):

        self.passengers.remove(person)
        print(person.name, "se bajó del bus")


person1 = Person("Laura")
person2 = Person("Felipe")
person3 = Person("Zeus")

bus1 = Bus(2)

bus1.add_passenger(person1)
bus1.add_passenger(person2)
bus1.add_passenger(person3)

bus1.remove_passenger(person1)