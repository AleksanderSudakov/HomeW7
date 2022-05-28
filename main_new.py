# Примає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.
import math


def lencir(r):

    try:
        return 2 * math.pi * r
    except TypeError:
        print("Некорректный тип параметра")

r = 10

print(f"Довжина кола з радіусом {r} = {lencir(r)}")

r = "10"

print(f"Довжина кола з радіусом {r} = {lencir(r)}")


# Примає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.

def sqcir(r):

    try:
        return 2 * math.pi * (r ** 2)

    except TypeError:
        print("Некорректный тип параметра")

r = 10

print(f"Площа кола з радіусом {r} = {sqcir(r)}")

r = "10"

print(f"Площа кола з радіусом {r} = {sqcir(r)}")

# Приймає число, повертає чи є число поліндромом. Тобто з права на ліво і з ліва на право читається однаково. 12321 - це поліндром, 1234 - не поліндром.

n = int(input())
copy = n
r = 0

while(n!=0):

    k = n % 10
    r = r * 10 + k
    n = int(n/10)

if(r == copy):
    print("Палиндром")
else:
    print("Не палиндром")

# Функція приймає число n яке більше 0. За допомогою рекурсії виводить всі числа що менші n але більші 0.

def betw(n):

    if n == 1:
        print(n)
        return 1
    print(n)
    return betw(n-1)

n = int(input())

betw(n-1)

# Написати функцію lambda що приймає x i y, а повертає x^2 + y^2

print((lambda x, y: x ** 2 + y ** 2)(3, 4))

# Написати функцію lambda що приймає слово і повертає його довжину.

print((lambda x: len(x))("12345"))

# Написати map що перетворює всі числа в списку на строку.

lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: str(x), lst)))

# Написати filter що залишає в списку тільки числа > 10

def morethan10(n):
    return n > 10

lst = [10, 2, 30, 4, 15]

lst = list(filter(morethan10, lst))

print(lst)

# Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd ) (2 способи з lambda і без ) ( підказка: викорисати метот replace )

def rep(n):
    return n.replace('a', '')

lst = ["asdasdgfa", "fgdagsdf", "nlaaalaa"]

lst = list(map(lambda n: n.replace('a', ''), lst))

print(lst)

lst = ["asdasdgfa", "fgdagsdf", "nlaaalaa"]

lst = list(map(rep, lst))

print(lst)

# Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4. (2 способи з lambda і без )

def morethan4(n):
    return len(n) > 4

lst = ["333", "55555", "1", "666666", "22"]

lst = list(filter(morethan4, lst))

print(lst)

lst = ["333", "55555", "1", "666666", "22"]

lst = list(filter(lambda x: len(x) > 4, lst))

print(lst)