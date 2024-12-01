def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        right = []
        left = []

        for line in lines:
            parts = line.split()
            right.append(int(parts[1]))
            left.append(int(parts[0]))

        right.sort()
        left.sort()

        diff = 0

        for i in range(len(left)):
            diff += abs(left[i] - right[i])

        print(diff)
            
if __name__ == "__main__":
    main()
