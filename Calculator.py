what = input("Оберіть операцію (+, -, /, *):")

a = float(input("Оберіть перше число:"))
b = float(input("Оберіть друге число:"))

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
elif what == "/":
    c = a / b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Рузультат:" + str(c))
else:
    print("Ведена неправельна операція")

