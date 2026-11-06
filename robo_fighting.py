
class ROBOT:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    def show(self):
        print("The robot name is", self.name)
        print("The robot health is", self.health)
        print("The robot energy is", self.energy)

    def attack(self, opponent):

        if self.health <= 0:
            print(self.name, "robot dead and cannot fight")

        elif opponent.health <= 0:
            print(opponent.name, "is already dead")

        elif self.energy >= 10:
            print(self.name, "attacks", opponent.name)

            self.energy -= 10
            self.health -= 10
            
        else:
            print(self.name, "doesnt have enough energy to fight")


robot1 = ROBOT("Yash", 100, 80)
robot2 = ROBOT("supernova56", 100, 80)

robot1.show()
print("----------------")

robot2.show()


robot1.attack(robot2)
robot1.show()
robot2.show()

print("----------------")

robot2.attack(robot1)
robot1.show()
robot2.show()

robot1.attack(robot2)
robot1.show()
robot2.show()

print("----------------")
robot1.attack(robot2)
robot1.show()
robot2.show()

print("----------------")

robot1.attack(robot2)
robot1.show()
robot2.show()

print("----------------")



robot2.attack(robot1)
robot1.show()
robot2.show()

print("----------------")

robot2.attack(robot1)
robot1.show()
robot2.show()

print("----------------")

robot2.attack(robot1)
robot1.show()
robot2.show()

print("----------------")

robot2.attack(robot1)
robot1.show()
robot2.show()

robot1.attack(robot2)

robot1.show
robot2.show