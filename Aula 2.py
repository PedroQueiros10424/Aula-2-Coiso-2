import tkinter as tk


janela = tk.Tk()

janela.geometry("350x400+75+30")

janela.title("Bolota")

janela.wm_resizable(width=False, height=False)

bolota1=tk.Button(janela,text="Clique Aqui para receber Bolotas!").place(x=80,y=50)
tk.Button(janela,text="Clique Aqui para não receber Bolotas!").place(x=80,y=90)
tk.Button(janela,text="Clique Aqui se for uma Bolota!").place(x=80,y=130)


janela.mainloop()
