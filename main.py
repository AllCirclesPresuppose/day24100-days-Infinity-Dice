import random

print("Infinity Dice 🎲")


def rollDice(sides):
  rand = random.randint(1, sides)
  print("You rolled ", rand)


again = "yes"

while again == "yes" or again == "y":
  howMany = int(input("how many sides?: "))
  rollDice(howMany)
  again = input("Roll again? ")
