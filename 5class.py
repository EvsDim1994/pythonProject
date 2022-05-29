import os

"""
x = (9, 9, 10) # картеж
y = 10, 88, 99, 1000 # картеж
print(type(x))
print(x)
print(x[0])
z, c, b = x # расспаковать по переменным



# картеж отличается от спика
# 1. картеж неизменяемый тип данных 2. быстрее итерируется


x = tuple("stroha")

print(x)

p = (1, 6, 121, 99)
o = (1, 2, 121, 99)
n = (1, 2, 121, 99)
#for i in range(len(n)):
 #   n[i] += 3


print(n)


#изменение картежа
t = list(x)
t[0] = 2222
x = tuple(t)

print(x)






# к картежу можно добавить значения

h = (1,2,4)
h += (4,7)
print(h)


#os.walk - метод для поиска файлов
"""
"""
print("before def")

def show(): # так опередялется функция

    print("fuction")

print("after def")

show()


# - запуск функции через переменную. y = show(). Но необходим возврат данныт через return
"""
spisok = []
for adress, dir, files in os.walk("venv"):
    spisok.append(adress)

print(spisok)

# ходит до папок


