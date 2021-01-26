filepath = 'trick.in'
line = ''

with open(filepath) as fp:
    line = fp.readline().split(' ')
    
print(max(int(line[0]) + int(line[1]), abs(int(line[0]) - int(line[1])), int(line[0]) * int(line[1])))