print("Здравствуй милый пользователь") # начало
name = input("Ведите свое имя") # салют
while True:
    act = input("Действие выбири: (+,-, *, /,):") #знаки калькулятора
    if act in('+', '-', '*', '/'): #знаки
        numder1=float(input("x= ")) #первый завет
        numder2=float(input("y= ")) #второй завет
        if act =='+': #действие сложение
            print("Ответ:", (numder1 + numder2)) #результат
        elif act == '-': #действие вычитание
            print("Ответ:", (numder1 - numder2)) #результат
        elif act == '*': #действие умножение
            print("Ответ:", (numder1 * numder2)) #результат
        elif act == '/': #действие деление
            print("Ответ:", (numder1 / numder2)) #результат