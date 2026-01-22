def valor_graus(a: int, valores):
    match a:
        case 0:
            return valores[0]
        case 30:
            return valores[1]
        case 45:
            return valores[2]
        case 60:
            return valores[3]
        case 90:
            return valores[4]
        case _:
            return "Valor não exato"
        
def valor_rad(a: int, valores):
    # o ângulo real é
    # pi / a
    match a:
        case 6:
            return valores[0]
        case 4:
            return valores[1]
        case 3:
            return valores[2]
        case 2:
            return valores[3]
        case _:
            return "Valor não exato"

print("=== Valor exato das funções trigonométricas ===")

a = 0
resultado = "??"

print("Razão trigonométrica? [sen/cos/tg]")
razao_trig = ""
match input()[0]:
    case "s": razao_trig = "sen"
    case "c": razao_trig = "cos"
    case "t": razao_trig = "tg"
    case _:
        print("Razão inválida")
        exit()


print("Radianos ou graus? [r/g]")
match input()[0]:
    case "r":
        a = int(float(input("ângulo = pi/")))
        match razao_trig:
            case "sen": 
                resultado = valor_rad(a, ("1/2", "√2/2", "√3/2", "1"))
            case "cos": 
                resultado = valor_rad(a, ("√3/2", "√2/2", "1/2", "0"))
            case "tg": 
                resultado = valor_rad(a, ("√3/3", "1", "√3", "Indefinido"))
    case "g":
        a = int(float(input("ângulo = ")))
        match razao_trig:
            case "sen": 
                resultado = valor_graus(a, ("0", "1/2", "√2/2", "√3/2", "1"))
            case "cos": 
                resultado = valor_graus(a, ("1", "√3/2", "√2/2", "1/2", "0"))
            case "tg": 
                resultado = valor_graus(a, ("0", "√3/3", "1", "√3", "Indefinido"))
    case _:
        print("Unidade inváida")
        exit()
    

print(razao_trig + "(" + str(a) + ") = " + resultado)