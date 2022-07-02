num = int(input("INGRESA UN NÚMERO DE TRES CIFRAS: "))

cen = (num - (num % 100)) / 100
res = num % 100
dec = (res - (res % 10)) / 10
uni = res % 10

print("CENTENA: {}".format(int(cen)))
print("DECENA: {}".format(int(dec)))
print("UNIDAD: {}".format(int(uni)))