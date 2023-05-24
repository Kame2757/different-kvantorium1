name = str(input("Введите имя\n"))
bith_year = int(input("Ваш год рождения?\n"))
current_year = 2022
if(bith_year == 2007):
    print("Вам 15 лет")
if((current_year - bith_year) > 14):
    print("Ваш возраст: ", current_year - bith_year)
elif((current_year - bith_year) == 14):
    print(name, "\nВаш возраст: ", current_year - bith_year)
else:
    print(name)


#Задача 3
a = input()
c = a.istitle()
if c == True:
    b = a.upper()
    print(b)
else:
    print(a)
b = a.replace('в', 'ё')
print(b)
с = len(a)
if с >= 10:
    b = a.split('Ё')
    b = a.replace('ё', ' ')
else:
    b = a.zfill(10) 
print(b)
#Задача 4
name = input()
lastname = input()
age = int(input())
tel = int(input())
resultFirstSting, resultSecondSting = "*",  "*"
lenName, lenLastName = len(name), len(lastname)
resultFirstSting1 = resultFirstSting.zfill(100).replace("0", "*")
resultSecondSting1 = resultSecondSting.zfill(100).replace("0", "*")
if lenName < 100 and lenLastName < 100:
    numName, numLastName = (100 - lenName) // 2, (100 - lenLastName) // 2
    numName1, numLastName1 = int(numName - 1), int(numLastName - 1)
    numName2, numLastName2 = int(numName * (-1)), int(numLastName * (-1))
    a = resultFirstSting1[numName2:numName1].replace('*', name)
    c = resultSecondSting1[numLastName2:numLastName1].replace('*', lastname)
    print(a)
    print(c)
else:
    print(name)
    print(lastname)