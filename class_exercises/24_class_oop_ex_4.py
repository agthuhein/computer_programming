class Car:
    def __init__(self, make, model, year):
        self. make = make
        self.model = model
        self.year = year


    def description(self):
        print(f"{self.year}\n{self.make}\n{self.model}")


c1 = Car("Toyota", "Wish", 2023)
c1.description()