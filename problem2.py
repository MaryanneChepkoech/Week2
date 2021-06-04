import sys


def main():
    print("What is your name?")
    name = input()
    print("Name:" + name)
    print("How old are you?")
    age = input()
    print('Age:' + age)
    print("What year were you born?")
    birthdt= input()
    print("year:" + birthdt)
    w=birthdt
    #print(w)
    v = (int(w) + 77)
    #print(v)
    x = name
    y = age
    z = birthdt

    print(f"Her name is {x}", f"she is {y}" ,f"Born in {z}",f"She will be 77years old in {v}" ,sep=";")



if __name__=='__main__':
    sys.exit(main())