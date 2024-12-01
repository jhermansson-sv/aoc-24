def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        left = []
        right = []

        for line in lines:
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))

        sim_score = 0
        for value in right:
           occurence = left.count(value)
           sim_score += occurence * value
        
        print(sim_score)

if __name__ == "__main__":
    main()