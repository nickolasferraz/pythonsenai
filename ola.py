import tkinter as tk
from tkinter import messagebox

def calcular_desconto():
    entrada = entrada_var.get()
    if entrada == '3':
        root.quit()
    else:
        try:
            preco_original = float(entrada_preco.get())
            desconto = 0.05
            novo_preco = preco_original - (preco_original * desconto)
            messagebox.showinfo("Resultado", f"O preço original é R${preco_original}. Na promoção, com o desconto de 5%, irá ficar R${novo_preco:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido para o preço.")

root = tk.Tk()
root.title("Calculadora de Desconto")

# Labels e Entry para entrada de dados
tk.Label(root, text="Boa tarde! Deseja fazer a conta? Se não, digite 3.").pack()
entrada_var = tk.StringVar()
entrada_entry = tk.Entry(root, textvariable=entrada_var)
entrada_entry.pack()

tk.Label(root, text="Qual é o preço do produto em R$?").pack()
entrada_preco = tk.Entry(root)
entrada_preco.pack()

# Botão para calcular desconto
calcular_button = tk.Button(root, text="Calcular Desconto", command=calcular_desconto)
calcular_button.pack()

root.mainloop()