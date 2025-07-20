"""
Programming project management task
Estimate: 50:00 minutes
Actual: 25:10 minutes
"""
from project import Project

FILENAME = "projects.txt"

MAIN_MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Create a menu in which uses can manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(MAIN_MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter project file name:")
            projects = load_projects(filename)
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
        # print(projects) # check if projects loaded
        choice = input(">>>").upper()

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as infile:
        infile.readline() # read first heading line
        for line in infile:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = float(parts[4])
            projects.append(Project(*parts))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


main()
