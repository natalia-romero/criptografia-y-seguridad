import sys
import struct
import socket
import os
import time

def calcular_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        palabra = (data[i] << 8) + data[i + 1]
        checksum += palabra
        if checksum > 0xFFFF:
            checksum = (checksum & 0xFFFF) + 1
    return ~checksum & 0xFFFF

def añadir_data_paquete(letra, sequence):
    # Estructura de datos en little endian
    data = struct.pack('<B', ord(letra))
    data += os.urandom(2)
    data += b'\x00\x00\x00\x00\x00'
    data += bytes(range(10, 38))

    # Cambiar el byte menos significativo de la secuencia
    data = data[:-1] + bytes([sequence])

    return data

def añadir_timestamp_paquete():
    timestamp = int(time.time())
    return struct.pack('<I', timestamp)

def añadir_identifier_paquete(identifier):
    return struct.pack('>H', identifier)

def añadir_sequence_paquete(sequence):
    return struct.pack('>H', sequence)

def enviar_paquete(letra, identifier, sequence):
    # Crear un socket raw ICMP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except socket.error as e:
        print(f"Error al crear el socket: {e}")
        sys.exit(1)

    # Construir el paquete ICMP
    data = añadir_data_paquete(letra, sequence)
    timestamp = añadir_timestamp_paquete()
    identifier = añadir_identifier_paquete(identifier)
    sequence = añadir_sequence_paquete(sequence)

    icmp_header = struct.pack(">BBHHH", 8, 0, 0, struct.unpack('>H', identifier)[0], struct.unpack('>H', sequence)[0])
    icmp_checksum = calcular_checksum(icmp_header + data)
    icmp_header = struct.pack(">BBHHH", 8, 0, icmp_checksum, struct.unpack('>H', identifier)[0], struct.unpack('>H', sequence)[0])

    icmp_packet = icmp_header + data

    # Enviar el paquete ICMP
    try:
        sock.sendto(icmp_packet, ("127.0.0.1", 0))
    except socket.error as e:
        print(f"Error al enviar el paquete: {e}")
    finally:
        sock.close()

    print(f"Paquete ICMP de solicitud enviado para letra '{letra}' con timestamp {struct.unpack('<I', timestamp)[0]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python programa.py <texto>")
        sys.exit(1)

    texto = sys.argv[1]
    identifier = os.getpid() & 0xFFFF
    sequence = 1

    for letra in texto:
        enviar_paquete(letra, identifier, sequence)
        sequence += 1
