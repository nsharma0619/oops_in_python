class Employee():

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


    def PayInc(self):
        self.pay = int(self.pay * self.raise_amount)

class developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev_1 = developer("neeraj", "sharma", 50000, "python")


print(issubclass(developer, Employee))