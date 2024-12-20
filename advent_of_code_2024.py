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
            print(str(is_increasing))
            if is_increasing: 
                if line[j] - curr_int > 3 or line[j] - curr_int <= 0:
                    # print("increasing")
                    break 
            else:
                print("diff: " + str(line[j] - curr_int))
                if line[j] - curr_int < -3 or line[j] - curr_int >= 0:
                    # print("decreasing")
                    break 
            curr_int = line[j]
            i += 1

        if i == len(line) - 1: 
            res += 1 
            # print("res: " + str(res))
    

def main(): 
    #day_1_solution()
    day_2_solution()

if __name__ == "__main__":
    main()
