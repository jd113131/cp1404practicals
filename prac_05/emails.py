"""
Email and name storer
Estimate: 14:54 minutes
Actual:
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    name = ' '.join(email.split("@")[0].split(".")).title()

    response = input(f"Is your name {name}? (Y/n)")
    if not response in "Yy ":
        name = input("Name: ")

    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
