class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, st):
        return self.marks + st.marks

s1 = student("Neeraj", 94)
s2 = student("TestUser", 55)

print(s1 + s2)