import os
from collections import Counter


def loadfile(filename):
    arra = list()
    arrn = list()
    with open(filename, "r") as file:
        for line in file:
            arra.append(int(line.split()[0]))
            arrn.append(int(line.split()[1]))
    return arra, arrn


def main():
    dist = list()
    filename = os.path.join(os.path.dirname(__file__), "input.txt")
    arra, arrb = loadfile(filename)
    arra.sort()
    arrb.sort()
    # part 1
    for i in range(len(arra)):
        dist.append(abs(arra[i] - arrb[i]))
    print(sum(dist))

    # part 2
    count = Counter(arrb)
    print(sum(arra[i] * count[arra[i]] for i in range(len(arra))))


if __name__ == "__main__":
    main()
