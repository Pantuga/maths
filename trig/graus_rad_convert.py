from fractions import Fraction
from math import pi
import math

print("=== Converter Graus e Radianos ===")

print("Converter para Radianos ou Graus? [r/g]")
match input()[0]:
    case "g":
        print("Nota: podes escrever frações (ex.: pi/4)")
        a_r = float(eval(input("ângulo (em radianos) = ")))
        a_g = a_r * 180 / pi
        print(str(a_r) + " rad = " + str(a_g) + "°")
    case "r":
        a_g = float(input("ângulo (em graus) = "))
        a_r_por_pi = a_g / 180
        a_r = a_r_por_pi * pi
        print(str(a_g) + "° =" )
        print("= (" + str(Fraction(a_r_por_pi).limit_denominator()) + ") * pi")
        print("= " + str(a_r) + " rad")
    case _:
        print("Unidade inváida")
        exit()