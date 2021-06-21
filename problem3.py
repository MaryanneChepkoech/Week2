import sys


def main():
    a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Curabitur rhovus tincidunt sem nec gravida."
    print(len(a))
    b = a.count('it',0,99)
    print(b)
    print(a.lower())
    c = a.replace('i','*')
    print(c)
if __name__ =="__main__":
    sys.exit(main())