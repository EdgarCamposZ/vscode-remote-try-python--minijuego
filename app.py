#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def jugar_piedra_papel_tijera(jugador, oponente):
   opciones = ["piedra", "papel", "tijera"]

   if jugador == oponente:
       return "Empate"

   if jugador == "piedra":
       if oponente == "papel":
           return "Oponente gana"
       else:
           return "Jugador gana"

   if jugador == "papel":
       if oponente == "tijera":
           return "Oponente gana"
       else:
           return "Jugador gana"

   if jugador == "tijera":
       if oponente == "piedra":
           return "Oponente gana"
       else:
           return "Jugador gana"

def main():
   print("Bienvenido a Piedra, Papel o Tijera!")
   jugador = input("Elige: piedra, papel o tijera: ").lower()
   while jugador not in ["piedra", "papel", "tijera"]:
       print("Opción no válida. Por favor, elige piedra, papel o tijera.")
       jugador = input("Elige: piedra, papel o tijera: ").lower()
   oponente = random.choice(["piedra", "papel", "tijera"])
   resultado = jugar_piedra_papel_tijera(jugador, oponente)
   print(f"Jugador elige {jugador}")
   print(f"Oponente elige {oponente}")
   print(resultado)

def main():
   print("Bienvenido a Piedra, Papel o Tijera!")
   while True:
       jugador = input("Elige: piedra, papel o tijera: ").lower()
       while jugador not in ["piedra", "papel", "tijera"]:
           print("Opción no válida. Por favor, elige piedra, papel o tijera.")
           jugador = input("Elige: piedra, papel o tijera: ").lower()
       oponente = random.choice(["piedra", "papel", "tijera"])
       resultado = jugar_piedra_papel_tijera(jugador, oponente)
       print(f"Jugador elige {jugador}")
       print(f"Oponente elige {oponente}")
       print(resultado)
       jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
       if jugar_de_nuevo != "si":
           break
if __name__ == '__main__':
   main()

