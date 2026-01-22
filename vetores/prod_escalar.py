print("=== Produto Escalar ===")
print("Sintaxe: (a, b, ...)")

try:
    u = tuple(eval(input("u = ")))
    v = tuple(eval(input("v = ")))
except:
    print("Erro: o valor inserido não é um vetor")
    exit()

if len(u) != len(v):
    print("Erro: vetores têm tamanhos difenetes")
    exit()

resultado = 0
for i in range(len(u)):
    resultado += u[i] * v[i]

print("u • v =", resultado)
