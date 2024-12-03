import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.utils import parse_input

def safe(line):
    desc = True
    asc = True
    acceptable_diff = True

    for i in range(len(line) - 1):
        if line[i] > line[i + 1]:
            asc = False
        if line[i] < line[i + 1]:
            desc = False 
        if not 1 <= abs(line[i] - line[i + 1]) <= 3:
            acceptable_diff = False
    return (asc or desc) and acceptable_diff

def p1(input):
    res = 0
    for line in input:
        if safe(line):
            res += 1
    return res

def p2(input):
    res = 0
    for line in input:
        for i in range(len(line)):
            sub = line[:i] + line[i + 1:]
            if safe(sub):
                res += 1
                break
    return res  
    

if __name__ == "__main__":
    input = parse_input(24, 2)
    print("p1:", p1(input))
    print("p2:", p2(input))
