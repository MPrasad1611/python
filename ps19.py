# class Calculator:
#     def __init__(self):
#         self.result=0
#     def add(self,a,b):
#         self.result=a+b
#         return self.result
#     def sub(self,a,b):
#         self.result=a-b
#         return self.result
#     def mul(self,a,b):
#         self.result=a*b
#         return self.result
#     def div(self,a,b):
#         self.result=a/b
#         return self.result
#     def mod(self,a,b):
#         self.result=a%b
#         return self.result
#     def fact(self,a):
#         self.result=1

# cal=Calculator()
# print(cal.add(10,20))
# print(cal.sub(10,20))
# print(cal.mul(10,20))
# print(cal.div(10,20))
# print(cal.mod(10,20))
# print(cal.fact(5))

class Human:
    gen="Male"
    def __init__(self,name1,age1):
        self.name=name1
        self.age=age1
    def display(self):
        print(self.name,self.age,self.gen)

    def learn(self):
        print(self.name,"I am learning")

human1=Human("Rahul",20)
human2=Human("Prasad",21)
print(human1.name,human1.age,human1.gen)
print(human2.name,human2.age,human2.gen)
human1.display()
human2.display()
human1.learn()
human2.learn()