class Employee:

    num_of_emp = 0
    raise_amount = 1.04  # class variables

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        Employee.num_of_emp+=1

    @property
    def FullName(self):
        return "{} {}".format(self.fname, self.lname)

    @FullName.setter
    def FullName(self, name):
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname
        
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)


emp_1 = Employee("Neeraj", "Sharma", 50000)

emp_1.FullName = "Test User"

print(emp_1.email)