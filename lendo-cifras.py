from tkinter import *
from random import *

class jogo:
    def __init__(self):
        self.add = 80
        self.listaBotao = []
        self.contador = 0
        self.janela = Tk()
        self.janela.geometry('500x500+350+100')
        self.janela.resizable(False, False)
        #janela.minsize(400,400)
        #janela.maxsize(600,600)
        #janela.state('zoomed') ou iconic
        self.janela.title('Lendo Cifra')
        self.janela.iconbitmap("icons/violao.ico")
        self.janela['bg'] = 'white'

        self.titulo = Label(self.janela, text='Campo Harmonico de C', font=('arial',15,'bold'), bg='white', fg='orange')
        self.titulo.place(x=140,y=30)

        self.botao = Button(self.janela, text='Iniciar', bg='orange', fg='white', relief='groove', font=('arial', 14, 'bold'), width=10, command = lambda: self.harmonia_01('C'))
        self.botao.place(x=200,y=230)

        logoImg = PhotoImage(file="img/guitarMan2.png")
        self.logoimage = Label(self.janela, image=logoImg, bg='white')
        self.logoimage.place(x=240, y=270)
        self.janela.mainloop()
    
    def harmonia_01(self, grau):

        self.titulo.destroy()
        self.botao.destroy()
        self.logoimage.destroy()
        
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
                
            lb1 = Label(self.janela, text=v1, font=('arial',18,'bold'), bg='white', width=3)
            lb2 = Label(self.janela, text=v2, font=('arial',18,'bold'), bg='white', width=3)
            lb3 = Label(self.janela, text=v3, font=('arial',18,'bold'), bg='white', width=3)
            lb1.place(x=180,y=130)
            lb2.place(x=230,y=130)
            lb3.place(x=280,y=130)

        
        txt1 = Label(self.janela, text='Informe na Ordem a Sequência das Notas:', font=('arial',13,'bold'), bg='white', fg='orange')
        txt1.place(x=30,y=200)

        for c in range(1, 8):
            self.listaBotao.append(c)
        for c in self.listaBotao:
            self.bt = Button(self.janela, text= str(c)+'º', command = lambda: self.harmonia(c), bg='orange', fg='white', width='5', border=1)
            if c == 1:
                self.bt.place(x=self.add,y=105)
            else:
                self.add += 50
                self.bt.place(x = self.add, y = 105)
        ioo
        '''self.bt1 = Button(self.janela, text='1º', command = lambda: self.harmonia(1), bg='orange', fg='white', width='5', border=1)
        self.bt1.place(x=80,y=245)
        self.bt2 = Button(self.janela, text='2º', command = lambda: self.harmonia(2), bg='orange', fg='white', width='5', border=1)
        self.bt2.place(x=130,y=245)
        self.bt3 = Button(self.janela, text='3º', command = lambda: self.harmonia(3), bg='orange', fg='white', width='5', border=1)
        self.bt3.place(x=180,y=245)
        self.bt4 = Button(self.janela, text='4º', command = lambda: self.harmonia(4), bg='orange', fg='white', width='5', border=1)
        self.bt4.place(x=230,y=245)
        self.bt5 = Button(self.janela, text='5º', command = lambda: self.harmonia(5), bg='orange', fg='white', width='5', border=1)
        self.bt5.place(x=280,y=245)
        self.bt6 = Button(self.janela, text='6º', command = lambda: self.harmonia(6), bg='orange', fg='white', width='5', border=1)
        self.bt6.place(x=330,y=245)
        self.bt7 = Button(self.janela, text='7º', command = lambda: self.harmonia(7), bg='orange', fg='white', width='5', border=1)
        self.bt7.place(x=380,y=245)'''

        logoImg2 = PhotoImage(file="img/guitarMan1.png")
        self.logoimage2 = Label(self.janela, image=logoImg2, bg='white')
        self.logoimage2.place(x=260, y=270)

        self.janela.mainloop()
        
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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

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
                logoimage3 = Label(self.janela, image=logoImg3, bg='white')
                logoimage3.place(x=260, y=270)

                self.janela.mainloop()


    #lb1 = Label(janela, text='Digite o grauº da nota', font=('arial',10,'bold'))
    #lb1.place(x=10,y=100)

instancia = jogo()
