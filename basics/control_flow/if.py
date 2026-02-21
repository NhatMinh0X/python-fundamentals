"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

"""

def if_statement():
    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    print(conclusion)

if_statement()