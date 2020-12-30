with open('/Users/Becca/python_scripts/input.txt', 'r') as input_file:
    correct_passwords = 0 
    for line in input_file:
        line = line.replace(": ", " ").replace("-", " ")
        line = line.split(" ")

        pos_x = int(line[0])
        pos_y = int(line[1])

        char = line[2]
        password = line[3]

        first_char = password[(pos_x - 1)]
        second_char = password[(pos_y - 1)]

        if first_char == char or second_char == char:
            if first_char != second_char:
                correct_passwords += 1
    
    print(correct_passwords)

