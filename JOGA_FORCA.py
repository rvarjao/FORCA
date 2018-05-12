from FORCA import Forca

forca = Forca()

print("palavra: ", forca.palavra_secreta)

while forca.status == forca.status_jogo_em_andamento:
    # print("selecionado: {}".format(selecionado))

    print("\n"*5)
    titulo = "---FORCA---\n"

    palavra = forca.dicionario_palavra_secreta["palavra"]
    categoria = forca.dicionario_palavra_secreta["categoria"]
    dica = forca.dicionario_palavra_secreta["dica"]
    letras_tentadas = forca.letras_tentadas
    vidas_restantes = forca.vidas_restantes

    titulo += "Categoria: {}".format(forca.dicionario_palavra_secreta["categoria"]) + "\n"
    titulo += "Dica: {}\nnúmero de letras: {}".format(dica, len(palavra))
    titulo += "\nVidas restantes: {}".format(vidas_restantes)
    if forca.mensagem != "": print("mensagem: {} ".format(forca.mensagem))

    forca.imprime_forca()
    print("---> {}".format(forca.palpite))

    print(titulo)

    letra = input("Digite uma letra: ")

    forca.tenta_letra(letra.upper())


    print("letras tentadas: {}".format(forca.str_letras_tentadas()))
