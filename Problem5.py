import sys
import math


def calculate(a, b, c):
    # control+alt+l to clean code
    x = 2 * c/(-b + math.sqrt(b ** 2 - 4 * a * c))
    return x


def main():
    c = 3
    b = 2
    a = 1
    x = calculate(a, b, c)
    print(f"x={x}")


if __name__ == "__main__":
    sys.exit(main())
