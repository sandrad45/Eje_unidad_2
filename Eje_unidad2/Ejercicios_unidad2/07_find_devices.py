file = open ("devices.txt", "r")
bus  = input('Nombre de dispositivo:')
for line in file:
    line = line.strip()
    if bus in line: 
        print(line)
    else:
       print('no encontrado')
