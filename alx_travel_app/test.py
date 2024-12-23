list = (1, 2, 3, 4)

def generator(lst):
    for i in lst:
        yield i
        i += 1
        print(i)

for value in generator(list):
    pass