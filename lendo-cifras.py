#Programador: Misael Jesus
#Date: 23/09/2020
#e_mail: misaelleite2002@gmail.com

'''
Para que seja possível a execução do código, e necésário que possua o módulo "pygame" baixado e instalado no seu python,
também será preciso que baixe os arquivos e pastas referente a esta aplicação, caso contrário não irá funcionar.
Baixes a pasta completa e em seguida é só executar a aplicação. Bom proveito!!
'''

#Importando Módulos
from tkinter import *
from random import *
import pygame

#Classe contendo toda a aplicação
class jogo:
    
    def __init__(self):
        
        #Variáveis responsáveis por alguns controles do programa
        self.telaInicial = False
        self.confirmarPausa = False
        self.listaBotao = []
        self.contBrilho = 0
        self.contador = 0
        
        #Iniciando mixer de trilha sonora principal do programa
        pygame.init()
        pygame.mixer.music.load('song/tema_principal.mp3')
        pygame.mixer.music.play(-1)
        pygame.event.wait()        
        
        #Iniciando janela principal
        self.janela = Tk()
        self.janela.geometry('500x500+350+100')
        #self.janela.attributes("-alpha", 0.9)
        self.janela.resizable(False, False)
        #janela.minsize(400,400)
        #janela.maxsize(600,600)
        #janela.state('zoomed') ou iconic
        self.janela.title('Lendo Cifra')
        self.janela.iconbitmap("icons/violao.ico")
        self.janela['bg'] = 'white'
        self.componentes_janela_incial()
        self.janela.mainloop()
    
    def componentes_janela_incial(self):        
    
        #Imagem de violão na tela principal
        logoImg1 = PhotoImage(file="img/viola3.png")
        self.logoimage1 = Label(self.janela, image=logoImg1, bg='white')
        self.logoimage1.place(x=10, y=70)        
        
        self.titulo1 = Label(self.janela, text='Campo Harmonico', font=('earwig factory',30), bg='white', fg='orange')
        self.titulo1.place(x=80,y=20)
        
        self.titulo2 = Label(self.janela, text='De', font=('earwig factory',25), bg='white', fg='orange')
        self.titulo2.place(x=240,y=90)
        
        self.titulo3 = Label(self.janela, text='C', font=('hanging letters',45), bg='white', fg='orange')
        self.titulo3.place(x=240,y=130)   

        self.botao = Button(self.janela, text='b', bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('font bottons music pro', 60), border=0, command = lambda: self.janela_2_jogo('C'))
        self.botao.place(x=170,y=200)    

        #Imagem de homem tocando guitarra de brinquedo
        logoImg2 = PhotoImage(file="img/guitarMan2.png")
        self.logoimage2 = Label(self.janela, image=logoImg2, bg='white')
        self.logoimage2.place(x=280, y=310)
        
        #Icone do mutar ou abrir audio, na margem superior da janela principal
        iconAud = PhotoImage(file='img/audio.png')
        self.audio = Button(self.janela, image=iconAud, bg='white', activebackground='white', border=0, command = lambda: self.som())
        self.audio.place(x=460, y=5)    
                
        #Função que invocará procedimentos para fazer o botão principal piscar
        self.efeito_botao_crescer()
        
        self.janela.mainloop()
        
        
        
    #--- Função responsável por fazer o botão da janela principal piscar ---        
    def efeito_botao_crescer(self):
        
        self.contBrilho += 1

        if self.contBrilho % 2 == 0:
            self.botao['fg'] = 'orange'

        else:
            self.botao['fg'] = 'white'
        
        self.botao.after(500, self.efeito_botao_crescer)
    
    
    
    
    #--- Função responsável por tirar a música de fundo ao clicar no botão de volume da janela principal ---
    def som(self):
        
        #Se a função for invocada destruirá o ícone atual e criará o ícone de "mudo"
        if pygame.mixer.music.get_busy() and self.confirmarPausa == False:
            self.audio.destroy()
            
            iconAud2 = PhotoImage(file='img/mute.png')
            
            self.mudo = Button(self.janela, image=iconAud2, border=0, bg='white', activebackground='white', command = self.som)
            self.mudo.place(x=460, y=5)
            
            pygame.mixer.music.set_volume(0.0)
            
            self.confirmarPausa = True
        
        #Senão destruirá o de mudo e criará o de o botão de volume
        else:            
            self.mudo.destroy()
            self.confirmarPausa = False
            
            iconAud = PhotoImage(file='img/audio.png')
            
            self.audio = Button(self.janela, image=iconAud, bg='white', activebackground='white', border=0,    command = self.som)
            self.audio.place(x=460, y=5)
            
            pygame.mixer.music.set_volume(1.0)
            
        self.janela.mainloop()



    #--- Função responsável por selecionar quais notas aleatoriamente  irão imprimir na tela ---
    def escolhendo_notas_formar(self, tom):
        
        if tom == 'C':
            
            self.lista = ['C','Dm','Em','F','G','Am','Bº']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break

            v1 = self.lista[n1]
            v2 = self.lista[n2]
            v3 = self.lista[n3]

            self.dd = [False,False,False]
            self.listaEmba = [v1,v2,v3]
            
            self.lb1['text'] = v1
            self.lb2['text'] = v2
            self.lb3['text'] = v3



        
    #--- Função responsável por identicar qual o tom escolhido e interpretár os exercícios propostos ---
    def janela_2_jogo(self, grau):
        pygame.mixer.music.stop()

        pygame.mixer.music.load('song/jazz_piano.mp3')
        pygame.mixer.music.play(-1)
        
        #Destruindo os labels e botões da janela principal, fazendo um reaproveitamento da mesma janela
        self.titulo1.destroy()
        self.titulo2.destroy()
        self.titulo3.destroy()
        self.botao.destroy()
        self.logoimage1.destroy()
        self.logoimage2.destroy()
        
        #Imagem de violão na honrizontal na janela principal
        iconVio = PhotoImage(file='img/viola00.png')
        self.viola = Label(self.janela, image=iconVio, bg='white', border=0)
        self.viola.place(x=-130, y=50)
        
        #Botão com imagem de seta indicadora de voltar
        imgVoltar = PhotoImage(file='icons/seta2.png')
        self.botVoltar = Button(self.janela, image=imgVoltar, border=0, activebackground='white', bg='white', command=self.voltar)
        self.botVoltar.place(x=5, y=5)
                
        
        self.txt1 = Label(self.janela, text='Informe na Ordem o Grau das Notas', font=('arial',15,'bold'), bg='white', fg='orange')
        self.txt1.place(x=80,y=20)        
        
        self.lb1 = Label(self.janela, text='', font=('hanging letters',25), fg='orange', bg='white', width=3)
        self.lb2 = Label(self.janela, text='', font=('hanging letters',25), fg='orange',bg='white', width=3)
        self.lb3 = Label(self.janela, text='', font=('hanging letters',25), fg='orange',bg='white', width=3)
        self.lb1.place(x=180,y=160)
        self.lb2.place(x=230,y=160)
        self.lb3.place(x=280,y=160)          
        
        #Invocando função responsável por mostrar quais notas aleatoriamente irão aparecer
        self.escolhendo_notas_formar('C')

        #Botões que referenciam cada grau das notas
        self.bt1 = Button(self.janela, text='1º', command = lambda: self.harmonia(1), bg='orange', fg='white', width='5', relief='groove')
        self.bt1.place(x=80,y=245)
        self.bt2 = Button(self.janela, text='2º', command = lambda: self.harmonia(2), bg='orange', fg='white', width='5', relief='groove')
        self.bt2.place(x=130,y=245)
        self.bt3 = Button(self.janela, text='3º', command = lambda: self.harmonia(3), bg='orange', fg='white', width='5', relief='groove')
        self.bt3.place(x=180,y=245)
        self.bt4 = Button(self.janela, text='4º', command = lambda: self.harmonia(4), bg='orange', fg='white', width='5', relief='groove')
        self.bt4.place(x=230,y=245)
        self.bt5 = Button(self.janela, text='5º', command = lambda: self.harmonia(5), bg='orange', fg='white', width='5', relief='groove')
        self.bt5.place(x=280,y=245)
        self.bt6 = Button(self.janela, text='6º', command = lambda: self.harmonia(6), bg='orange', fg='white', width='5', relief='groove')
        self.bt6.place(x=330,y=245)
        self.bt7 = Button(self.janela, text='7º', command = lambda: self.harmonia(7), bg='orange', fg='white', width='5', relief='groove')
        self.bt7.place(x=380,y=245)

        #Homem com guitarra de brinquedo enquanto o jogador tentar acertas os exercícios das notas
        logoImg1 = PhotoImage(file="img/guitarMan1.png")
        self.logoimage2 = Label(self.janela, image=logoImg1, bg='white')
        self.logoimage2.place(x=280, y=300)

        self.janela.mainloop()

    
    
    #Função responsável por quando apertar o botão de voltar retornar para a tela inicial
    def voltar(self):
        
        self.viola.destroy()
        self.botVoltar.destroy()
        self.txt1.destroy()
        self.lb1.destroy()
        self.lb2.destroy()
        self.lb3.destroy()
        self.bt1.destroy()
        self.bt2.destroy()
        self.bt3.destroy()
        self.bt4.destroy()
        self.bt5.destroy()
        self.bt6.destroy()
        self.bt7.destroy()
        
        pygame.mixer.music.load('song/tema_principal.mp3')
        pygame.mixer.music.play(-1)
        
        self.logoimage2.destroy()        
        self.componentes_janela_incial()




    #--- Função responsável por reiniciar todo processo caso o jogador queira jogar novamente ---
    def reiniciar(self):
        
        #Função que irá reinicializar os labels e botões zerando tudo
        def restart():
            
            self.contador = 0
            
            self.bt1['bg'] = 'orange'
            self.bt2['bg'] = 'orange'
            self.bt3['bg'] = 'orange'
            self.bt4['bg'] = 'orange'
            self.bt5['bg'] = 'orange'
            self.bt6['bg'] = 'orange'
            self.bt7['bg'] = 'orange'
            
            self.botaoReiniciar.destroy()
            
            self.logoimage3.destroy()
            
            logoImg1 = PhotoImage(file="img/guitarMan1.png")
            self.logoimage2 = Label(self.janela, image=logoImg1, bg='white')
            self.logoimage2.place(x=280, y=300)            
            
            self.escolhendo_notas_formar('C')            
            
            self.janela.mainloop()
        
        #Função que fará o botão de jogar novamente piscar
        def brilhar():
            
            self.contBrilho += 1
            
            if self.contBrilho % 2 == 0:
                self.botaoReiniciar['fg'] = 'orange'
            else:
                self.botaoReiniciar['fg'] = 'white'
            self.botaoReiniciar.after(300, brilhar)

        #Botão de restart caso o jogador queira jogar novamente
        self.botaoReiniciar = Button(self.janela, text='Vamos de Novo?', bg='white', activebackground='white', fg='orange', activeforeground='orange', border=0, font=('arial', 18, 'bold'), command=restart)
        self.botaoReiniciar.place(x=50, y=350)
        
        #Chamando a função responsável por fazer o botão reiniciar piscar
        brilhar()

    
    
    
    #--- Função de verificação onde ao clicar no botão irá verificar se foi atingido a meta, e o jogador venceu---
    def harmonia(self, grau):
        
        #Verificando acerto caso o botão de grau 1 seja apertado
        if grau == 1:
            
            if  self.dd[0] == False and self.lista[0] == self.listaEmba[0]:
                self.bt1['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[0] == self.listaEmba[1]:
                self.bt1['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[0] == self.listaEmba[2]:
                self.bt1['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt1['bg'] = 'red'
                
            if self.contador >= 3:

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)

                self.reiniciar()

                self.janela.mainloop()                
        
        #Verificando acerto caso o botão de grau 2 seja apertado
        if grau == 2:
            if  self.dd[0] == False and self.lista[1] == self.listaEmba[0]:
                self.bt2['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[1] == self.listaEmba[1]:
                self.bt2['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[1] == self.listaEmba[2]:
                self.bt2['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt2['bg'] = 'red'

            if self.contador >= 3:
                
                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)

                self.reiniciar()
                
                self.janela.mainloop()

        #Verificando acerto caso o botão de grau 3 seja apertado
        if grau == 3:
            if  self.dd[0] == False and self.lista[2] == self.listaEmba[0]:
                self.bt3['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[2] == self.listaEmba[1]:
                self.bt3['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[2] == self.listaEmba[2]:
                self.bt3['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt3['bg'] = 'red'

            if self.contador >= 3:

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)
                
                self.reiniciar()

                self.janela.mainloop()
                
        #Verificando acerto caso o botão de grau 4 seja apertado                
        if grau == 4:
            if  self.dd[0] == False and self.lista[3] == self.listaEmba[0]:
                self.bt4['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[3] == self.listaEmba[1]:
                self.bt4['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[3] == self.listaEmba[2]:
                self.bt4['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt4['bg'] = 'red'

            if self.contador >= 3:

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)
                
                self.reiniciar()

                self.janela.mainloop()
                
        #Verificando acerto caso o botão de grau 5 seja apertado
        if grau == 5:
            if  self.dd[0] == False and self.lista[4] == self.listaEmba[0]:
                self.bt5['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[4] == self.listaEmba[1]:
                self.bt5['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[4] == self.listaEmba[2]:
                self.bt5['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt5['bg'] = 'red'

            if self.contador >= 3:           

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)
                
                self.reiniciar()

                self.janela.mainloop()
                
        #Verificando acerto caso o botão de grau 6 seja apertado
        if grau == 6:
            if  self.dd[0] == False and self.lista[5] == self.listaEmba[0]:
                self.bt6['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[5] == self.listaEmba[1]:
                self.bt6['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[5] == self.listaEmba[2]:
                self.bt6['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt6['bg'] = 'red'

            if self.contador >= 3:

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)
                
                self.reiniciar()

                self.janela.mainloop()

        #Verificando acerto caso o botão de grau 7 seja apertado
        if grau == 7:
            if  self.dd[0] == False and self.lista[6] == self.listaEmba[0]:
                self.bt7['bg'] = 'green'
                self.dd[0] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == False and self.lista[6] == self.listaEmba[1]:
                self.bt7['bg'] = 'green'
                self.dd[1] = True
                self.contador += 1
            elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[6] == self.listaEmba[2]:
                self.bt7['bg'] = 'green'
                self.dd[2] = True
                self.contador += 1
            else:
                self.bt7['bg'] = 'red'

            if self.contador >= 3:          

                self.logoimage2.destroy()
                logoImg3 = PhotoImage(file="img/guitarMan3.png")
                self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                self.logoimage3.place(x=300, y=300)
                
                self.reiniciar()

                self.janela.mainloop()


    #lb1 = Label(janela, text='Digite o grauº da nota', font=('arial',10,'bold'))
    #lb1.place(x=10,y=100)

instancia = jogo()
