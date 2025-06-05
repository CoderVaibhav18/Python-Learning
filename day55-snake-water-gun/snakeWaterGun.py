#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import random

your_choice = int(input("Enter your choice 0 for 'snake', 1 for 'water' & 2 for 'gun': "))
comp_choice = random.randint(0, 2)
choice = ["snake", "water", "gun"]

if your_choice == comp_choice:
  print(f"Game is tie, Bcoz your_choice: {choice[your_choice]}, comp_choice: {choice[comp_choice]}")
elif ``: