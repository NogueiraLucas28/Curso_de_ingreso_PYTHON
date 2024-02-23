import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        acumulador_edades = 0
        acumulador_votos = 0
        contador_candidatos = 0
        bandera = True

        while True:
            nombre = prompt("Carga de datos", "Ingrese nombre")
            if nombre == None:
                break
            edad = prompt("Carga de datos", "Ingrese edad")
            edad = int(edad)
            
            if edad < 25:
                alert("Error", "La edad minima es 25")
                break
            votos = prompt("Carga de datos", "Ingrese votos")
            votos = int(votos)
            if votos < 0:   
                alert("Error", "No puede tener menos de 0 votos")
                break
            contador_candidatos += 1
            acumulador_edades += edad
            acumulador_votos += votos
            if (bandera == True) or (votos > maximos_votos):
                maximos_votos = votos
                candidato_mas_votos = nombre

            if (bandera == True) or (votos < minimos_votos):
                minimos_votos = votos
                candidato_menos_votos = nombre
                edad_candidato_menos_votos = edad
                bandera = False
            
            
            
        promedio_edades = acumulador_edades / contador_candidatos


        mensaje = f"candidato mas votado: {candidato_mas_votos},    candidato menos votad: {candidato_menos_votos},     edad del menos votado:{edad_candidato_menos_votos},      promedio edades: {promedio_edades},      votos totales:{acumulador_votos}"
        print(mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
