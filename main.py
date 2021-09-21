def kratnost(a, b):
    for i in a:
        if i % b != 0:
            return False
    return True

def poisk(a, b):
    if b in a.keys():
        return True
    else:
        return False

#здесь находтся 2 функции, которые впоследсвие проверяются(по 3 теста на каждую), первая для list, вторая для dict


