class Employee :
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee) :
    def __init__ (self , name , salary , team_size) :
        super().__init__(name , salary)
        self.team_size = team_size

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Team size:", self.team_size)






e1 = Employee("Ali", 20000)
m1 = Manager("Sina", 40000, 5)

e1.show_info()
m1.show_info()