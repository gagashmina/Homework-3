def is_same_color(k, l, m, n):
    color1 = (k + l) % 2
    color2 = (m + n) % 2
    if color1 == color2:
        return "Поля ({} {}) и ({} {}) являются полями одного цвета.".format(k, l, m, n)
    else:
        return "Поля ({} {}) и ({} {}) не являются полями одного цвета.".format(k, l, m, n)


def is_threatened(k, l, m, n, figure):
    if figure == "ферзь":
        if k == m or l == n or abs(k - m) == abs(l - n):
            return "Ферзь угрожает полю ({} {})".format(m, n)
        else:
            return "Ферзь не угрожает полю ({} {})".format(m, n)
    elif figure == "ладья":
        if k == m or l == n:
            return "Ладья угрожает полю ({} {})".format(m, n)
        else:
            return "Ладья не угрожает полю ({} {})".format(m, n)
    elif figure == "слон":
        if abs(k - m) == abs(l - n):
            return "Слон угрожает полю ({} {})".format(m, n)
        else:
            return "Слон не угрожает полю ({} {})".format(m, n)
    elif figure == "конь":
        if abs(k - m) == 2 and abs(l - n) == 1 or abs(k - m) == 1 and abs(l - n) == 2:
            return "Конь угрожает полю ({} {})".format(m, n)
        else:
            return "Конь не угрожает полю ({} {})".format(m, n)
    else:
        return "Некорректное название фигуры."


def is_reachable(k, l, m, n, figure):
    if figure == "ладья":
        if k == m or l == n:
            return "Ладья может попасть на поле ({} {}) одним ходом.".format(m, n)
        else:
            return "Ладья не может попасть на поле ({} {}) одним ходом. Можно попасть на поле ({} {}) за два хода.".format(m, n, k, n)
    elif figure == "ферзь" or figure == "слон":
        if abs(k - m) == abs(l - n):
            return "{} может попасть на поле ({} {}) одним ходом.".format(figure.capitalize(), m, n)
        else:
            return "{} не может попасть на поле ({} {}) одним ходом. Можно попасть на поле ({} {}) за два хода.".format(figure.capitalize(), m, n, k, n)
    else:
        return "Некорректное название фигуры."


# Входные данные
k = int(input("Введите номер вертикали для поля 1: "))
l = int(input("Введите номер горизонтали для поля 1: "))
m = int(input("Введите номер вертикали для поля 2: "))
n = int(input("Введите номер горизонтали для поля 2: "))
figure = input("Введите название фигуры (ферзь, ладья, слон, конь): ")

# Проверка на цвет полей
print(is_same_color(k, l, m, n))

# Проверка на угрозу фигурой
print(is_threatened(k, l, m, n, figure))

# Проверка на достижимость фигурой
print(is_reachable(k, l, m, n, figure))