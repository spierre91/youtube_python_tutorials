
def add_numbers(num1, num2):
    print(f'{num1} plus {num2} is', num1 +num2)
    return num1 + num2
#add_numbers(5, 7)
    
sum_value = add_numbers(10, 23)
print(sum_value)

def get_address(name, address):
    print(f'{name} lives at {address}')
    return f'{name} lives at {address}'


message = get_address('Bob', '10 Oak St.')

print("message: ", message)
