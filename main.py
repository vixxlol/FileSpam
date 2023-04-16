import os

print("Welcome! How many files do you want to spam?")
files = input("> ")
created = 0

try:
    files = int(files)
except ValueError:
    print("Invalid number.")
    exit()

if files < 1:
    print("You have to create 1 file at least.")
else:
    for i in range(files):
        with open(f"file{created}", 'w'):
            pass
        created += 1