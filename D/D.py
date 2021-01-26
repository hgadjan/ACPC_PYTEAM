filepath = 'number.in'
ans = ''
number_list = []

with open(filepath) as fp:
    n = fp.readline()
    line = fp.readline()

    for i in range(int(n)):
        number_list.append(line[i])
 
number_list.sort()
for num in number_list:
    ans = str(num) + ans
      
print(ans)