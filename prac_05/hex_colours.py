"""Get colour and output the hexadecimal colour codes"""

COLOUR_TO_HEXADECIMAL_CODE = {
    "ABSOLUTE ZERO": "#0048ba",
    "ACID GREEN": "#b0bf1a",
    "ALICEBLUE": "#f0f8ff",
    "AQUA": "#00ffff",
    "BABY BLUE": "#89cff0",
    "BLACK": "#000000",
    "BLUE1": "#0000ff",
    "BROWN": "#a52a2a",
    "GREEN1": "#00ff00",
    "RED1": "#ff0000"
}

colour = input("Enter colour: ").upper()
while colour != '':
    try:
        print(f"The colour code for {colour} is {COLOUR_TO_HEXADECIMAL_CODE[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
