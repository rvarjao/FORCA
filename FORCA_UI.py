# coding=utf-8
# encoding=utf8
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from FORCA import Forca

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        master.minsize (width=800, height=800)

        self.pack()

        self.winfo_toplevel().title("Forca - by Ricardo Varjão")

        #variaveis
        self.forca = Forca()

        self.colors = {"mensagem" : "black"}


        #CRIA OBJETOS DA TELA INICIAL
        self.cria_tela_inicial()
        self.novoJogo()
        root.bind ('<Return>', self.acao_botao_ok())



    def cria_tela_inicial(self):
        #CRIA OBJETOS DA TELA INICIAL

        self.btnNewGame = tk.Button(self)
        self.btnNewGame["text"] = "Novo jogo"
        self.btnNewGame["command"] = self.novoJogo
        self.btnNewGame.pack()

        self.labelTitulo = tk.Label(self)
        self.labelTitulo.pack()
        self.labelTitulo["text"] = "Titulo"

        self.labelDica = tk.Label(self)
        self.labelDica["text"] = "Dica"
        self.labelDica.pack()

        self.labelMensagem = tk.Label(self)
        self.labelMensagem["text"] = "Mensagem"
        self.labelMensagem.pack()

        self.frameDoJogo = tk.Frame(self)
        self.frameDoJogo.pack (fill="both", expand="yes")

        img = ImageTk.PhotoImage (Image.open ("imagens_forca/forca6.jpg"))
        self.labelImage = tk.Label (self.frameDoJogo, image=img)
        self.labelImage.image = img
        self.labelImage.pack(side = "left")

        self.labelPalavra = tk.Label(self.frameDoJogo)
        self.labelPalavra["text"] = "PALAVRA SECRETA"
        self.labelPalavra.pack(side = "right")

        self.frame_entrada_de_dados = tk.Frame(self)
        self.frame_entrada_de_dados.pack()

        self.labelLetras = tk.Label(self.frame_entrada_de_dados)
        self.labelLetras["text"] = "Letras tentadas"
        self.labelLetras.pack(side="top")

        self.labelNovaLetra = tk.Label (self.frame_entrada_de_dados)
        self.labelNovaLetra[ "text" ] = "Nova letra: "
        self.labelNovaLetra.pack (side="left")

        # self.btnOk = tk.Button(self.frame_entrada_de_dados)
        # self.btnOk["text"] = "Ok"
        # self.btnOk.pack(side = "right")
        # self.btnOk["command"] = self.acao_botao_ok

        self.campoNovaLetra = tk.Entry(self.frame_entrada_de_dados)
        self.campoNovaLetra.pack(side = "right")
        self.campoNovaLetra.focus()
        self.campoNovaLetra.bind('<Return>', lambda event : self.acao_botao_ok())

        fontSize = 20
        self.labelPalavra.configure(font=("Helvetica", 40))
        self.labelLetras.configure(font=("Helvetica", fontSize))
        self.labelDica.configure(font=("Helvetica", fontSize))
        self.labelMensagem.configure(font=("Helvetica", int(fontSize * 1.5)))
        self.labelNovaLetra.configurefont=("Helvetica", fontSize)
        self.labelTitulo.configure(font=("Helvetica", fontSize))


    def novoJogo(self):

        self.campoNovaLetra.config(state = 'normal')

        self.forca = Forca()
        self.forca.escolha_nova_palavra()
        self.atualiza_tela()

    def acao_botao_ok(self):
        if len(self.campoNovaLetra.get()) > 0:
            letra = self.campoNovaLetra.get()[0].upper()
            self.set_text(self.campoNovaLetra, "")
            self.forca.tenta_letra(letra)
            self.atualiza_tela()


    def atualiza_tela(self):

        #LABEL DAS LETRAS TENTADAS


        print("mensgem: {}".format(self.forca.mensagem))
        print("   dica: {}".format(self.forca.dica))
        print("palpite: {}".format(self.forca.palpite))
        print(" titulo: {}".format(self.forca.titulo))
        print("mensgem: {}".format(self.forca.mensagem))


        self.labelMensagem.configure(fg=self.colors["mensagem"])
        self.labelMensagem["text"] = self.forca.mensagem

        self.labelLetras["text"] = self.forca.str_letras_tentadas()
        self.labelDica["text"] = self.forca.dica
        self.labelPalavra["text"] = self.forca.palpite
        self.labelTitulo["text"] = self.forca.titulo

        fileName = "imagens_forca/forca{}.jpg".format(self.forca.vidas_restantes)
        img = ImageTk.PhotoImage (Image.open (fileName))
        self.labelImage.configure(image = img)
        self.labelImage.image = img

        if self.forca.status != self.forca.status_jogo_em_andamento:
            self.fimDeJogo()

    # img2 = ImageTk.PhotoImage(Image.open(path2))
    # panel.configure(image=img2)
    # panel.image = img2


    #             self.labelImage = tk.Label (self.frameDoJogo, image=img)


    def fimDeJogo(self):
        self.campoNovaLetra.config(state = 'disabled')
        self.updateLabels()
        print("fim de jogo")


    def set_text(self, field, text):
        field.delete (0, END)
        field.insert (0, text)
        return





root = tk.Tk()
app = Application(master=root)
root.resizable (width=False, height=False)
root.size()
app.mainloop()
