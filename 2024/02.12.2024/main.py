import os
from typing import List


def load(filename):
    a = list()
    with open(filename, "r") as file:
        for line in file.readlines():
            a.append([int(item) for item in line.split()])
    return a


def safe(line):
    tmplist = line
    tmplist_len = len(tmplist)
    tmplistduplen = len(list(set(tmplist)))
    if tmplist_len != tmplistduplen:
        return "Unsafe"
    else:
        match tmplist:
            case _ if all(
                1 <= int(tmplist[i + 1]) - int(tmplist[i]) <= 3
                for i in range(len(tmplist) - 1)
            ):
                return "Safe"
            case _ if all(
                1 <= int(tmplist[i]) - int(tmplist[i + 1]) <= 3
                for i in range(len(tmplist) - 1)
            ):
                return "Safe"


def main():
    filename = os.path.join(os.path.dirname(__file__), "input.txt")
    arr = load(filename)
    first: List[str] = []
    for i in range(len(arr)):
        first.append(safe(arr[i]))
    sumfirst = 0
    # part 1
    for i in first:
        if i == "Safe":
            sumfirst += 1
    print(sumfirst)
    # part 2
    sumsecond = 0
    for i in range(len(arr)):
        if first[i] == "Safe":
            sumsecond += 1
        else:
            for k in range(len(arr[i])):
                if safe(arr[i][:k] + arr[i][k + 1 :]) == "Safe":
                    sumsecond += 1
                    break
    print(sumsecond)


if __name__ == "__main__":
    main()
