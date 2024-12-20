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

def main(): 
    day_1_solution()

if __name__ == "__main__":
    main()
