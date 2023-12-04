# Advent of Code - 2023 - Day 1
file = open("/home/richard/Development/dev-richard/PY_AOC_2023/inputFiles/input_d1.txt")
num_array = []
sum = 0

# Process the input
for line in file:
    temp_num_arr = []
    for char in line:
        if char.isdecimal():
            temp_num_arr.append(char)
    count = len(temp_num_arr)
    temp_num = "0"
    if count > 3 or count > 1:
        temp_num = temp_num_arr[0] + temp_num_arr[count-1]
    elif count == 1:
        temp_num = temp_num_arr[0] + temp_num_arr[0]
    num_array.append(int(temp_num))

# Calculates the data
for i in num_array:
    sum += i
print(sum)