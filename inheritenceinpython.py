class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    def bark(self):
        print('bark')
#we dont need pass comment bcz we define a method in dog class 

class Cat(Animal):
    pass


dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.walk()
