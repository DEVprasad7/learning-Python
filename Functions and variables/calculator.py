def calculate(n1, n2, op):
    if op == 1:
        result =  n1 + n2
    elif op == 2:
        result =  n1 - n2
    elif op == 3:
        result =  n1 * n2
    elif op == 4:
        result =  n1 / n2
    elif op == 5:
        result =  n1 ** n2
    else :
        raise ValueError('Invalid choice of operator')
    
    if result.is_integer():
        result = int(result)

    return result

    



    

continue_calculating = True
while continue_calculating is True:
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    print('Enter 1 for Addition')
    print('Enter 2 for Subtraction')
    print('Enter 3 for Multiplication')
    print('Enter 4 for Division')
    print('Enter 5 for Exponent')

    op = int(input('Enter your choice : '))

    result = calculate(num1, num2, op)
    print('=', result)
    yes_or_no = input('Would you like to continue (y/n): ')
    # if yes_or_no.is_str():
    #     raise ValueError('Invalid Syntax')
    if yes_or_no == 'n':
        continue_calculating = False