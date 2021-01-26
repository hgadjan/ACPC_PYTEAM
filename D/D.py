filepath = 'number.in'
ans = ''
number_list = []

with open(filepath) as fp:
    line1 = fp.readline()
    line = fp.readline()

    for i in range(int(line1)):
        number_list.append(line[i])
 
number_list.sort()
for num in number_list:
    ans = str(num) + ans
      
print(ans)