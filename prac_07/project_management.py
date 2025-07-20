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
            try:
                filter_date = datetime.datetime.strptime(
                    input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
                display_if_projects_starts_afterword(projects, filter_date)
            except ValueError:
                print("Invalid date")
        elif choice == "A":
            print("Let's add a new project")
            projects = add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MAIN_MENU)
        choice = input(">>> ").upper()

    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save == "yes":
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r", encoding="utf-8") as infile:
        infile.readline()  # read first heading line
        for line in infile:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            projects.append(Project(*parts))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as outfile:
        # save first heading line
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name}"
                  f"\t{project.start_date.strftime("%d/%m/%Y")}"
                  f"\t{project.priority}"
                  f"\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}"
                  , file=outfile)


def display_projects(projects):
    """Display projects in two groups, completed and incomplete projects."""
    projects.sort()
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_complete():
            print(project)
    print("Completed projects: ")
    for project in projects:
        if project.is_complete():
            print(project)


def display_if_projects_starts_afterword(projects, filter_date):
    """Display projects that start after a certain date."""
    print("Incomplete projects: ")
    for project in projects:
        if project.starts_after(filter_date):
            print(project)


def add_new_project(projects):
    """Add a new project to the list of projects."""
    name = get_valid_input("Name: ", str)

    while True:
        start_date = input("Enter start date (dd/mm/yy): ")
        try:
            datetime.datetime.strptime(start_date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date")

    priority = get_valid_input("Priority: ", int)
    cost_estimate = get_valid_input("Cost estimate: ", float)
    completion_percentage = get_valid_input("Completion percentage: ", int)
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def get_valid_input(question, input_type):
    """Get input from the user with error handling."""
    while True:
        try:
            return input_type(input(question))
        except ValueError:
            print("Invalid input")


def update_project(projects):
    """Update a project completion rate and priority in the list of projects."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project Choice: "))
    print(projects[project_choice])
    try:
        new_percentage = int(input("New Percentage: "))
        projects[project_choice].completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        projects[project_choice].priority = new_priority
    except ValueError:
        pass


main()
