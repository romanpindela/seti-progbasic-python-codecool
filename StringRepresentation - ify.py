print("type on original base")
original_base = int(input())

print ("type number in original base")
user_input = input().replace("[","").replace("]","").split(",")
input_numbers = list(map(int,user_input))

def to_String_Representation(list_of_numbers):
    result = ""
    for element in input_numbers:
        if element == 10:
            result += "A"
        elif element == 11:
            result += "B"
        elif element == 12:
            result += "C"
        elif element == 13:
            result += "D"
        elif element == 14:
            result += "E"
        elif element == 15:
            result += "F"
        else:
            result += str(element)
    return result

x = to_String_Representation(input_numbers)
print(x)


