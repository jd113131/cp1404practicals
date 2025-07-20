"""
Programming project management task
Estimate: 50:00 minutes
Actual: 25:10 minutes
"""

MAIN_MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Creat a menu in which uses can manage projects."""
    print("Welcome to Pythonic Project Management")
    ## TODO load projects
    print(MAIN_MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        elif choice == "Q":
            pass
        choice = input(">>>").upper()

main()
