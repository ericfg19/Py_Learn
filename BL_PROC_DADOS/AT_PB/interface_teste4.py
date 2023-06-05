import tkinter as tk
import sqlite3
import ctypes as ct
import pandas as pd
from statistics import mean

def consulta_tabela():
    result_text.delete("1.0", "end-1c") # Deletar texto do result
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db') # conexao com db
    housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consulta_valores():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
    housingdb = pd.read_sql_query("SELECT MAX(lot_area) AS Máximo, MIN(lot_area) as Mínimo, AVG(lot_area) as Média from PB_tabela", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consulta_itens():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
    housingdb = pd.read_sql_query("SELECT * FROM PB_Tabela WHERE garage_type = 'Detchd'", cnx)
    cnx.close()
    result_text.insert(tk.END, str(housingdb) + "\n")

def consultar_lista_num():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
    consulta = "SELECT lot_area FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_num = resultado['Lot_Area'].tolist()
    result_text.insert(tk.END, str(lista_var_num) + "\n")

def consultar_lista_categoria():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
    consulta = "SELECT garage_type FROM PB_Tabela"
    resultado = pd.read_sql_query(consulta, cnx)
    cnx.close()
    lista_var_categoria = resultado['Garage_Type'].tolist()
    result_text.insert(tk.END, str(lista_var_categoria) + "\n")

def calcular_soma():
    result_text.delete("1.0", "end-1c")
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
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
    cnx = sqlite3.connect('C:\\PB\\PB_Tabela.db')
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

def dark_title_bar(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

root = tk.Tk()
root.title("Projeto de Bloco")

root.geometry("900x700")
dark_title_bar(root)


frame = tk.Frame(root)
frame.pack(pady=15)



button1 = tk.Button(frame, text="10 - Consultar Tabela(apresenta o conteúdo das variáveis)", command=consulta_tabela)
button1.grid(row=0, column=0, padx=10, pady=5)

button2 = tk.Button(frame, text="11 - Consultar Valores(valores máximo, mínimo e médio)", command=consulta_valores)
button2.grid(row=1, column=0, padx=10, pady=5)

button3 = tk.Button(frame, text="12 - Consultar Itens(listagem de itens únicos da variável)", command=consulta_itens)
button3.grid(row=2, column=0, padx=10, pady=5)

button4 = tk.Button(frame, text="13 - Criar Lista Numérica", command=consultar_lista_num)
button4.grid(row=3, column=0, padx=10, pady=5)

button5 = tk.Button(frame, text="14 - Criar Lista Categórica", command=consultar_lista_categoria)
button5.grid(row=4, column=0, padx=10, pady=5)

button6 = tk.Button(frame, text="15 - Calcular Soma", command=calcular_soma)
button6.grid(row=5, column=0, padx=10, pady=5)

button7 = tk.Button(frame, text="16 - Contar Itens", command=contar_itens)
button7.grid(row=6, column=0, padx=10, pady=5)

result_text = tk.Text(root, height=20, width=150)
result_text.pack(padx=60, pady=25)

footer = tk.Label(
    text="Projeto de Bloco - Eric F Guimaraes",
    fg="white",
    bg="#154c79",
    width=190,
    height=1
)
footer.pack(fill='both', side='bottom')

root.mainloop()
