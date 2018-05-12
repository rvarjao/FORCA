import Common


class Forca():

    status_jogo_em_andamento = "status_jogo_em_andamento"
    status_jogo_encerrado_jogador_venceu = "status_jogo_encerrado_jogador_venceu"
    status_jogo_encerrado_jogador_perdeu = "status_jogo_encerrado_jogador_perdeu"

    def __init__(self):

        #variaveis
        self.palavra_secreta = ""  #palavra a ser adivinhada
        self.palpite = ""         #palavra como será apresentada na tela
        self.letras_tentadas = [ ] #letras que já foram tentadas
        self.mensagem = ""        #mensagens de erro, de game over, ou de já ganhou

        self.status = self.status_jogo_em_andamento

        self.vidas_restantes = 6

        self.codigoErroTentativaLetra = {0: "Você já tentou essa letra", 1: "Palavra secreta não possui a letra",
                                         2: "Palavra secreta possui a letra"}

        self.dicionario_palavra_secreta = self.escolha_nova_palavra()
        print("dicionario: ", self.dicionario_palavra_secreta)


        self.palavra_secreta = Common.remover_acentos (self.dicionario_palavra_secreta[ "palavra" ].upper ( ))
        self.categoria = self.dicionario_palavra_secreta[ "categoria" ]
        self.dica = self.dicionario_palavra_secreta[ "dica" ]

        self.titulo = "Categoria: {}".format (self.dicionario_palavra_secreta[ "categoria" ])

        self.palpite = ""
        charOculto = "*"

        # tira os espacos em branco do palpite
        for (i, char) in enumerate (self.palavra_secreta):
            if char == " ":
                self.palpite += char
            else:
                self.palpite += charOculto



    def escolha_nova_palavra(self):
        #SELECIONA UMA PALAVRA DENTRO DO BANCO DE DADOS
        import json
        import random

        file_obj = open ("LISTA_11_FORCA.txt", "r")
        # text = file_obj.read ( ).decode (encoding="utf-8")
        # database = json.loads (text, encoding="utf-8")
        text = file_obj.read ( )
        database = json.loads (text, encoding="utf-8")

        categorias = [ "filmes", "estados e capitais", "paises e capitais", "times", "nomes dos alunos" ]

        # escolhe uma categoria
        categoria = categorias[ random.randrange (0, len (categorias)) ]

        # pega todos os itens daquela categoria
        itens = database[ categoria ]

        # escolhe um item daquela categoria
        item = itens[ random.randrange (0, len (itens)) ]

        textoDica = ""
        chave = ""
        # como o banco de dados nao esta padronizado, dependendo da categoria escolhida tem que
        # ser feita a busca em chaves diferentes
        if categoria == "filmes":
            chave = "titulo"
            textoDica = "Ganhador da {}a edicao do Oscar".format (item[ "edicao" ])
        elif categoria == "times":
            chave = "nome"
            textoDica = "Time da 1a divisão do Campeonato Brasileiro de 2018"
        elif categoria == "estados e capitais":
            chave = "capital"
            estado = item[ "estado" ]
            textoDica = "Capital de {}".format (estado)
        elif categoria == "paises e capitais":
            chave = "pais"
            continente = item[ "continente" ]
            textoDica = "Continente: {}".format (continente)
        elif categoria == "nomes dos alunos":
            chave = "nome"
            textoDica = "Nome de um aluno(a)"

        palavra = item[ chave ]
        retornar = {"categoria": categoria, "palavra": palavra, "dica": textoDica}

        print("vai retornar: ", retornar)
        return retornar


    def tenta_letra(self, letra): 
        # verifica a letra e retorna um dicionario contendo uma mensagem e um codigo de erro ou acerto

        charOculto = "*"
        self.mensagem = ""

        if self.letras_tentadas.__contains__(letra):
            self.mensagem = "Você já tentou essa letra."
            self.colors[ "mensagem" ] = "yellow"

        else:
            self.letras_tentadas.append(letra)
            self.letras_tentadas.sort()
            if self.palavra_secreta.find(letra) == -1 :
                self.mensagem = "Palavra secreta não possui a letra: {}".format(letra)
                self.vidas_restantes -= 1
                if self.vidas_restantes == 0 :
                    self.mensagem = "Você perdeu. Palavra secreta é: {}".format(self.palavra_secreta)
                    self.status = self.status_jogo_encerrado_jogador_perdeu
                    self.fimDeJogo()

            else:
                temp = ""

                for (i, char) in enumerate(self.palavra_secreta):
                    if char == letra : temp += char
                    else: temp += self.palpite[i]
                    # print("PALPITE: {}".format(self.palpite))

                self.palpite = temp

                if self.palpite.find(charOculto) == -1:
                    self.mensagem = "Você venceu"
                    self.status = self.status_jogo_encerrado_jogador_perdeu
                    self.fimDeJogo()


    def str_letras_tentadas(self):
        str_letras = "["

        for (i, letra) in enumerate(self.letras_tentadas):
            str_letras += letra
            if i < len(self.letras_tentadas) - 1:
                str_letras += ","
        str_letras += "]"

        return str_letras

    def imprime_forca(self):
        
        # strForca = "Vidas restantes: {}\n".format(self.vidas_restantes)
        strForca = "_____\n"

        if self.vidas_restantes == 6:
            strForca += "|\n" * 3
        if self.vidas_restantes == 5:
            strForca += "|   O\n"
            strForca += "|\n" * 2
        if self.vidas_restantes == 4:
            strForca += "|   O\n"
            strForca += "|   |\n"
            strForca += "|\n"
        if self.vidas_restantes == 3:
            strForca += "|   O\n"
            strForca += "|  -|\n"
            strForca += "|\n"
        if self.vidas_restantes == 2:
            strForca += "|   O\n"
            strForca += "|  -|-\n"
            strForca += "|\n"
        if self.vidas_restantes == 1:
            strForca += "|   O\n"
            strForca += "|  -|-\n"
            strForca += "|  /\n"
        if self.vidas_restantes == 0:
            strForca += "|   O\n"
            strForca += "|  -|-\n"
            strForca += "|  / \\\n"
        print (strForca)
        
    def fimDeJogo(self):
        print("fim de jogo")
