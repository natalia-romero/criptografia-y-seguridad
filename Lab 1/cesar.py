import sys

def cifrar_cesar(texto, corrimiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            es_mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter) - ord('a')
            codigo = (codigo + corrimiento) % 26
            caracter_cifrado = chr(codigo + ord('a'))
            if es_mayuscula:
                caracter_cifrado = caracter_cifrado.upper()
            resultado += caracter_cifrado
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python cifrado_cesar.py <texto> <corrimiento>")
    else:
        texto_a_cifrar = sys.argv[1]
        corrimiento = int(sys.argv[2])
        texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
        print("Texto cifrado:", texto_cifrado)

