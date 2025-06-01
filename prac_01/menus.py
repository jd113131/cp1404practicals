"""
Menu
"""

name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ")
while choice != 'Q':
   if choice == 'H':
       print(f"hello {name}")
   elif choice == 'G':
       print(f"goodbye {name}")
   else:
       print("Invalid message")

   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")
   choice = input(">>> ")
print("Finished")