import re

def p1(input):
    res = 0
    pattern = rf"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, input)
    for match in matches:
        res += (int(match[0]) * int(match[1]))
    return res

def p2(input):
    res = 0
    pattern = rf"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    enabled = True

    matches = re.findall(pattern, input)
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled and match.startswith("mul"):
            numbers = re.findall(r"\d+", match)
            res += int(numbers[0]) * int(numbers[1])
    return res

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read().replace("\n", "")
    print("p1:", p1(input))
    print("p2:", p2(input))