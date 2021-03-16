input_dict = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "a", 12: "b", 13: "c", 14: "d", 15: "e", 16: "f"}

result_list = []

for i in [1, 2, 14, 5, 15, 2, 13, 11, 5, 7, 8]:
    result_list.append(input_dict[i])

print("".join(result_list))
