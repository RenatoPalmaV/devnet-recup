# file = open("rec-examenes/devices.txt", "r")
# for item in file:
#     print(item)
# file.close()

# file = open("rec-examenes/devices.txt", "r")
# for item in file:
#     item = item.strip()
#     print(item)
# file.close()

devices = []
file = open("rec-examenes/devices.txt", "r")
for item in file:
    item = item.strip()
    devices.append(item)
file.close()
print(devices)
