import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:Lucas
apellido:Nogueira
Tutor:Marina/albana
---
Ejercicio: for_01
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

    Necesitamos saber:

    Nombre y género de la persona que más ganó.

    Promedio de dinero ganado en Ruleta.

    Porcentaje de personas que jugaron en el Tragamonedas.

    Cuál es el juego menos elegido por los ganadores.

    El nombre del jugador que ganó más dinero jugando Poker
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        primera_vez = True
        primera_vez_poker = True
        continuar = True
        dinero_ruleta = 0
        contador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0
        nombre_maximo_poker = "No ingreso jugadores de poker"
    
        while continuar:
            nombre = prompt("Datos", "Ingrese su nombre")
            while nombre == "":
                nombre = prompt("ERROR", "Reingrese su nombre")

            importe = prompt("Datos", "Ingrese importe ganado")
            importe = int (importe)
            while importe < 1000:
                importe = prompt("ERROR", "Reingrese importe ganado")
                importe = int (importe)

            genero = prompt("Datos", "Ingrese su genero")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("ERROR", "Reingrese su genero")
            
            juego = prompt("Datos", "Ingrese juego utilizado")    
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("ERROR", "Reingrese juego utilizado")   
            
            match juego:
                case "Ruleta":
                    dinero_ruleta += importe
                    contador_ruleta += 1
                case "Poker":
                    contador_poker += 1
                    if primera_vez_poker == True or importe > poker_maximo_importe:
                        poker_maximo_importe = importe
                        nombre_maximo_poker = nombre
                        primera_vez_poker == False
                case "Tragamonedas":
                    contador_tragamonedas += 1
            
            if primera_vez == True or importe > importe_maximo:
                importe_maximo = importe
                primera_vez = False
                nombre_maximo = nombre
                genero_maximo = genero
                
            continuar = question("UTN", "Desesa continuar?")
            
        jugadores_totales = contador_poker + contador_ruleta + contador_tragamonedas

        if primera_vez == True or importe > importe_maximo:
            importe_maximo = importe
            primera_vez = False
            nombre_maximo = nombre
            genero_maximo = genero

        if contador_ruleta == 0:
            promedio_ruleta_mensaje = "no ingreso dinero ganado en Ruleta"
        else:
            promedio_ruleta = dinero_ruleta / contador_ruleta
            promedio_ruleta_mensaje = f"Promedio de dinero ganado en Ruleta: {promedio_ruleta}"

        if contador_tragamonedas == 0:
            porcentaje_tragamonedas_mensaje = "No hubo jugadores de tragamonedas"
        else:
            porcentaje_tragamonedas = (contador_tragamonedas * 100) / jugadores_totales
            porcentaje_tragamonedas_mensaje = f"Promedio de jugadores en tragamonedas {porcentaje_tragamonedas}"
        
        if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
            juego_menos_elegido = "El juego menos elegido es Poker"
        elif contador_ruleta < contador_tragamonedas:
            juego_menos_elegido = "El juego menos elegido es Ruleta"
        else:
            juego_menos_elegido = "El juego menos elegido es Tragamonedas"


        alert ("Resultados",f"Nombre del maximo ganador: {nombre_maximo}\nGenero del maximo ganador: {genero_maximo}\n{promedio_ruleta_mensaje}\n{porcentaje_tragamonedas_mensaje}\n{juego_menos_elegido}\nNombre del maximo ganador en poker: {nombre_maximo_poker}")

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()