letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
dicionario = {}
for i in range(27):
    dicionario[letras[i]] = i + 2

def fast_exp(b, e, m):

    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r

def mdc(x, y):

    if (y == 0): return x

    z = fast_exp(x, 1, y) % y

    return mdc(y, z)

def primo(num):

    if (num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                return 0
        return 1
    else:
        return 0

def gerarchave():

    p = int(input("digite o primo 'p': \n"))

    while (primo(p) == 0):
        p = int(input("p não é primo \ndigite o primo 'p': \n"))

    q = int(input("digite o primo 'q': \n"))

    while (primo(q) == 0):
        q = int(input("q não é primo \ndigite o primo 'q': \n"))

    n = p * q

    totiente = (p - 1) * (q - 1)

    e = int(input("digite o expoente 'e': \n"))

    while (mdc(e, totiente) != 1 and e < totiente):
        e = int(input("expoente invalido \nlembre-se que o expoente deve ser coprimo de n, ou seja o mdc(e,n) deve ser igual a 1 \ndigite o expoente 'e': \n"))

    with open("chave_publica.txt", "w") as f:
        f.write(f"{e}, {n}")

def encriptar():

    msg = input("digite a mensagem a ser encriptada: \n")

    e = int(input("insira a chave publica \ndigite 'e': \n"))
    n = int(input("agora digite 'n': \n"))

    cryptMsg = ""
    i = 0

    while (i < len(msg)):
        m = msg[i]
        cryptMsg = cryptMsg + str(fast_exp(dicionario[m.upper()], e, n) % n)
        if(i + 1 != len(msg)):
            cryptMsg += " "
        i += 1
    with open("mensagem_encriptada.txt", "w") as f:
        f.write(f"{cryptMsg}")

def desencriptar():

    p = int(input("digite o primo 'p': \n"))

    while (primo(p) == 0):
        p = int(input("p não é primo \ndigite o primo 'p': \n"))

    q = int(input("digite o primo 'q': \n"))

    while (primo(q) == 0):
        q = int(input("q não é primo \ndigite o primo 'q': \n"))

    n = p * q
    totiente = (p - 1) * (q - 1)

    e = int(input("digite o expoente 'e': \n"))

    while (mdc(e, totiente) != 1 and e < totiente):
        e = int(input("expoente invalido \nlembre-se que o expoente deve ser coprimo de phi(n), ou seja o mdc(e,phi(n)) deve ser igual a 1 \ndigite um novo expoente 'e': \n"))

    msg = input("digite a mensagem a ser desencriptada: \n")

    d = 0
    while(int((d * e) % totiente) != 1):
        d += 1

    i = 0
    msgC = ""

    while(i < len(msg)):
        numeroatual = ""
        while(i < len(msg) and msg[i] != ' '):
            numeroatual += msg[i]
            i += 1
        numeroatual = int(numeroatual)
        i += 1
    
        msgC += str(letras[(fast_exp(numeroatual, d, n) - 2)])

    
    with open("mensagem_desencriptada.txt", "w") as f:
        f.write(f"{msgC}")

def main():        
    try:
        while (True):
            opcao = int(input('O que deseja fazer? \n1 - Gerar chave publica \n2 - Encriptar\n3 - Desencriptar\n0 - Sair\n'))
            if (opcao == 1):
                gerarchave()
                break 
            if (opcao == 2):
                encriptar()
                break
            if (opcao == 3):
                desencriptar()
                break
            if(opcao == 0):
                break
            if (not(opcao > 0 and opcao < 3)):
                print("valor invalido :( \ntente novamente... \n")
    except:
        print("valor não esperado :( \nprograma será fechado. \n")

main()

#Feito por Vinícius da Costa Neitzke