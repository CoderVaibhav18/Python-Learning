#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import random

comp_choice = random.randint(0, 2)
your_choice = int(input("Enter your choice 0 for 'snake', 1 for 'water' & 2 for 'gun': "))
choice = ["snake", "water", "gun"]

print(f"\n🧠 You choose: {choice[your_choice]}")
print(f"💻 Computer choose: {choice[comp_choice]}\n")

if your_choice == comp_choice:
  print(f"Game is tie, Bcoz your_choice: {choice[your_choice]}, comp_choice: {choice[comp_choice]}")
elif ((comp_choice == 0) and (your_choice == 1)) or ((comp_choice == 1) and (your_choice == 2)) or ((comp_choice == 2) and (your_choice == 0)):
  print("😔 Oh no! You lost the game. Better luck next time! 💡")
else:
   print("🎉 Congrats! You won the game! Great move! 💪")
  
