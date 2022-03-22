def number_gen(n):
    acca = 1
    list_for_marcus = []

    while acca <= n:
        list_for_marcus.append(acca)
        acca += 1
    
    return list_for_marcus


def number_generator(n):
    acca = 1

    while acca <= n:
        yield acca
        acca += 1


print(number_gen(10))
print(number_gen(20))

foo = number_generator(10)
print(next(foo))
print(next(foo))

print(list(number_generator(10)))

print(list(range(10)))