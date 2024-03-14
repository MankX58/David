num1 = int(input(""))
num2 = int(input(""))
impar = 0
multiplo_3 = 0 

for i in range (num1, num2+1):

    if i % 2 != 0:
        impar += 1

    if i % 3 == 0:
       multiplo_3 = multiplo_3 + 1

print(int(impar))
print(int(multiplo_3))

