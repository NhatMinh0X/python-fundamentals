def while_statement():
    number = 2
    power = 5

    result = 1
    while power > 0:
        result *= number
        power -= 1

    print(result)

while_statement()