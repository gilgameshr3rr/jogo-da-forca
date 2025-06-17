import random

def escolher_palavra():
    with open("300-palavras-tecnologia.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()      
    palavras = []  
    for palavra in conteudo.split():  
        palavra_limpa = palavra.strip() 
        if palavra_limpa != "": 
            palavras.append(palavra_limpa.upper()) 
            print(palavras)
    return random.choice(palavras) 



def inicializar_jogo(palavra):
    progresso = []
    for letra in palavra:
        progresso.append("_")
    letras_tentadas = []
    erros = 0
    return progresso, letras_tentadas, erros

def exibir_forca(erros):
    fases = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]
    if erros >= len(fases):
        return fases[-1]
    return fases[erros]

def exibir_estado_palavra(progresso):
    return " ".join(progresso)

def verificar_letra(letra, palavra, progresso):
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                progresso[i] = letra
        return True
    else:
        return False

def verificar_vitoria(progresso):
    if "_" in progresso:
        return False
    else:
        return True

def main():
    palavra = escolher_palavra()
    progresso, letras_tentadas, erros = inicializar_jogo(palavra)
    max_erros = 6

    print("\n🎉 Bem-vindo ao Jogo da Forca!")

    while True:
        print("\n🎮 NOVA RODADA")
        print("-" * 30)
        print(exibir_forca(erros))
        print(f"🎯 Palavra: {exibir_estado_palavra(progresso)}")
        print(f"📌 Letras tentadas: {', '.join(letras_tentadas)}")
        print("-" * 30)

        letra = input("➡️ Digite uma letra: ").strip().upper()

        if len(letra) != 1 or not letra.isalpha():
            print("❌ Entrada inválida. Digite apenas uma única letra do alfabeto.")
            continue

        if letra in letras_tentadas:
            print("⚠️ Você já tentou essa letra. Tente novamente.")
            continue

        letras_tentadas.append(letra)

        if verificar_letra(letra, palavra, progresso):
            print(f"✅ A letra '{letra}' está na palavra!")
        else:
            erros += 1
            print(f"❌ A letra '{letra}' NÃO está na palavra.")

        if verificar_vitoria(progresso):
            print("\n🏁 FIM DE JOGO")
            print("-" * 30)
            print(exibir_forca(erros))
            print(f"🎯 Palavra: {exibir_estado_palavra(progresso)}")
            print(f"📌 Letras tentadas: {', '.join(letras_tentadas)}")
            print("")
            print("         ★ ★ ★ ★ ★ ★")
            print("   ┌──────────────────────┐")
            print("   │     VOCÊ VENCEU!     │")
            print("   │        🏆🏆         │")
            print("   └──────────────────────┘")
            print(f"\n🎉 Parabéns! Você ganhou! A palavra é: {palavra}")
            break

        if erros >= max_erros:
            print("\n🏁 FIM DE JOGO")
            print("-" * 30)
            print(exibir_forca(erros))
            print(f"🎯 Palavra: {exibir_estado_palavra(progresso)}")
            print(f"📌 Letras tentadas: {', '.join(letras_tentadas)}")
            print(f"\n💀 Você perdeu! A palavra era: {palavra}")
            break

    print("\n🔁 Deseja jogar novamente? (S/N)")
    resposta = input().strip().upper()
    if resposta == "S":
        main()
    else:
        print("👋 Encerrando o jogo!")

main()
