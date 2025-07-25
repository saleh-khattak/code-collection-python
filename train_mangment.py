from random import randint
class  Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def bookTecket(self,fro,to):
        print(f"Your tecket is booked in Train number {self.trainNo} from {fro} to {to}")
    def fear(self,fro,to):
        print(f"The fear in Train number {self.trainNo} from {fro} to {to} is {randint(100,500)}")
    def getStatus(self):
        print(f"The train {self.trainNo} is going on time")

t=Train(20042)
t.fear("Peshawar","Lahore")
t.bookTecket("Peshawar","Lahore")
t.getStatus()