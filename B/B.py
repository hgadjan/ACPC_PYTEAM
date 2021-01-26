filepath = 'winner.in'

with open(filepath) as fp:
    n = int(fp.readline())
    line = fp.readline()[0:n*2]
    one = line.count('1')
    two = line.count('2')
    
    if one > two:
        print('Mike')
    elif one < two:
        print('Jack')
    else:
        print('Tie')
