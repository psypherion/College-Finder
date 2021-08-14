ip = input('Enter You Expression : ')
index = 0
ip = ip.split()
print('Original Input: ', ip)
print('Simplifying...')

#Power simplify
while True:
    temp = False
    for i in range(0, len(ip)):
        if ip[i] == '^':    temp = True
    if temp == False:   break
    for i in range(0, len(ip)):
        if ip[i] == '^':
            index = i
            break
    val = float(ip[(index-1)]) ** float(ip[(index+1)])
    del ip[index - 1]
    del ip[index]
    del ip[index - 1]
    ip.insert((index - 1), str(val))

print(ip)

#Division simplify
while True:
    temp = False
    for i in range(0, len(ip)):
        if ip[i] == '/':    temp = True
    if temp == False:   break
    for i in range(0, len(ip)):
        if ip[i] == '/':
            index = i
            break
    val = float(ip[(index-1)]) / float(ip[(index+1)])
    del ip[index - 1]
    del ip[index]
    del ip[index - 1]
    ip.insert((index - 1), str(val))
print(ip)

#Multiplication Simplify
while True:
    temp = False
    for i in range(0, len(ip)):
        if ip[i] == '*':    temp = True
    if temp == False:   break
    for i in range(0, len(ip)):
        if ip[i] == '*':
            index = i
            break
    val = float(ip[(index-1)]) * float(ip[(index+1)])
    del ip[index - 1]
    del ip[index]
    del ip[index - 1]
    ip.insert((index - 1), str(val))
print(ip)

#Substraction check
while True:
    temp = False
    for i in range(0, len(ip)):
        if ip[i] == '-':    temp = True
    if temp == False:   break
    for i in range(0, len(ip)):
        if ip[i] == '-':
            index = i
            break
    val = -float(ip[i+1])
    del ip[index]
    del ip[index]
    ip.insert((index), str(val))


print(ip)
#Addition
for i in range(len(ip)):
    if ip[i]=='+': ip[i] = '0'
    ip[i]=float(ip[i])
print('Result= ', sum(ip))
