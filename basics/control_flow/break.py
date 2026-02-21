

def break_statement():
    number_to_be_found = 42
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            break
        else:
            number_of_iterations += 1

    print(number_of_iterations)

break_statement()