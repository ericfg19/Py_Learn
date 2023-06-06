import tkinter as tk
from tkinter import ttk
import sqlite3
import ctypes as ct
import pandas as pd
import webbrowser
from statistics import mean

pd.options.display.max_rows = None

# conexao com db
cnx_path = 'C:\\PB\\data\\PB_Tabela.db'

def consulta_tabela():
    result_text.delete("1.0", "end-1c") # Deletar texto do result 
    cnx = sqlite3.connect(cnx_path) # conexao com db
    housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consulta_valores():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    housingdb = pd.read_sql_query("SELECT MAX(lot_area) AS Máximo, MIN(lot_area) as Mínimo, AVG(lot_area) as Média from PB_tabela", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consulta_itens():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela WHERE garage_type = 'Detchd'", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consultar_lista_num():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    consulta = "SELECT lot_area FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_num = resultado['Lot_Area'].tolist()
    result_text.insert(tk.END, str(lista_var_num) + "\n")

def consultar_lista_categoria():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    consulta = "SELECT garage_type FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_categoria = resultado['Garage_Type'].tolist()
    result_text.insert(tk.END, str(lista_var_categoria) + "\n")

def calcular_soma():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    consulta = "SELECT lot_area FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_num = resultado['Lot_Area'].tolist()
    media = mean(lista_var_num)
    soma_val_media = 0
    for valor in lista_var_num:
        if valor > media:
            soma_val_media += valor
    result_text.insert(tk.END, "A soma dos valores acima da média é: {:.2f}\n".format(soma_val_media))

def contar_itens():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect(cnx_path)
    consulta = "SELECT garage_type FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_categoria = resultado['Garage_Type'].tolist()
    contagem = {}
    for categoria in lista_var_categoria:
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    for categoria, quantidade in contagem.items():
        if categoria == '':
            result_text.insert(tk.END, f"Casas com a Garagem 'NULL' constam {quantidade} vezes na lista.\n")
        else:
            result_text.insert(tk.END, f"Casas com a Garagem '{categoria}' constam {quantidade} vezes na lista.\n")

def linkedin():
        webbrowser.open_new(r"https://www.linkedin.com/in/ericfguimaraes/")
def github():
        webbrowser.open_new(r"https://github.com/ericfg19/")

# Alterar cor de barra de janela
def dark_title_bar(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

root = tk.Tk()
root.title("Projeto de Bloco - [Processamento de Dados [23E1_5]]")
root.iconbitmap("C:\\PB\\img\\icon.ico")
root.geometry("1000x725")
dark_title_bar(root)


frame = tk.Frame(root)
frame.pack(pady=10)



button1 = tk.Button(frame, text="10 - Consultar Tabela(apresentar o conteúdo das variáveis)", width=70, height=1, command=consulta_tabela)
button1.grid(row=0, column=0, padx=10, pady=5)

button2 = tk.Button(frame, text="11 - Consultar Valores(apresentar valores máximo, mínimo e médio)", width=70, height=1, command=consulta_valores)
button2.grid(row=1, column=0, padx=10, pady=5)

button3 = tk.Button(frame, text="12 - Consultar Itens(apresentar listagem de item único da variável)", width=70, height=1, command=consulta_itens)
button3.grid(row=2, column=0, padx=10, pady=5)

button4 = tk.Button(frame, text="13 - Criar Lista contendo os dados da variável numérica(Lot_Area)", width=70, height=1, command=consultar_lista_num)
button4.grid(row=3, column=0, padx=10, pady=5)

button5 = tk.Button(frame, text="14 - Criar Lista contendo os dados da variável categórica(Garage_Type)", width=70, height=1, command=consultar_lista_categoria)
button5.grid(row=4, column=0, padx=10, pady=5)

button6 = tk.Button(frame, text="15 - Calcular soma dos valores acima da média dos valores da própria variável", width=70, height=1, command=calcular_soma)
button6.grid(row=5, column=0, padx=10, pady=5)

button7 = tk.Button(frame, text="16 - Contar ocorrência dos itens individuais da variável categórica(Garage_Type)", width=70, height=1, command=contar_itens)
button7.grid(row=6, column=0, padx=10, pady=5)

btn_github = tk.Button(root, text="GitHub", command=github)
btn_github.place(x=860,y=650,width=60,height=20)

btn_linkedin = tk.Button(root, text="Linkedin", command=linkedin)
btn_linkedin.place(x=930,y=650,width=60,height=20)



result_text = tk.Text(root, height=20, width=150)
result_text.pack(padx=60, pady=25)
#result_text.place(x=720,y=50,width=500,height=250)


footer = tk.Label(
    text="Este projeto é apenas para fins acadêmicos.\nIdealizado para mostrar as competências de matérias da faculdade, seu uso comercial não é permitido.\nEric F Guimaraes © - 2023",
    fg="white",
    bg="#154c79",
    width=190,
    height=3
)
footer.pack(fill='both', side='bottom')

root.mainloop()
