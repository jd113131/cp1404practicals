"""
Read and display wimbledon winner and their counties
Estimate: 20 minutes
Actual:   21:27 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    names_to_number_of_wins, countries_with_winners = read_file()
    display_winners(names_to_number_of_wins)
    display_countries_with_winners(countries_with_winners)


def read_file():
    names_to_number_of_wins = {}
    countries_with_winners = set()
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file) # skips the first heading line
        for line in in_file:
            country_of_winner, name_of_winner = line.split(",")[1:3]

            try:
                names_to_number_of_wins[name_of_winner] += 1
            except KeyError:
                names_to_number_of_wins[name_of_winner] = 1
            countries_with_winners.add(country_of_winner)

    return names_to_number_of_wins, countries_with_winners


def display_winners(names_to_number_of_wins):
    print("Wimbledon Champions: ")
    for winner, number_of_wins in names_to_number_of_wins.items():
        print(f"{winner} {number_of_wins}")


def display_countries_with_winners(countries_with_winners):
    print("")
    winning_countries = sorted(list(countries_with_winners))
    print(f"These {len(winning_countries)} countries have won Wimbledon: ")
    print(", ".join(winning_countries))


main()
