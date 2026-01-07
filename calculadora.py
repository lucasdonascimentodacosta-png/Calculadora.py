import tkinter as tk

# ===== JANELA =====
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#020617")
janela.resizable(False, False)

# ===== VARIÁVEL =====
expressao = ""

# ===== FUNÇÕES =====
def clicar(valor):
    global expressao
    expressao += str(valor)
    entrada_var.set(expressao)

def limpar():
    global expressao
    expressao = ""
    entrada_var.set("")

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        entrada_var.set(resultado)
        expressao = resultado
    except:
        entrada_var.set("Erro")
        expressao = ""

# ===== CAMPO DE TEXTO =====
entrada_var = tk.StringVar()

entrada = tk.Entry(
    janela,
    textvariable=entrada_var,
    font=("Segoe UI", 24),
    justify="right",
    bd=0,
    bg="#020617",
    fg="white"
)
entrada.pack(fill="x", ipady=15, padx=10, pady=10)

# ===== FRAME BOTÕES =====
frame = tk.Frame(janela, bg="#020617")
frame.pack(expand=True, fill="both")

# ===== BOTÕES =====
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for texto, linha, coluna in botoes:
    botao = tk.Button(
        frame,
        text=texto,
        font=("Segoe UI", 14),
        bg="#1e293b",
        fg="white",
        bd=0,
        command=lambda t=texto: clicar(t) if t not in ['=', 'C']
        else calcular() if t == '='
        else limpar()
    )
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

# ===== GRID RESPONSIVO =====
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# ===== INICIAR =====
janela.mainloop()
