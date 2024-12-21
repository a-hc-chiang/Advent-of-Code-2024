import time 
import math

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

def main(): 
    #day_1_solution()
    #day_2_solution()
    day_2_part_2_solution()

if __name__ == "__main__":
    main()
