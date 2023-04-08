mss = []
user = 0
while user != "end":
    user = input()
    mss.append(user)

numbers = [int(x) for x in mss if x.isdigit()]
total = sum(numbers)

print("Введенные значения:", mss)
print("Сумма чисел:", total)
