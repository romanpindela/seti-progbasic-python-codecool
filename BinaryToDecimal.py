user_input = input("Type a binary set: ")

input_numbers = []
for i in user_input:
    if i.isdigit():
        input_numbers.append(int(i))

def binary_to_decimal(list_of_digits):
    result = 0
    n = 0
    for i in reversed(list_of_digits):
        result += i * 2 ** n
        n+=1
    return result

x = binary_to_decimal(input_numbers)
print(x)