"""Generate MENU to determine score and display stars for each point"""

MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Generate a menu that gets the users score and can display
    stars for each point scored and determine there result"""
    score = get_score()

    print(MENU)
    choice = input("Enter your choice: ")

    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            diaplay_starts(score)
        else:
            print("invalid input")
        print(MENU)
        choice = input("Enter your choice: ")

    print("Finished")

def get_score():
    """Gets the users to input a score and validates it"""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("invalid input")
        score = int(input("Enter your score: "))
    return score

def determine_result(score):
    """Returns the result based on the score"""
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    return "Invalid score"

def diaplay_starts(score):
    """displays 1 start every point scored"""
    print('*' * score)

main()
