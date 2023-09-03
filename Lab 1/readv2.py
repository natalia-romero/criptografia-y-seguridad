import sys
from scapy.all import rdpcap

# Frecuencia de letras en español (porcentaje)
frecuencia_letras = {
    'a': 0.1170,
    'b': 0.0171,
    'c': 0.0434,
    'd': 0.0501,
    'e': 0.1218,
    'f': 0.0069,
    'g': 0.0170,
    'h': 0.0070,
    'i': 0.0671,
    'j': 0.0044,
    'k': 0.0002,
    'l': 0.0497,
    'm': 0.0315,
    'n': 0.0671,
    'o': 0.0868,
    'p': 0.0251,
    'q': 0.0088,
    'r': 0.0687,
    's': 0.0798,
    't': 0.0463,
    'u': 0.0393,
    'v': 0.0090,
    'w': 0.0001,
    'x': 0.0022,
    'y': 0.0090,
    'z': 0.0052,
}

def descifrar_cesar(texto_cifrado, corrimiento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    descifrado = ''
    for letra in texto_cifrado:
        if letra.isalpha():
            indice = (alfabeto.index(letra) - corrimiento) % 26
            letra_descifrada = alfabeto[indice]
            descifrado += letra_descifrada
        else:
            descifrado += letra
    return descifrado

def calcular_probabilidad_descifrado(descifrado):
    descifrado = descifrado.lower()
    probabilidad = 1.0
    for letra in descifrado:
        if letra in frecuencia_letras:
            probabilidad *= frecuencia_letras[letra]
    return probabilidad

def encontrar_mensaje_cifrado(pcap_file):
    mensajes_posibles = []

    packets = rdpcap(pcap_file)
    for packet in packets:
        if packet.haslayer("ICMP") and packet["ICMP"].type == 8:  # Solo ICMP Request
            data = packet["ICMP"].load
            if data and len(data) > 0:
                primer_caracter = chr(data[0])
                mensajes_posibles.append(primer_caracter)

    print("Mensaje cifrado:")
    mensaje_cifrado = ''.join(mensajes_posibles)
    print(mensaje_cifrado)

    print("\nDescifrando mensajes posibles:")

    descifrados_posibles = []
    mejor_probabilidad = 0.0
    mejor_corrimiento = 0

    for corrimiento in range(26):
        descifrado = descifrar_cesar(mensaje_cifrado, corrimiento)
        descifrados_posibles.append(descifrado)
        probabilidad = calcular_probabilidad_descifrado(descifrado)

        if probabilidad >= mejor_probabilidad:
            mejor_probabilidad = probabilidad
            mejor_corrimiento = corrimiento
        
        print(f"Corrimiento {corrimiento}: {descifrado}")

    print("\nMensaje descifrado más probable:")
    mejor_descifrado = descifrados_posibles[mejor_corrimiento]
    print(f"\033[92m{mejor_descifrado}\033[0m (Corrimiento {mejor_corrimiento})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python programa.py <archivo.pcapng>")
        sys.exit(1)

    archivo_pcapng = sys.argv[1]
    encontrar_mensaje_cifrado(archivo_pcapng)
