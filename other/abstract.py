from abc import ABC, abstractmethod

class person(ABC):
    @abstractmethod
    def testmethod():
        pass

class student(person):
    def testmethod():
        print("hello")

s = student()

