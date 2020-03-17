stres = int(input("how stres? (numeral): "))
if stres < 10:
    print(stres * "a")
elif stres < 50:
    print(stres * "A")
else:
    print(10 * "a" + 15 * "A" + (stres - 25) * "Ã")
