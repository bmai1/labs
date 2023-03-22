def main():
    file = input("Enter filename: ")
    with open(file) as f:
        # number of test cases
        n = f.readline()
        for i in range(int(n)):
            line = f.readline().split()
            if len(line) != 2:
                print("Need two words in each line")
                break
            if len(line[0]) != len(line[1]):
                print("Words not same length")
                break
            print("Distances: ", end = '')
            for i, c in enumerate(line[0]):
                if ord(c) == ord(line[1][i]):
                    print(0, end = ' ')
                # Y > X, normal distance
                elif ord(c) < ord(line[1][i]):
                    print(ord(line[1][i]) - ord(c), end = ' ')
                # X > Y, distance = (Y + 26) - X
                else:
                    print(ord(line[1][i]) + 26 - ord(c), end = ' ')
            print()


if __name__ == "__main__":
    main()