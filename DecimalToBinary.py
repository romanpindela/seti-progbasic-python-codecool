# print("Type a decimal")
userNumber = int(input("Type a decimal: "))

def decimal_to_binary(decimal_number):
    if decimal_number > 1:
        decimal_to_binary(decimal_number // 2)

    result.append(decimal_number % 2)

result = []
decimal_to_binary(userNumber)
print(result)

