from dateutil.parser import parse #import dateparser
from datetime import *

#class creation and attribute initialization
class Person:
    def __init__(self,name,sex,birth):
        self.name = name
        self.sex = sex
        self.birth = parse(birth).date()

#We expand the class definition by defining the following methods.

    #Getter method
    def getName(self):
        return self.name
    #Getter method
    def getBirth(self):
        return self.birth
    #isMan method
    def isMan(self):
        if self.sex == 'M':
            return True
        else:
            return False
    #isFemale method
    def isVrouw(self):
        if self.sex == 'V':
            return True
        else:
            return False
    #Age method
    def age(self):
        age = date.today() - self.birth
        year = timedelta(days=365)
        return age//year

class Student(Person):
    studnr_source = 1 #Class variable
    def __init__(self,name,sex,birth):
        super().__init__(name,sex,birth)
        self.studnr = Student.studnr_source
        Student.studnr_source += 1
        self.training = []
        
    
    #Methods
    def getStudent_number(self):
        return self.studnr

    def getTraining(self):
        return self.training
        
    def setTraining(self,a):
        self.training.append(a)   
    #Not working
    def removeTraining(self,d):
        for index,object in enumerate(self.training):
            if object == d:
                del self.training[index]
            else:
                print("Training not found")
    
    def followsTraining(self,e):
        if e in self.training:
            return True
        else:
            return False

s1 = Student("Denis", "M", "02-04-2000")
s2 = Student("Karima", "V", "15-12-2003")

print(s1.getStudent_number(),s1.getName(),s1.age())
print(s2.getStudent_number(),s2.getName(),s2.age())

s2.setTraining("Inf")
s2.setTraining("TWi")

print(s2.getName(),s2.followsTraining("ChT"))
print(s2.getName(),s2.followsTraining("Inf"))

# print(s2.getTraining())
s2.removeTraining('Inf')
# print(s2.getTraining())
print(s2.getName(),s2.followsTraining("Inf"))
# print(s2.getName(),s2.followsTraining("TWi"))

