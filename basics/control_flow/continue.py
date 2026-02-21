"""CONTINUE statement

@see: https://docs.python.org/3/tutorial/controlflow.html
"""

def  continue_statement():

    even_numbers = []

    rest_of_the_numbers = []

    for number in range(1, 10):
        if number % 2 == 0:
            even_numbers.append(number)
            continue

        rest_of_the_numbers.append(number)

    print(even_numbers)
    print(rest_of_the_numbers)

continue_statement()


