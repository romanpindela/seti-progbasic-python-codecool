print("type on original base")
original_base = int(input())
max_base = 16
if (original_base > max_base):
    raise ValueError(f"Base number must be smaller than {max_base}, your number was {original_base}")

print ("type number in original base")
user_input = input().replace("[","").replace("]","").split(",")
input_numbers = list(map(int,user_input))

def to_String_Representation(list_of_numbers):
    input_dict = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    result_list = []
    for i in list_of_numbers:
        if i > max_base:
            raise ValueError(f"Each number must be smaller than {max_base}. Your number was too big: {i}")
        result_list.append(input_dict[i])
    return("".join(result_list))

result2 = to_String_Representation(input_numbers)
print(result2)


