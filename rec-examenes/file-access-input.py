file = open("rec-examenes/devices.txt", "a")
while True:
    new_item = input("Enter device name: ")
    if new_item == "exit":
        print("All done!")
        break
    file.write(new_item + "\n")
file.close()
