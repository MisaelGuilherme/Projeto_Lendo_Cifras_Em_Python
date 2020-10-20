from tkinter import *
from random import *
import pygame


class jogo:
    
    def __init__(self):
        
        self.confirmarPausa = False
        self.listaBotao = []
        self.contBrilho = 0
        self.contador = 0
        
        pygame.init()
        pygame.mixer.music.load('song/tema_principal.mp3')
        pygame.mixer.music.play(-1)
        pygame.event.wait()        
        
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

        logoImg1 = PhotoImage(file="img/viola3.png")
        self.logoimage1 = Label(self.janela, image=logoImg1, bg='white')
        self.logoimage1.place(x=10, y=70)        
        
        self.titulo1 = Label(self.janela, text='Campo Harmonico', font=('earwig factory',30), bg='white', fg='orange')
        self.titulo1.place(x=80,y=20)
        
        self.titulo2 = Label(self.janela, text='De', font=('earwig factory',25), bg='white', fg='orange')
        self.titulo2.place(x=240,y=90)
        
        self.titulo3 = Label(self.janela, text='C', font=('hanging letters',45), bg='white', fg='orange')
        self.titulo3.place(x=240,y=130)   

        self.botao = Button(self.janela, text='b', bg='white', activebackground='white', fg='orange', activeforeground='orange', font=('font bottons music pro', 60), border=0, command = lambda: self.harmonia_01('C'))
        self.botao.place(x=170,y=200)    

        logoImg2 = PhotoImage(file="img/guitarMan2.png")
        self.logoimage2 = Label(self.janela, image=logoImg2, bg='white')
        self.logoimage2.place(x=280, y=310)
        
        iconAud = PhotoImage(file='img/audio.png')
        self.audio = Button(self.janela, image=iconAud, bg='white', activebackground='white', border=0, command = lambda: self.som())
        self.audio.place(x=450, y=10)    
                
        self.efeito_botao_crescer()
        
        self.janela.mainloop()
    def efeito_botao_crescer(self):
        self.contBrilho += 1

        if self.contBrilho % 2 == 0:
            self.botao['fg'] = 'orange'

        else:
            self.botao['fg'] = 'white'
        
        self.botao.after(500, self.efeito_botao_crescer)
        
    def som(self):
        
        if pygame.mixer.music.get_busy() and self.confirmarPausa == False:
            self.audio.destroy()
            
            iconAud2 = PhotoImage(file='img/mute.png')
            
            self.mudo = Button(self.janela, image=iconAud2, border=0, bg='white', activebackground='white', command = self.som)
            self.mudo.place(x=450, y=10)
            
            pygame.mixer.music.set_volume(0.0)
            
            self.confirmarPausa = True
        
        else:            
            self.mudo.destroy()
            self.confirmarPausa = False
            
            iconAud = PhotoImage(file='img/audio.png')
            
            self.audio = Button(self.janela, image=iconAud, bg='white', activebackground='white', border=0,    command = self.som)
            self.audio.place(x=450, y=10)
            
            pygame.mixer.music.set_volume(1.0)
            
        self.janela.mainloop()

    def harmonia_01(self, grau):

        self.titulo1.destroy()
        self.titulo2.destroy()
        self.titulo3.destroy()
        self.botao.destroy()
        self.logoimage1.destroy()
        self.logoimage2.destroy()
        
        iconVio = PhotoImage(file='img/viola00.png')
        self.viola = Label(self.janela, image=iconVio, bg='white', border=0)
        self.viola.place(x=-130, y=40)
        
        txt1 = Label(self.janela, text='Informe na Ordem o Grau das Notas', font=('arial',15,'bold'), bg='white', fg='orange')
        txt1.place(x=80,y=20)        
        
        if grau == 'C':
            
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
                
            lb1 = Label(self.janela, text=v1, font=('hanging letters',25), fg='orange', bg='white', width=3)
            lb2 = Label(self.janela, text=v2, font=('hanging letters',25), fg='orange',bg='white', width=3)
            lb3 = Label(self.janela, text=v3, font=('hanging letters',25), fg='orange',bg='white', width=3)
            lb1.place(x=180,y=160)
            lb2.place(x=230,y=160)
            lb3.place(x=280,y=160)


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

        logoImg1 = PhotoImage(file="img/guitarMan1.png")
        self.logoimage2 = Label(self.janela, image=logoImg1, bg='white')
        self.logoimage2.place(x=280, y=300)

        self.janela.mainloop()

    def reiniciar(self):
        
        def restart():
            self.contador = 0
            self.bt1['bg'] = 'orange'
            self.bt2['bg'] = 'orange'
            self.bt3['bg'] = 'orange'
            self.bt4['bg'] = 'orange'
            self.bt5['bg'] = 'orange'
            self.bt6['bg'] = 'orange'
            self.bt7['bg'] = 'orange'
            
            self.reiniciar.destroy()
            
            self.logoimage3.destroy()
        
        def brilhar():
            
            self.contBrilho += 1
            
            if self.contBrilho % 2 == 0:
                self.reiniciar['fg'] = 'orange'
            else:
                self.reiniciar['fg'] = 'white'
            self.reiniciar.after(300, brilhar)

        self.reiniciar = Button(self.janela, text='Vamos de Novo?', bg='white', activebackground='white', fg='orange', activeforeground='orange', border=0, font=('arial', 18, 'bold'), command=restart)
        self.reiniciar.place(x=50, y=350)
        
        brilhar()
        
    def harmonia(self, grau):
                
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
