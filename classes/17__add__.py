# explain with real world example of strings, int 

class Employee:

    num_of_emp = 0
    raise_amount = 1.04  # class variables

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.email = first+last+"@gmail.com"
        self.pay = pay
        Employee.num_of_emp+=1


    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)


    def __add__(self, emp):
        if(isinstance(emp, Employee)):
            return self.pay+emp.pay
        return NotImplemented

dev_1 = Employee("neeraj", "sharma", 50000)
dev_2 = Employee("Test", "User", 60000)

print(dev_1+dev_2)