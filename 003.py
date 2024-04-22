vlan_normal=range(1,1005)
vlan_extendida=range(1006,4094)
numero_vlan=int(input("Ingrese el numero de vlan"))

if numero_vlan in vlan_normal:
    print("El numero de la vlan",numero_vlan,"es normal")
elif numero_vlan in vlan_extendida:
    print  ("El numero de la vlan",numero_vlan,"es extendido")
else:
    print("EL numero de vlan",numero_vlan, "no corresponde a una vlan de rango normal o extendida")