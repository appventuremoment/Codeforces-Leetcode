print((lambda year: [x for x in [len(str(x)) == len(set(str(x))) and x for x in range(year + 1, 9100)] if x][0])(int(input())))