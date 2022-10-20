file = open ("devices.txt", "r")
bus  = input('Que dispositivo desea buscar? ')
for line in file:
    line = line.strip()
    print (line)
    
    if bus in line: 
        print(line)
    else:
       print('no encontrado')
