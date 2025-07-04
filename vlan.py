vlan = int(input("Ingrese número de VLAN: "))
if 1 <= vlan <= 1005:
    print("VLAN normal")
elif 1006 <= vlan <= 4094:
    print("VLAN extendida")
else:
    print("VLAN fuera de rango")
