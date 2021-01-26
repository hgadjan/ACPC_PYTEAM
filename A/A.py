filepath = 'digits.in'
ans = ""
l = {'0': 'O',
     '1': 'I',
     '2':'Z',
     '3': 'E',
     '5': 'S',
     '7': 'L',
     '8': 'B',
     '9': 'G'
     }



with open(filepath) as fp:
    n = int(fp.readline().strip())
    line = fp.readline()
    cnt = 1

    while line and cnt <= n:
        numb = line[::-1]
        if numb:
            for i in numb:
                ans += l[i]
            ans +="\n"

        cnt += 1
        line = fp.readline()

print(ans)
