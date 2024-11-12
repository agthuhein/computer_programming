class Vechicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"
    

class Car(Vechicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year


    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Motorcycle(Vechicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


c1 = Car("Toyota", "Wish", 2023)
print(c1.get_info())

m1 = Motorcycle("Honda", "NT1100" , 2024)
print(m1.get_info())