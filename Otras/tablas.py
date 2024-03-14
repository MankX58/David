numero = int(input(""))
veces = int(input(""))
for i in range(1, veces+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    

# Lo mismo pero con while     
# i = 1
# while i <= veces:
#     resultado = numero * i
#     prtin(f"{numero} x {i} = {resultado}")
#     i += 1