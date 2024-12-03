def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        l = []
        r = []

        for line in lines:
            parts = line.split()
            l.append(int(parts[0]))
            r.append(int(parts[1]))

        sim_score = 0
        for value in r:
           occurence = l.count(value)
           sim_score += occurence * value
        
        print(sim_score)

if __name__ == "__main__":
    main()