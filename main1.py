class PartyAnimal:
    def __init__(self, name):
        self.name = name
        self.x = 0

    def party(self):
        self.x += 1
        print(f"{self.name} is partying! Party count: {self.x}")

class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)  # Call the parent class's __init__ method
        self.points = 0

    def touchdown(self):
        self.points += 7
        self.party()  # Call the party method from the parent class
        print(f"{self.name} scored a touchdown! Points: {self.points}")

# Example usage
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()