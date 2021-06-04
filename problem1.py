import sys


def main():
    print("What is your name?")
    name = input()
    print("Name:" + name)
    print("How old are you?")
    age = input()
    print('Age:' + age)
    x = "Maryanne"
    y = "28 years old"
    print(f"Her name is {x} and she is {y}")

if __name__ == "__main__":
    sys.exit(main())