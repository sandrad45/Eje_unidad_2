file = open ("devices.txt", "r")
bus  = input('Que dispositivo desea buscar? ')
for line in file:
    line = line.strip()
    if bus in line: 
        print(line)
    else:
       print('NO existe ese dispositivo :X')