from random import randint

print("Welcome to Arithmetic Practice!")
o = input("enter the operation you would like to practice (+, -, *, /): ")
q = int(input("how many questions do you want to do?: "))
d = int(input("how many digits minimum?: "))

for i in range(q):
    a = randint(10 ** (d - 1), 10 ** d)
    b = randint(10 ** (d - 1), 10 ** d)

    if o == "+" or o == "-":
        c = a + b
    else:
        c = a * b

    if o == "+" or o == "*":
        r = int(input(f"{a} {o} {b} = "))
        if r == c:
            print("correct!")
        else:
            print(f"incorrect, the correct response is {c}")
    else:
        r = int(input(f"{c} {o} {b} = "))
        if r == a:
            print("correct!")
        else:
            print(f"incorrect, the correct response is {a}")
