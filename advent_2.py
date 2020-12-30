# https://adventofcode.com/2020/day/2
# Validate passwords from a list based on the conditions given with each password.
# Example: 3-4 j: tjjj
# Password must contain between 3 and 4 "j"s, password listed after colon.

with open('/Users/Becca/python_scripts/input.txt', 'r') as input_file:
    correct_passwords = 0 
    for line in input_file:
        line = line.replace(": ", " ").replace("-", " ") 
        # removes : and , replaces these with spaces
        line = line.split(" ")
        # splits at each space

        min = int(line[0])
        max = int(line[1])
        char = line[2]
        password = line[3]
        count = password.count(char)

        if min <= count <= max:
            correct_passwords += 1 

    print(correct_passwords)        


