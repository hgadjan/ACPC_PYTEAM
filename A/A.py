filepath = 'digits.in'

l = {'0': 'O',
     '1': 'I',
     '2':'Z',
     '3': 'E',
     '5': 'S',
     '7': 'L',
     '8': 'B',
     '9': 'G'
     }

ans = ""

with open(filepath) as fp:
    line1 = fp.readline()
    line = fp.readline()
    cnt = 1
    while line and cnt <= int(line1.strip()):

        numb = str(line.strip())
        numb = numb[::-1]
        if numb:
            for i in numb:
                ans += l[i]
            ans +="\n"
        cnt += 1
        line = fp.readline()

print(ans)
