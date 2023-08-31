import sys
def descifrar_mensaje(mensaje_cifrado, veces):
  """Descifra un mensaje cifrado usando el cifrado César."""
  mensaje_descifrado = ""
  for letra in mensaje_cifrado:
    if letra.islower():
      ascii = ord(letra) - ord('a')
      nuevo_ascii = (ascii - veces) % 26 + ord('a')
      mensaje_descifrado += chr(nuevo_ascii)
    elif letra.isupper():
      ascii = ord(letra) - ord('A')
      nuevo_ascii = (ascii - veces) % 26 + ord('A')
      mensaje_descifrado += chr(nuevo_ascii)
    else:
           mensaje_descifrado += letra
  return mensaje_descifrado
if __name__ == "__main__":
  mensaje_cifrado = input("Ingresa el mensaje cifrado: ")
  veces = int(input("Cuantas veces quieres mover la letra: "))
  mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, veces)
  print(f"El mensaje descifrado es: {mensaje_descifrado}")