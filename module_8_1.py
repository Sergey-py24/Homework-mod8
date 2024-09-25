

def add_everything_up(a, b):
    try:
        res = a + b
        return res
    except TypeError:
        res = str(a) + str(b)
        return res




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('wasd', 'qwerty'))