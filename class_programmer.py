class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("saleh",2000000,"Piano")
print(p.company,p.name,p.salary,p.pin)