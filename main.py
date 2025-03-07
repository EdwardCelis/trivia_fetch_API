from trivia import trivia_fetch

def main():
    num = input("Ingresa un número para descubrir su trivia: ")
    if num.isdigit():
        resultado = trivia_fetch(num)
        print(f"\n🔢 {resultado['number']}: {resultado['text']}")
    else:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
