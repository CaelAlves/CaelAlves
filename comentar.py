import tkinter as tk
import webbrowser
import pyautogui
import time
import pyperclip
import random
from tkinter import messagebox

def esperar_variavel(minimo=1, maximo=3):
    """Aguarda um tempo aleatório entre o mínimo e máximo fornecidos."""
    tempo_espera = random.uniform(minimo, maximo)
    print(f"Aguardando {tempo_espera:.2f} segundos...")
    time.sleep(tempo_espera)

def abrir_link():
    palavras = entrada_palavras.get("1.0", tk.END).strip().splitlines()
    link = entrada_link.get()
    
    if link:
        print("Link:", link)
        webbrowser.open(link)
        
        # Solicita ao usuário que mova o mouse até o ícone de comentário
        messagebox.showinfo("Mover o Mouse", "Movimente o mouse até o ícone de comentário (balão) e aguarde 5 segundos.")
        
        # Espera 5 segundos para o usuário realizar a ação
        time.sleep(5)
        
        # Captura a posição atual do mouse
        x, y = pyautogui.position()
        print(f"Posição capturada: x={x}, y={y}")
        
        # Exibe mensagem de posição copiada
        messagebox.showinfo("Posição Copiada", f"Posição do mouse copiada: x={x}, y={y}")
        
        # Loop sobre todas as palavras
        for palavra in palavras:
            # Copia a palavra atual
            pyperclip.copy(palavra)
            print("Palavra copiada:", palavra)
            
            # Espera um tempo aleatório antes de mover o mouse
            esperar_variavel(1, 2)
            
            # Mover o mouse para as coordenadas capturadas e clicar
            pyautogui.moveTo(x, y)
            pyautogui.click()
            
            # Espera um tempo aleatório antes de colar
            esperar_variavel(0.5, 1.5)
            
            # Pressiona Ctrl+V para colar a palavra
            pyautogui.hotkey('ctrl', 'v')
            
            # Pressiona Enter
            pyautogui.press('enter')
            
            # Espera um tempo aleatório entre 1 e 3 segundos
            esperar_variavel(1, 3)
    else:
        print("Por favor, insira um link.")

# Configurando a janela
janela = tk.Tk()
janela.title("Acessar Instagram")

# Entrada de palavras
tk.Label(janela, text="Digite uma lista de palavras:").pack()
entrada_palavras = tk.Text(janela, height=10, width=50)
entrada_palavras.pack()

# Entrada de link
tk.Label(janela, text="Digite o link da postagem do Instagram:").pack()
entrada_link = tk.Entry(janela, width=50)
entrada_link.pack()

# Botão para abrir o link e clicar
botao_abrir = tk.Button(janela, text="Abrir Link e Clicar", command=abrir_link)
botao_abrir.pack()

# Iniciar o loop da interface
janela.mainloop()
