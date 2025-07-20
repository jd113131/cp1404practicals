"""
Programming project management task
Estimate: 50:00 minutes
Actual: 25:10 minutes
"""
import datetime

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
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter project file name: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter file to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_date = datetime.datetime.strptime(
                input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
            display_if_projects_starts_afterword(projects, filter_date)
        elif choice == "A":
            print("Let's add a new project")
            projects = add_new_project(projects)
            pass
        elif choice == "U":
            pass
        elif choice == "Q":
            pass
        # print(projects) # check if projects loaded
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as infile:
        infile.readline()  # read first heading line
        for line in infile:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = float(parts[4])
            projects.append(Project(*parts))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as outfile:
        # save first heading line
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name}"
                  f"\t{project.start_date}"
                  f"\t{project.priority}"
                  f"\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}"
                  , file=outfile)
    return


def display_projects(projects):
    """Display projects in two groups, completed and incomplete projects."""
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_complete():
            print(project)
    print("Completed projects: ")
    for project in projects:
        if project.is_complete():
            print(project)
    return

def display_if_projects_starts_afterword(projects, filter_date):
    print("Incomplete projects: ")
    for project in projects:
        if project.starts_after(filter_date):
            print(project)


def add_new_project(projects):
    """Add a new project to the list of projects."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = float(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects

main()
