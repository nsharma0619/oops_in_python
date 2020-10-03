class Test:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def show(self):
        print(self.__c)

t = Test()

t.show()

#similarly for private methods

