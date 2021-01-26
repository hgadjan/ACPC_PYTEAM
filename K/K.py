filepath = 'mango.in'
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = list()

with open(filepath) as fp:
    s = str(fp.readline().strip())
    for i in range(26):
        ans.append(s.count(l[i]))

out = ""

for item in ans:
    out += str(item)+' '

out+= '\n'
sortedItem = sorted(s)

for element in sortedItem:
    out += element


print(out)
