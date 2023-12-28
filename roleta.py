def oroletar(aposta):
    fichas = 5000
    print(roleta)

    import json

    # Abra o arquivo JSON em modo de leitura
    with open('dados.json', 'r') as arquivo:
        # Carregue o conteúdo do arquivo JSON para um dicionário
        dados = json.load(arquivo)

    # Exemplo de como acessar o dicionário
    apostas = dados["apostas"]
    print(apostas)




def roletar():
    import random
    # Número Aleatório
    roleta = [x for x in range(37)]
    numero = random.choice(roleta)

    # Cor
    if int(int(numero)) == 0:
        cor = "Green"
    elif int(numero) in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        cor = "black"
    else:
        cor = "red"

    # Paridade
    paridade = "Even" if int(numero) % 2 == 0 else "Odd"
    if int(numero) in ["0", "00", "000"]: paridade = "none"

    # Linha
    linha = 0
    if int(numero) in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
        linha = 1
    if int(numero) in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
        linha = 2
    if int(numero) in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        linha = 3


    # Dúzia
    duzia = 0
    if int(numero) in range(1, 13):
        duzia = 1
    if int(numero) in range(13, 25):
        duzia = 2
    if int(numero) in range(25,37):
        duzia = 3

    # meia
    meia = 0
    meia = "1-18" if int(numero) in range(1, 19) else "19-36"

    # Resultado
    resultado = {
        "numero": numero,
        "Cor": cor,
        "Paridade": paridade,
        "Linha": linha,
        "Duzia": duzia,
        "meia": meia
    }

    return resultado

# Exemplo de uso
resultado_roleta = roletar()
print(resultado_roleta)


roletar()
