def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        l = []
        r = []

        for line in lines:
            parts = line.split()
            r.append(int(parts[1]))
            l.append(int(parts[0]))

        r.sort()
        l.sort()

        diff = 0

        for i in range(len(l)):
            diff += abs(l[i] - r[i])

        print(diff)
            
if __name__ == "__main__":
    main()
