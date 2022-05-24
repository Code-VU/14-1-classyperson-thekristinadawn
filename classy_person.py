'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name
        
    def increase_age(self): 
        self.age = self.age + 1
        print(self.age)

    def say_greeting(self):
        print("Hello world! My name is",self.name,"!")
    
    def __iter__(self):
        self.start = 1
        return self

 
    def count_to_age(self):
        for x in range(1,self.age):
            print(x)
      

kristina = Person(34, "Kristina")
print(kristina.age)
kristina.increase_age()
kristina.say_greeting()
kristina.count_to_age()



# You won't need to call anything here.