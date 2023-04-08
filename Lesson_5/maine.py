userStart = int(input("userStart: "))
userStop = int(input("userStop: "))

summa = 0

for i in range(userStart, userStop+1):
    if userStart < userStop:
       print(i)
       summa += i
print("summa:", summa)