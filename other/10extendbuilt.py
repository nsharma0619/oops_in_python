class text(str):
    def double(self):
        return self+self

t = text("hello")

print(t.double())