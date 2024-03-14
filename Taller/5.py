V = int(input("")) 
C = int(input(""))

if C > 20:
    V = V * 0.93

if V > 560000:
    V = V * 0.78
    print(int(V))
else: print(int(V))


