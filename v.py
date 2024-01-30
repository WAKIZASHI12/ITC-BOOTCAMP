some = ("Bish", "Bishkek", "Bakyt", 29, 32, "Alpha")

letters = []
numbers = []

for i in some:
    if str(i).isdigit():
        numbers.append(i)

    elif str(i).isalpha():
        letters.append(i)
