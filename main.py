price = 0
ticket = int(input("Введите количество билетов: "))
for ticket in range(ticket):
 try:
    age = int(input("Введите возраст участника конференции: "))
    if age > 100 or age <= 0:
       raise ValueError("Тебе не может быть столько лет")
 except ValueError as error:
    print(error)
    print("Неправильный возраст")
 else:
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif age >= 25:
        price += 1390
if ticket >= 3:
    price -= price/100*10
print(f"К оплате:", price)