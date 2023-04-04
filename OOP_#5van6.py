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

class Docent(Person):
    def __init__(self,name,sex,birth,salary=0):
        super().__init__(name,sex,birth)
        self.salary = salary
    
    #setter method salary
    def setSalary(self,a):
        self.salary = a

    #getter method salary
    def getSalary(self):
        return self.salary
    
    #increase salary
    def increaseSalary(self,increase):
        self.salary = int(self.salary * (1+increase/100))

if __name__ == '__main__':
    teacher1 = Docent("Marcela","V", "25-12-1993")

    print(teacher1.getName(),teacher1.age(),teacher1.isVrouw(), teacher1.getSalary())
    
    #We set salary to 2500/month
    teacher1.setSalary(2500)

    #We print salary
    print(teacher1.getSalary())

    #We now increase salary by 5%
    teacher1.increaseSalary(5)

    #We print the newly increased salary
    print(teacher1.getSalary())