from random import randint
while True:
    try:
        user = int(input("Введіть число від 1 до 10 \n:"))
        break
    except ValueError:
        print("Не коректний ввід, тількі цілі числа!")

print(f"Число котре ти загадав: {user}")
num = randint(1,10)
num

print(f"Число що випало випадково: {num}")
if user == num:
  print("Вітаю! Ти вгадав число!")
if user > 10:
    print("Число більше заданного формату. Гра закінченна!")
else:
    if user < 1:
        print("Число меньше заданого формату. Гра закінченна!")
    else:
        if user > num:
            print("Твое число більше, ти програв, але був близько!")
        else:
            if user < num:
                print("Твое число меньше, ти програв, але був близько!")