list = [1, 2, 3, 4, 5, 6, 7]


def toDictionary(l):
    cift = []
    tek = []
    countcift = 0
    countTek = 0
    sumcift = 0
    sumTek = 0
    for x in l:
        if x % 2 == 0:
            cift.append(x)
            countcift += 1
            sumcift += x
        else:
            tek.append(x)
            countTek += 1
            sumTek += x
    Dict1 = ({
        'Even':
            {'list': cift,
             'sum': sumcift,
             'len of list': countcift
             },
        'Odd':
            {
                'list': tek,
                'sum': sumTek,
                'len of list': countTek
            }
    })

    return Dict1


print(toDictionary(list))


def palindrom(n):
    result = ''
    for x in n:
        result = x + result
    n = n.lower()
    result = result.lower()
    if result == n:
        return True
    else:
        return False


print(palindrom('AGA'))
print(palindrom('name'))
print(palindrom('Aga'))
