import random

characters = ["wizard", "dragon", "robot", "knight"]
places = ["forest", "castle", "space", "village"]

story = f"A {random.choice(characters)} appeared in a {random.choice(places)}."

print(story)
