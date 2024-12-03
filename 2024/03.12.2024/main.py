# https://adventofcode.com/2024/day/3
import re
from typing import List


def load():
    linearr: List[str] = []
    with open("input.txt") as f:
        for line in f:
            linearr.append(line.strip())
    return linearr


def main():
    linearr = load()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # part 1
    first = list()
    for line in linearr:
        matches = re.findall(pattern, line)
        numbers = [int(a) * int(b) for a, b in matches]
        first.append(sum(numbers))
    print(sum(first))
    # part 2
    enabled = True
    result = 0
    control_pattern = r"(do\(\)|don't\(\))"
    for line in linearr:
        tokens = re.findall(f"{pattern}|{control_pattern}", line)
        for token in tokens:
            if token[2] == "do()":  # If the token is a "do()"
                enabled = True
            elif token[2] == "don't()":  # If the token is a "don't()"
                enabled = False
            elif token[0] and token[1]:  # If the token is a "mul(a, b)"
                if enabled:  # Only process mul instructions if enabled
                    a, b = int(token[0]), int(token[1])
                    result += a * b

    # Output the result
    print(result)


if __name__ == "__main__":
    main()
