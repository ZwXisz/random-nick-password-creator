import random
import string
def nick_auto():
        Alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        vogais = ['a', 'e', 'i', 'o', 'u']
        consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        nome = []

        max_letras = random.randint(6, 13)

        letra1 = random.choice(Alfabeto)

        nome.append(letra1)
           
        while len(nome) < max_letras:
            if nome[-1] == "q":
                CouV = "u"
            elif len(nome)>=2 and nome[-2] == "q" and nome[-1] == "u":
                CouV = random.choice(vogais)
            elif nome[-1] in vogais:
                CouV = random.choice(consoantes)
            elif nome[-1] == "r":
                CouV = random.choice(vogais + ["r"])
            elif nome [-1] == "s":
                CouV = random.choice(vogais + ["s"])
            elif nome[-1] in consoantes:
                CouV = random.choice(vogais)
            else: CouV = random.choice(Alfabeto)
            nome.append(CouV)
        
        if (nome[-2] in consoantes and nome[-2] in ["r", "s"]) and (nome[-1] in consoantes and nome[-1] in ["r", "s"]):
            CouV = random.choice(vogais)
            nome.append(CouV)
        elif nome[-1] in consoantes and nome[-1]not in ["r", "s", "m"]:
            CouV = random.choice(vogais)
            nome.append(CouV)

        nome_visor = ''.join(nome)
        print(nome_visor)
nick_auto()
def senha_auto():
    letras = list(string.ascii_lowercase) 
    letras_maiusculas = list(string.ascii_uppercase) 
    simbolos = list(string.punctuation)  

    senha = [] 

    simb = random.choice(simbolos)
    maiusc = random.randint(1, 6)
    tamanho = random.randint(6, 16)

    
    for letra in simb:
        if letra.isalpha():
            senha.append(letra)
    
    for _ in range(maiusc):
        senha.append(random.choice(letras_maiusculas))

    for _ in simb:
        if simb.isprintable():
            senha.append(simb)

    while len(senha) < tamanho:
        colocar = random.choice(letras)
        senha.append(colocar)
    



    random.shuffle(senha)
    senha_visor = ''.join(senha)
    print(senha_visor)
senha_auto() 