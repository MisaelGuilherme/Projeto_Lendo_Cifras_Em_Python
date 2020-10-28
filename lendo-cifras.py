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


#-------- Classe contendo toda a aplicação --------
class jogo:
   
    
    #--- sons, trilhas sonoras e efeitos ---
    def sons_efeitos(self, efeito):
         
        pygame.init()
         
        #Iniciando mixer de trilha sonora principal do programa
        if efeito == 'musica_tema_inicial':
            
            pygame.mixer.music.load('song/tema_principal.mp3')
            pygame.mixer.music.play(-1)
            pygame.event.wait()                

        elif efeito == 'musica_jazz_piano': 
            
            pygame.mixer.music.load('song/jazz_piano.mp3')
            pygame.mixer.music.play(-1)
        
        elif efeito == 'aplausos':
            
            self.aplausos = pygame.mixer.Sound('song/aplausos1.wav')
            self.aplausos.play()
        
        elif efeito == 'click':
            
            self.click = pygame.mixer.Sound("song/click.wav")
            self.click.play()
    
            
    
    
    #--- Função responsável por fazer o botão da janela principal piscar ---        
    def efeito_botao_crescer(self):
        
        self.contBrilho += 1

        if self.contBrilho % 2 == 0:
            self.botao['fg'] = 'orange'

        else:
            self.botao['fg'] = 'white'
        
        self.botao.after(500, self.efeito_botao_crescer)
        
    
    
    
    #--- Função responsável por aumentar o tom no Menu Inicial ---
    def mudar_tom_mais(self):
        lista = ['C','D','E','F','G','A','B']
        
        if self.contTom == 6: 
            self.contTom = 0
            self.titulo3['text'] = lista[self.contTom]        
        
        elif self.contTom == 0:
            self.contTom += 1
            self.titulo3['text'] = lista[self.contTom]
        else:
            self.contTom += 1
            self.titulo3['text'] = lista[self.contTom]
        print(self.contTom)
    
    
    
    
    #--- Função responsável por diminuir o tom no Menu Inicial ---
    def mudar_tom_menos(self):
        lista = ['C','D','E','F','G','A','B']
        
        if self.contTom == -6:
            self.contTom = 0
            self.titulo3['text'] = lista[self.contTom]        
        
        elif self.contTom == 0:
            self.contTom -= 1
            self.titulo3['text'] = lista[self.contTom]
        else:
            self.contTom -= 1
            print(self.contTom)
            self.titulo3['text'] = lista[self.contTom]    
        
        
        
        
    #--- Função Inicial, criando janela e configurando ---
    def __init__(self):
        
        #Variáveis responsáveis por alguns controles do programa
        self.rodada = False
        self.confirmarPausa = False
        self.listaBotao = []
        self.contBrilho = 0
        self.contador = 0
        self.contTom = 0
        
        #self.sons_efeitos('musica_tema_inicial')
        
        #Iniciando janela principal
        self.janela = Tk()
        self.janela.geometry('500x500+350+100')
        self.janela.resizable(False, False)

        self.janela.title('Lendo Cifra')
        self.janela.iconbitmap("icons/violao.ico")
        self.janela['bg'] = 'white'
        self.componentes_janela_incial()
        self.janela.mainloop()
    
    
    
    
    #--- Função responsável por adcionar os labels e botões do Menu Principal ---
    def componentes_janela_incial(self):        
    
        #Imagem de violão na tela principal
        logoImg1 = PhotoImage(file="img/viola3.png")
        self.logoimage1 = Label(self.janela, image=logoImg1, bg='white')
        self.logoimage1.place(x=10, y=70)        
        
        self.titulo1 = Label(self.janela, text='Campo Harmonico', font=('earwig factory',30), bg='white', fg='orange')
        self.titulo1.place(x=80,y=20)
        
        self.titulo2 = Label(self.janela, text='De', font=('earwig factory',25), bg='white', fg='orange')
        self.titulo2.place(x=240,y=90)
        
        self.setaEsquerd = Button(self.janela, text='v', border=0, bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('kg arrows', 30), command = self.mudar_tom_menos)
        self.setaEsquerd.place(x=170, y=130)
        
        self.setaDireit = Button(self.janela, text='u', border=0, bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('kg arrows', 30), command = self.mudar_tom_mais)
        self.setaDireit.place(x=270, y=130)
        
        self.titulo3 = Label(self.janela, text='C', font=('hanging letters',45), bg='white', fg='orange')
        self.titulo3.place(x=240,y=130)   

        self.botao = Button(self.janela, text='b', bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('font bottons music pro', 60), border=0, command = self.janela_2_jogo)
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
        

    
        
    #--- Função responsável por tirar a música de fundo ao clicar no botão de volume da janela principal ---
    def som(self):
        
        self.sons_efeitos('click')
        
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
        
        elif tom == 'D':
            
            self.lista = ['D','Em','F#m','G','A','Bm','C#º']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break                        
        
        elif tom == 'E':
            
            self.lista = ['E','F#m','G#m','A','B','C#m','D#º']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break
                       
        elif tom == 'F':
            
            self.lista = ['F','Gm','Am','Bb','C','Dm','Eº']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break
                
        elif tom == 'G':
            
            self.lista = ['G','Am','Bm','C','D','Em','F#º']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break
                
        elif tom == 'A':
            
            self.lista = ['A','Bm','C#m','D','E','F#m','G#º']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break
                
        elif tom == 'B':
            
            self.lista = ['B','C#m','D#m','E','F#','G#m','A#º']
            notas = []
            while True:
                n1 = randint(0,6)
                n2 = randint(0,6)
                n3 = randint(0,6)
                if n1 != n2 and n2 != n3 and n1 != n3:
                    break
            self.lb1['width'] = 4
            self.lb2['width'] = 4
            self.lb3['width'] = 4
            self.lb1.place(x=162,y=160)
            self.lb2.place(x=225,y=160)
            self.lb3.place(x=293,y=160)                        
                                
        v1 = self.lista[n1]
        v2 = self.lista[n2]
        v3 = self.lista[n3]

        self.dd = [False,False,False]
        self.listaEmba = [v1,v2,v3]
        
        self.lb1['text'] = v1
        self.lb2['text'] = v2
        self.lb3['text'] = v3



        
    #--- Função responsável por identicar qual o tom escolhido e interpretár os exercícios propostos ---
    def janela_2_jogo(self):
        
        self.contTom = 0
        
        self.tomHarmonia = self.titulo3['text']
        
        self.sons_efeitos('click')
        
        self.sons_efeitos('musica_jazz_piano')
        
        #Destruindo os labels e botões da janela principal, fazendo um reaproveitamento da mesma janela
        self.titulo1.destroy()
        self.titulo2.destroy()
        self.titulo3.destroy()
        self.botao.destroy()
        self.logoimage1.destroy()
        self.logoimage2.destroy()
        self.setaEsquerd.destroy()
        self.setaDireit.destroy()
        
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
        
        self.lb1 = Label(self.janela, text='', border=1, font=('arial',25), fg='orange', bg='pink', width=3)
        self.lb2 = Label(self.janela, text='', border=1, font=('arial',25), fg='orange',bg='pink', width=3)
        self.lb3 = Label(self.janela, text='', border=1, font=('arial',25), fg='orange',bg='pink', width=3)
        self.lb1.place(x=165,y=160)
        self.lb2.place(x=225,y=160)
        self.lb3.place(x=290,y=160)          
        
        #Invocando função responsável por mostrar quais notas aleatoriamente irão aparecer
        print(self.tomHarmonia)
        self.escolhendo_notas_formar(self.tomHarmonia)

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





    #--- Função de verificação onde ao clicar no botão irá verificar se foi atingido a meta, e o jogador venceu---
    def harmonia(self, grau):
        
        #Verificando acerto caso o botão de grau 1 seja apertado
        if grau == 1:
            
            self.verificar_acerto(0, self.bt1)
                
        #Verificando acerto caso o botão de grau 2 seja apertado
        if grau == 2:
            
            self.verificar_acerto(1, self.bt2)

        #Verificando acerto caso o botão de grau 3 seja apertado
        if grau == 3:
            
            self.verificar_acerto(2, self.bt3)            
                
        #Verificando acerto caso o botão de grau 4 seja apertado                
        if grau == 4:
            
            self.verificar_acerto(3, self.bt4)
                
        #Verificando acerto caso o botão de grau 5 seja apertado
        if grau == 5:
            
            self.verificar_acerto(4, self.bt5)
                
        #Verificando acerto caso o botão de grau 6 seja apertado
        if grau == 6:
            
            self.verificar_acerto(5, self.bt6)

        #Verificando acerto caso o botão de grau 7 seja apertado
        if grau == 7:
            
            self.verificar_acerto(6, self.bt7)




    #--- Função responsável por verificar os botões caso e configurando a cor caso haja acerto ---
    def verificar_acerto(self, L1, botaoNum):
        
        #Verificando acerto caso o botão seja apertado            
        if  self.dd[0] == False and self.lista[L1] == self.listaEmba[0]:
            botaoNum['bg'] = 'green'
            self.dd[0] = True
            self.contador += 1
        
        elif self.dd[0] == True and self.dd[1] == False and self.lista[L1] == self.listaEmba[1]:
            botaoNum['bg'] = 'green'
            self.dd[1] = True
            self.contador += 1
        
        elif self.dd[0] == True and self.dd[1] == True and self.dd[2] == False and self.lista[L1] == self.listaEmba[2]:
            botaoNum['bg'] = 'green'
            self.dd[2] = True
            self.contador += 1
        else:
            botaoNum['bg'] = 'red' 
            
        if self.contador >= 3:

            self.partida_vencida()
    
    
    
    
    #--- Função responsável por configurar layout de vitória  caso o jogador tenha acertado as alternativas ---
    def partida_vencida(self):
        
        self.rodada = True
        
        self.logoimage2.destroy()
        logoImg3 = PhotoImage(file="img/guitarMan3.png")
        self.logoimage3 = Label(self.janela, image=logoImg3, bg='white')
        self.logoimage3.place(x=300, y=300)

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
            
            pygame.mixer.music.stop()
            pygame.mixer.music.load('song/jazz_piano.mp3')       
            pygame.mixer.music.play()
            
            self.escolhendo_notas_formar(self.tomHarmonia)
            
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
        self.botaoReiniciar = Button(self.janela, text='r', border=0, bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('kg arrows', 70), command=restart)
        self.botaoReiniciar.place(x=80, y=330)
        
        #Chamando a função responsável por fazer o botão reiniciar piscar
        brilhar()
        
        self.sons_efeitos('aplausos')
        
        self.janela.mainloop()    
    
    
    
    
    #--- Função responsável por quando apertar o botão de voltar retornar para a tela inicial ---
    def voltar(self):
        
        self.sons_efeitos('click')
        
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
        
        self.contador = 0
        
        if self.rodada == True:
            self.botaoReiniciar.destroy()
            self.logoimage3.destroy()
        
        pygame.mixer.music.load('song/tema_principal.mp3')
        pygame.mixer.music.play(-1)
        
        self.logoimage2.destroy()
        self.componentes_janela_incial()        

instancia = jogo()
