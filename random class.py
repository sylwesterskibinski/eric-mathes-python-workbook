from random import randint

class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)
    
die = Die()

results = []

for _ in range(1,10):
    result = die.roll_die()
    results.append(result)
    
print(results)

die20 = Die(sides = 20)

for _ in range(1,10):
    result = die20.roll_die()
    results.append(result)

print(results)