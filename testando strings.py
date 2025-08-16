frase = ""
exit = False
# --- IGNORE ---

while not exit:
    texto = input("Digite algo: ")
    if texto == "/exit":
        exit = True
        break
    frase = frase + " " + texto
    
    # ...existing code...
print(f"Você digitou: {frase}")
