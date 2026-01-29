import random

health = 50

easy = 1
medium = 2
hard = 3

difficulty = hard

health_potion = int(random.randint(25, 50) / difficulty)

health += health_potion

print(health)
