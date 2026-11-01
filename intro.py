# fazer o cadastro do cliente cpf, telefone e especificações do veículo

# permitir buscar por cpf e remover clientes com seus veículos
# o mesmo cliente pode cadastrar mais de um veículo

#criar layout inicial


from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image



class janela:
    def __init__(self):
        self.janelaprincipal = Tk()
        self.janelaprincipal.title('Oficina Mecânica')
        width = 900
        height = 670
        self.janelaprincipal.config(bg='white')
        tela_largura = self.janelaprincipal.winfo_screenwidth()
        tela_altura = self.janelaprincipal.winfo_screenheight()
        x = (tela_largura / 2) - (width / 2)
        y = (tela_altura / 2) - (height / 2)
        self.janelaprincipal.geometry("%dx%d+%d+%d" %(width,height,x,y))
        self.janelaprincipal.resizable(0,0)
        path = "imagens/logooficinamecanica.png"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.janelaprincipal,width=890,height=560,bg="snow",relief="sunken")
        main.place(x=55, y=70)
        fotoframe = LabelFrame(main,width=420,height=440,bg="snow",relief="raised")
        foto=Label(fotoframe, image=img)
        foto.place(x=6,y=6)
        fotoframe.place(x=10,y=100)



        self.janelaprincipal.mainloop()