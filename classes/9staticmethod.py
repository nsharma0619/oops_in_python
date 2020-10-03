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
        self.pay = int(self.pay * self.raise_amount)  # we have to use variables using either classes or instances
        # self.pay = int(self.pay * Employee.raise_amount)

    @classmethod # also called alternative constructor
    def from_string(cls, string):
        fname, lname, pay = string.split("-")
        return cls(fname, lname, pay)

    @staticmethod 
    def isweekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
mydate = datetime.date(2016,7,10)
print(Employee.isweekend(mydate))