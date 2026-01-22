from math import pi

print("=== Simplificar Ângulos Orientados (graus) ===")
    
# x = a + k*360
x = float(input("ângulo = "))
k = int(abs(x) // 360)
a = abs(x) - (k*360)

if x >= 0:
    print("ângulo =", a, "+", k, "* 360")
else:
    print("ângulo = -", a, "-", k, "* 360")
