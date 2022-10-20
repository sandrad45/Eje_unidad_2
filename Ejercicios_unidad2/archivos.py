from pyparsing import line_end


file = open ("devices.txt", "r")
while True:
   line= input ("nombre de dispositivo:")
   if line == "Exit":
       print("line")
       break
file.write(line + "\n")
file.close()
 




