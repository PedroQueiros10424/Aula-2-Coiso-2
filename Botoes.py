import tkinter as tk


janela = tk.Tk()

janela.geometry("350x400+75+30")

janela.title("Cores")

def azul():
    janela.config(background="blue")
def verde():
    janela.config(background="Green")
def vermelho():
    janela.config(background="red")
def amarelo():
    janela.config(background="Yellow")

buttom1=tk.Button(janela,text="Verde", fg="green",command=verde)
buttom1.place(x=20,y=200,width=100,height=100)

buttom2=tk.Button(janela,text="Azul",fg="Blue",command=azul)
buttom2.place(x=200,y=200,width=100,height=100)

buttom3=tk.Button(janela,text="Vermelho", fg="red",command=vermelho)
buttom3.place(x=200,y=20,width=100,height=100)

buttom4=tk.Button(janela,text="Amarelo",fg="Yellow", command=amarelo)
buttom4.place(x=20,y=20,width=100,height=100)

label1= tk.Label(text="cor",fg="Black",width=75,height=75)
label1.place(x=100,y=100)

janela.mainloop()