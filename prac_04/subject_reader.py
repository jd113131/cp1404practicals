"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    # data does not need to be returned as its point can be used however task says to return to data
    subjects = load_subjects()
    display_subjects(subjects)


def display_subjects(subjects):
    for subject in subjects:
        print(f"{subject[0]} taught by {subject[1]} and has {subject[2]} students")


def load_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    file_data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        file_data.append(parts)
    input_file.close()
    return file_data


main()