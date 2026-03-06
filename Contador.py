import tkinter as tk


janela = tk.Tk()

janela.geometry("350x400+75+75")
pontos=0

def adicionar():
    global pontos
    pontos+=1
    label1.config(text=pontos)

def subtrair():
    global pontos
    pontos-=1
    label1.config(text=pontos)

def resetar():
    global pontos
    pontos = 0
    label1.config(text=pontos)



buttom1=tk.Button(janela,text="+1", command=adicionar)
buttom1.pack()

buttom2=tk.Button(janela,text="-1", command=subtrair)
buttom2.pack()

buttom3=tk.Button(janela,text="Resetar", command = resetar)
buttom3.pack()

label1= tk.Label(text=pontos,height=200,width=40)
label1.pack()
janela.mainloop()