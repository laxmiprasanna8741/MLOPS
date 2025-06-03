class Employe():
    def __init__(self):
        print("started")
        self.id = 1
        self.name = "sam"
        self.salary = 100000  
        print("ended")

    def travel(self,destination)  :
        print("travel")
        print(f"employee is traveling to {destination}")
sam = Employe()
sam.travel("kerala")
# print(sam.salary)