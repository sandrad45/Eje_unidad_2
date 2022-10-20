devices=[]
file=open("devices.txt","a")
while True:
    newItem= input("nuevo devices: ")
    if newItem == "exit":
        print("All done!")
        newItem=newItem.strip()
        break
    else:
        file.write(newItem +"\n")
    
file.close()