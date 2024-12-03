import os

def parse_input(year: int, day: int) -> list[list[int]]:

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, os.pardir, f"Y{year}/Day{day}/input.txt")
    
    parsed_lines = []

    with open (file_path, 'r') as f:
        for line in f:
            numbers = [int(x) for x in line.split() if x.isdigit()]
            parsed_lines.append(numbers)
        return parsed_lines
