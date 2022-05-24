'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    
    def __init__(self) -> None:
        self.name = input("Enter name:")
        self.age = input("Enter age:")
        

    def display(self):
        print(self.name, self.age)

        
    def increase_age(self): 
        self.age = int(self.age) + 1  
        print(self.age)    

    def say_greeting(self):
        print("Hello world! My name is",self.name,"!")
    

    def count_to_age(self):
        for x in range(1,self.age):
            print(x)
      
person = Person()
person.increase_age()
person.say_greeting()
person.count_to_age()






    






# You won't need to call anything here.