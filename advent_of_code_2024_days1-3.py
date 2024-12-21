import re

#day 1: 
def day_1_solution(): 
    #reading and parsing txt file
    f = open("day_1.txt", "r")
    array1 = []
    array2 = []
    for line in f:
        result = line.strip().split("   ")
        array1.append(int(result[0]))
        array2.append(int(result[1]))
    array1.sort()
    array2.sort()

    res = 0
    for i in range(len(array1)): 
        res += abs(array1[i] - array2[i])
    print(str(res))
    #print(array1[i], array2[i]) for i in range(len(array2))] 

#day 2: 
def day_2_solution():
    f = open("day_2.txt", "r")
    
    list = []
    for line in f: 
        to_add = line.strip().split(" ")
        to_add_l = []
        for val in to_add: 
            to_add_l.append(int(val))
        list.append(to_add_l)

    res = 0 
    for line in list: 
        i = 0
        curr_int = line[0]
        is_increasing = False 
        # print(curr_int) 
        # print(line)
        if curr_int > line[len(line)-1]:
            is_increasing = False
        elif curr_int < line[len(line)-1]:
            is_increasing = True
        else: 
            continue

        for j in range(1, len(line)): 
            # print(str(is_increasing))
            if is_increasing: 
                if line[j] - curr_int > 3 or line[j] - curr_int <= 0:
                    # print("increasing")
                    break 
            else:
                # print("diff: " + str(line[j] - curr_int))
                if line[j] - curr_int < -3 or line[j] - curr_int >= 0:
                    # print("decreasing")
                    break 
            curr_int = line[j]
            i += 1

        if i == len(line) - 1: 
            res += 1 
            # print("res: " + str(res))
    print(str(res))
       
def day_2_part_2_solution(): 
    f = open("day_2.txt", "r")
    list = []
    for line in f: 
        to_add = line.strip().split(" ")
        to_add_l = []
        for val in to_add: 
            to_add_l.append(int(val))
        list.append(to_add_l)

    res = 0 
    for line in list: 
        # print(line)
        i = 0
        curr_int = line[0]
        is_increasing = find_increasing(line)
        bad_val = 0

        for j in range(1, len(line)): 
            new_val = line[j]
            # print("curr int: " + str(curr_int) + " new_val: " + str(new_val))
            # print("i is: " + str(i))
            if is_increasing: 
                if line[j] - curr_int > 3 or line[j] - curr_int <= 0:
                    bad_val += 1 
                    is_valid = None 
                    if curr_int > line[j] and j == 1: 
                        is_valid = check(line, is_increasing, 0)
                    else: 
                        is_valid = check(line, is_increasing, j)
                    if is_valid:
                        i += 1
                        continue
                    else:
                        break
            else:
                if line[j] - curr_int < -3 or line[j] - curr_int >= 0:
                    bad_val += 1 
                    is_valid = None 
                    if curr_int < line[j] and j == 1: 
                        is_valid = check(line, is_increasing, 0)
                    else: 
                        is_valid = check(line, is_increasing, j)
                    if is_valid: 
                        i += 1
                        continue
                    else: 
                        break
            curr_int = new_val
            i += 1
        # print(str(i) + " i and bad_val is " + str(bad_val))
        # print("i is: " + str(i) + " len is: " + str(len(line)))
        # print(str(bad_val))
        if i == len(line) - 1 and bad_val < 2: 
            res += 1 
        else: 
            print(str(line) + " isn't safe!")
    print(str(res))

def check(arr, is_increasing, remove_idx):
    # print("remove idx: " + str(remove_idx))
    # Checking if we ignore the invalid value, the levels are still valid or not
    prev = None
    for i in range(len(arr)):
        if i == remove_idx:
            continue
        if prev is not None:
            if is_increasing and (arr[i] - prev > 3 or arr[i] - prev <= 0):
                return False
            elif not is_increasing and (arr[i] - prev < -3 or arr[i] - prev >= 0):
                return False
        prev = arr[i]
    return True

def find_increasing(line): 
    # Calculate the trend based on differences between adjacent values
    increasing, decreasing = 0, 0
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        # print("Diff: " + str(diff) + " increasing: " + str(increasing) + " decreasing: " + str(decreasing))
        if diff > 0:
            increasing += 1
        elif diff < 0:
            decreasing += 1
    # print(increasing > decreasing)
    return increasing > decreasing

#day 3: 
def day_3_part_1_solution(): 
    f = open("day_3.txt", "r")

    input_string = ""
    for line in f: 
        input_string += line

    # The pattern will create tuples 
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    result = re.findall(pattern, input_string)
    print(type(result[0]))
    res = 0 
    for tup in result: 
        res += int(tup[0]) * int(tup[1])
    print(str(res))

def day_3_part_2_solution():
    f = open("day_3.txt", "r")

    input_string = ""
    for line in f: 
        input_string += line

    #New pattern with do() and don't() to parse 
    pattern = r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)'

    #Second pattern to extract integers from mul(x,y)
    mul_pattern_extractor = r'\d{1,3}'
    extracted_functions = re.findall(pattern, input_string)
    res = 0 
    is_do = True
    
    #iterating through the resulting list  
    for value in extracted_functions: 
        if value == "do()": 
            is_do = True
        elif value == "don't()":
            is_do = False
        else: #mul case
            if is_do: 
                multiplication_operands = re.findall(mul_pattern_extractor, value)
                res += int(multiplication_operands[0]) * int(multiplication_operands[1])
    print(res)

def main(): 
    #day_1_solution()
    #day_2_solution()
    # day_2_part_2_solution()
    # day_3_part_1_solution()
    day_3_part_2_solution()

if __name__ == "__main__":
    main()